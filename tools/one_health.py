#!/usr/bin/env python3
"""Read-only integrity scanner for the One repository; Python standard library only."""
from __future__ import annotations
import argparse, ast, difflib, hashlib, json, os, platform, re, stat, subprocess, sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

SCHEMA_VERSION = "one-health-report/2"
SKIP_DIRS = {".git", "target", ".venv", "venv", "node_modules", "__pycache__", ".mypy_cache", ".pytest_cache", "health-baseline"}
TEXT_SUFFIXES = {".md", ".py", ".toml", ".json", ".yml", ".yaml", ".sh", ".ps1", ".one", ".txt", ".rs", ".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
JAVASCRIPT_SUFFIXES = {".js", ".mjs", ".cjs", ".jsx", ".ts", ".tsx"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
FENCE_RE = re.compile(r"^( {0,3})(\x60{3,}|~{3,})(.*)$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{40}$")
CORE_COMMANDS = ("one buat", "one periksa", "one jalankan", "one test", "one bangun", "one package", "one lihat struktur", "one version", "one help")

def _git(root: Path, *args: str) -> str | None:
    try:
        env = os.environ.copy()
        env["GIT_PAGER"] = "cat"
        result = subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True, text=True, timeout=5, env=env)
    except (OSError, subprocess.SubprocessError):
        return None
    return result.stdout.strip()

def _finding(detector, rule, path, line, severity, confidence, summary, evidence, recommendation, status="open"):
    stable_evidence = evidence if isinstance(evidence, str) else json.dumps(evidence, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    stable = hashlib.sha256(f"{detector}\0{rule}\0{path}\0{stable_evidence}".encode("utf-8")).hexdigest()[:12]
    return {"finding_id": f"OH-{stable}", "detector_id": detector, "rule_id": rule, "status": status,
            "severity": severity, "confidence": confidence, "path": path, "line": line,
            "summary": summary, "evidence": evidence, "recommendation": recommendation}

def _files(root: Path):
    for current, dirs, names in os.walk(root, followlinks=False):
        # os.walk with followlinks=False does not put directory symlinks in
        # names and will not descend into them. Inspect and yield them
        # explicitly before pruning traversal, otherwise escaping directory
        # symlinks evade the path-integrity detector entirely.
        for name in sorted(dirs[:]):
            path = Path(current) / name
            if path.is_symlink():
                dirs.remove(name)
                try: rel = path.relative_to(root).as_posix()
                except ValueError: continue
                yield path, rel
            elif name in SKIP_DIRS:
                dirs.remove(name)
        dirs[:] = sorted(dirs)
        for name in sorted(names):
            path = Path(current) / name
            try: rel = path.relative_to(root).as_posix()
            except ValueError: continue
            if name in {"one-health-report.json", "one-health-report.md"} and not path.is_symlink():
                continue
            if path.is_file() or path.is_symlink(): yield path, rel

def _markdown_anchors(text: str) -> set[str]:
    """Return a conservative set of CommonMark-style heading and explicit HTML anchors."""
    anchors = set()
    duplicate_counts = {}
    for line in text.splitlines():
        heading = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            title = re.sub(r"!\[([^\]]+)\]\([^)]*\)", r"\1", heading.group(1))
            title = re.sub(r"[\x60*_~]", "", title).lower()
            slug = re.sub(r"[^\w\- ]", "", title, flags=re.UNICODE).strip()
            slug = re.sub(r"\s+", "-", slug)
            count = duplicate_counts.get(slug, 0)
            duplicate_counts[slug] = count + 1
            anchors.add(slug if count == 0 else f"{slug}-{count}")
        for explicit in re.finditer(r"""\b(?:id|name)\s*=\s*["']([^"']+)["']""", line, re.IGNORECASE):
            anchors.add(explicit.group(1))
    return anchors

def _markdown_links(path, rel, root, text, findings):
    for match in LINK_RE.finditer(text):
        raw = match.group(1).strip()
        target = raw[1:raw.index(">")] if raw.startswith("<") and ">" in raw else (raw.split()[0] if raw else "")
        if not target: continue
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc or target.startswith("//"): continue
        target_path = unquote(parsed.path)
        line = text.count("\n", 0, match.start()) + 1
        resolved = (path.parent / target_path).resolve() if target_path else path.resolve()
        try: resolved.relative_to(root.resolve())
        except ValueError:
            findings.append(_finding("markdown-links", "path-escape", rel, line, "high", "high",
                "Tautan Markdown keluar dari root repositori.", target, "Ubah tautan agar tetap berada di dalam repositori."))
            continue
        if not resolved.exists():
            findings.append(_finding("markdown-links", "broken-relative-link", rel, line, "medium", "high",
                "Tautan relatif menunjuk ke jalur yang tidak ditemukan.", target,
                "Perbaiki target atau hapus tautan jika memang sudah usang."))
            continue
        fragment = unquote(parsed.fragment)
        if fragment and resolved.is_file() and (resolved.suffix.lower() == ".md" or resolved == path.resolve()):
            try:
                target_text = resolved.read_text(encoding="utf-8")
            except (OSError, UnicodeError):
                continue
            if fragment not in _markdown_anchors(target_text):
                findings.append(_finding("markdown-links", "broken-heading-anchor", rel, line, "medium", "medium",
                    "Tautan Markdown menuju heading atau anchor yang tidak ditemukan.", target,
                    "Perbarui fragmen tautan agar cocok dengan heading/ID aktual, atau perbaiki heading target."))

def _scan_markdown(path, rel, root, text, findings):
    _markdown_links(path, rel, root, text, findings)
    active = None
    for number, line in enumerate(text.splitlines(), 1):
        match = FENCE_RE.match(line)
        if not match: continue
        marker = match.group(2)
        if active is None: active = (marker[0], len(marker), number)
        elif marker[0] == active[0] and len(marker) >= active[1] and not match.group(3).strip(): active = None
    if active:
        findings.append(_finding("markdown-structure", "unclosed-code-fence", rel, active[2], "medium", "high",
            "Blok kode Markdown tidak memiliki penutup yang cocok.", f"Fence dibuka pada baris {active[2]}.",
            "Tambahkan fence penutup yang sesuai atau perbaiki batas blok kode."))

SECRET_PATTERNS = [
    ("private-key-material", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"), "critical", "high"),
    ("github-token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9_]{30,}|github_pat_[A-Za-z0-9_]{30,})\b"), "critical", "high"),
    ("aws-access-key-id", re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "high", "high"),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"), "high", "high"),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), "high", "high"),
    ("stripe-live-secret", re.compile(r"\bsk_live_[0-9A-Za-z]{20,}\b"), "critical", "high"),
    ("npm-access-token", re.compile(r"\bnpm_[A-Za-z0-9]{30,}\b"), "high", "high"),
    ("pypi-access-token", re.compile(r"\bpypi-[A-Za-z0-9_-]{50,}\b"), "high", "high"),
    ("generic-hardcoded-secret", re.compile(r"""(?i)\b(?:api[_-]?key|access[_-]?token|client[_-]?secret|password|passwd|secret[_-]?key)\b\s*[:=]\s*["']([^"'\\\s]{16,})["']"""), "high", "medium"),
]
PLACEHOLDER_SECRET = re.compile(r"(?i)(?:example|sample|placeholder|changeme|change_me|your[_-]?|dummy|redacted|<[^>]+>|\$\{[^}]+\}|\$[A-Z][A-Z0-9_]*|process\.env|os\.environ|secrets\.)")

def _ast_name(node) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = _ast_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return ""


def _scan_python_security(rel: str, text: str, findings: list[dict]) -> None:
    """Conservative AST correlation for obfuscated execution and sensitive-data egress."""
    try:
        tree = ast.parse(text, filename=rel)
    except SyntaxError:
        return

    calls = [node for node in ast.walk(tree) if isinstance(node, ast.Call)]
    decoders = {
        "base64.b64decode", "binascii.a2b_base64", "binascii.unhexlify", "bytes.fromhex",
        "codecs.decode", "marshal.loads", "zlib.decompress", "lzma.decompress", "gzip.decompress",
    }
    dynamic = {"eval", "exec", "compile"}
    obfuscated_calls = set()
    for call in calls:
        if _ast_name(call.func) not in dynamic or not call.args:
            continue
        nested = {_ast_name(child.func) for child in ast.walk(call.args[0]) if isinstance(child, ast.Call)}
        if nested.intersection(decoders):
            obfuscated_calls.add(id(call))
            findings.append(_finding("security-code", "obfuscated-execution", rel, getattr(call, "lineno", None),
                "high", "high", "Kode yang didekode atau dibongkar secara dinamis langsung diteruskan ke eval/exec/compile.",
                "AST correlation: decoder-or-deserializer -> dynamic-code-execution; payload bytes omitted.",
                "Jangan jalankan payload. Telusuri asal data, hapus jalur eksekusi yang tidak perlu, dan tambahkan fixture regresi."))
            break

    for call in calls:
        if _ast_name(call.func) not in {"eval", "exec"} or id(call) in obfuscated_calls:
            continue
        findings.append(_finding("security-code", "dynamic-code-execution", rel, getattr(call, "lineno", None),
            "medium", "low", "AST menemukan pemanggilan eval/exec; konteks dan aliran data menentukan risikonya.",
            "AST call node; string literal dan komentar tidak diperlakukan sebagai pemanggilan kode.",
            "Tinjau asal kode, aliran data, batas kepercayaan, dan apakah eksekusi dinamis dapat dihindari."))
        break

    fetch_calls = {
        "requests.get", "httpx.get", "urllib.request.urlopen", "urlopen",
        "http.client.HTTPConnection.getresponse", "aiohttp.ClientSession.get",
    }
    execute_calls = dynamic.union({
        "os.system", "os.popen", "subprocess.run", "subprocess.Popen",
        "subprocess.call", "subprocess.check_call", "subprocess.check_output",
    })
    egress_calls = {
        "requests.post", "requests.put", "requests.patch", "requests.request",
        "httpx.post", "httpx.put", "httpx.patch", "httpx.request",
        "urllib.request.urlopen", "urlopen", "http.client.HTTPConnection.request",
        "socket.socket.send", "socket.socket.sendall", "smtplib.SMTP.sendmail",
        "aiohttp.ClientSession.post", "aiohttp.ClientSession.put",
    }
    sensitive_names = {"password", "passwd", "secret", "token", "credential", "credentials", "api_key", "private_key"}
    sensitive_text = re.compile(r"(?i)(?:/\.ssh(?:/|$)|/\.aws(?:/|$)|\.env\b|id_rsa|credentials|private[_ -]?key|api[_ -]?key)")
    sensitive_env_name = re.compile(r"(?i)^[A-Z][A-Z0-9_]*(?:SECRET|TOKEN|PASSWORD|CREDENTIAL|API_KEY)[A-Z0-9_]*$")

    def source_markers(node, tainted_names):
        markers = set()
        for child in ast.walk(node):
            if isinstance(child, ast.Attribute):
                name = _ast_name(child)
                if name in {"os.environ", "os.getenv", "os.environ.get", "getenv", "environ", "Path.home", "pathlib.Path.home"}:
                    markers.add("environment-or-home-directory")
            elif isinstance(child, ast.Call) and _ast_name(child.func).endswith((".getenv", ".getpass")):
                markers.add("environment-or-prompt-source")
            elif isinstance(child, ast.Name) and (child.id.lower() in sensitive_names or child.id in tainted_names):
                markers.add("credential-like-identifier")
            elif isinstance(child, ast.Constant) and isinstance(child.value, str) and (
                sensitive_text.search(child.value) or (child.value.isupper() and sensitive_env_name.fullmatch(child.value))
            ):
                markers.add("sensitive-path-or-label")
        return markers

    def trusted_github_api_client(call):
        """Recognize only the collector's narrow authenticated api.github.com client pattern."""
        if _ast_name(call.func) not in {"urlopen", "urllib.request.urlopen"}:
            return False
        if len(call.args) != 1 or not isinstance(call.args[0], ast.Name):
            return False
        api_root_ok = any(
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "API_ROOT" for target in node.targets)
            and isinstance(node.value, ast.Constant)
            and node.value.value == "https://api.github.com"
            for node in tree.body
        )
        if not api_root_ok:
            return False
        external_urls = {
            node.value for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
            and re.match(r"(?i)^https?://", node.value)
        }
        if external_urls != {"https://api.github.com"}:
            return False

        parents = {}
        for parent_node in ast.walk(tree):
            for child in ast.iter_child_nodes(parent_node):
                parents[child] = parent_node

        def enclosing_function(node):
            while node in parents:
                node = parents[node]
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    return node
            return None

        request_fn = next((node for node in tree.body
                           if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                           and node.name == "_request_json"), None)
        collector_fn = next((node for node in tree.body
                             if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
                             and node.name == "collect_ci_health"), None)
        if request_fn is None or collector_fn is None or enclosing_function(call) is not request_fn:
            return False

        request_name = call.args[0].id
        request_assignment_ok = False
        for node in ast.walk(request_fn):
            if not isinstance(node, ast.Assign):
                continue
            if not any(isinstance(target, ast.Name) and target.id == request_name for target in node.targets):
                continue
            value = node.value
            if not isinstance(value, ast.Call) or _ast_name(value.func) not in {"Request", "urllib.request.Request"}:
                continue
            if not value.args or not isinstance(value.args[0], ast.Name) or value.args[0].id != "url":
                continue
            headers = next((keyword.value for keyword in value.keywords if keyword.arg == "headers"), None)
            if not isinstance(headers, ast.Dict):
                continue
            for key, header_value in zip(headers.keys, headers.values):
                if not (isinstance(key, ast.Constant) and isinstance(key.value, str)
                        and key.value.lower() == "authorization" and isinstance(header_value, ast.JoinedStr)):
                    continue
                if any(isinstance(child, ast.Name) and child.id == "token" for child in ast.walk(header_value)):
                    request_assignment_ok = True
        if not request_assignment_ok:
            return False

        defaults = {}
        if collector_fn.args.defaults:
            first_default = len(collector_fn.args.args) - len(collector_fn.args.defaults)
            defaults = {arg.arg: default for arg, default in
                        zip(collector_fn.args.args[first_default:], collector_fn.args.defaults)}
        request_json_default = defaults.get("request_json")
        if not (isinstance(request_json_default, ast.Name) and request_json_default.id == "_request_json"):
            return False

        base_ok = any(
            isinstance(node, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "base" for target in node.targets)
            and isinstance(node.value, ast.JoinedStr)
            and any(isinstance(child, ast.Name) and child.id == "API_ROOT" for child in ast.walk(node.value))
            for node in ast.walk(collector_fn)
        )
        if not base_ok:
            return False
        request_calls = [
            node for node in ast.walk(collector_fn)
            if isinstance(node, ast.Call) and _ast_name(node.func) == "request_json"
        ]
        if not request_calls or not all(
            node.args and isinstance(node.args[0], ast.JoinedStr)
            and any(isinstance(child, ast.Name) and child.id == "base" for child in ast.walk(node.args[0]))
            for node in request_calls
        ):
            return False
        other_sinks = [
            node for node in calls
            if _ast_name(node.func) in egress_calls and node is not call
        ]
        return not other_sinks

    assignments = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            targets = node.targets
            value = node.value
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            targets = [node.target]
            value = node.value
        else:
            continue
        names = [target.id for target in targets if isinstance(target, ast.Name)]
        if names:
            assignments.append((names, value))

    # Track only simple local assignments. This deliberately avoids claiming general taint analysis.
    tainted_names, remote_names = set(), set()
    for _ in range(4):
        changed = False
        for names, value in assignments:
            value_nodes = list(ast.walk(value))
            value_calls = {_ast_name(node.func) for node in value_nodes if isinstance(node, ast.Call)}
            value_names = {node.id for node in value_nodes if isinstance(node, ast.Name)}
            if source_markers(value, tainted_names) or value_names.intersection(tainted_names):
                for name in names:
                    if name not in tainted_names:
                        tainted_names.add(name)
                        changed = True
            if value_calls.intersection(fetch_calls) or value_names.intersection(remote_names):
                for name in names:
                    if name not in remote_names:
                        remote_names.add(name)
                        changed = True
        if not changed:
            break

    for call in calls:
        name = _ast_name(call.func)
        descendants = list(ast.walk(call))
        nested_calls = {_ast_name(child.func) for child in descendants if isinstance(child, ast.Call)}
        nested_names = {child.id for child in descendants if isinstance(child, ast.Name)}
        if name in execute_calls and (
            nested_calls.intersection(fetch_calls) or nested_names.intersection(remote_names)
        ):
            findings.append(_finding("security-code", "downloaded-code-execution", rel, getattr(call, "lineno", None),
                "high", "medium", "Data yang diturunkan dari pemanggilan jaringan berkorelasi dengan primitive eksekusi kode/proses.",
                "AST local-assignment/source-sink correlation; network data and payload omitted.",
                "Tinjau asal payload dan aliran data. Jangan mengeksekusi konten jaringan; gunakan artefak terverifikasi dan digest."))
            break

    # Correlate sensitive sources with the actual network-sink expression, not merely the same file.
    for call in calls:
        name = _ast_name(call.func)
        if name not in egress_calls:
            continue
        markers = source_markers(call, tainted_names)
        if not markers:
            continue
        if trusted_github_api_client(call):
            continue
        findings.append(_finding("security-code", "sensitive-data-egress", rel, getattr(call, "lineno", None),
            "high", "medium",
            "Referensi environment/credential atau jalur sensitif terdapat pada ekspresi API pengiriman jaringan.",
            f"source_indicators={','.join(sorted(markers))}; sink_api={name}; values_redacted=true",
            "Periksa tujuan jaringan dan data yang dikirim. Cabut kredensial jika terpapar; jangan jalankan berkas untuk menguji temuan."))
        break

    for call in calls:
        if _ast_name(call.func) not in {"subprocess.run", "subprocess.Popen", "subprocess.call",
                                       "subprocess.check_call", "subprocess.check_output"}:
            continue
        if any(keyword.arg == "shell" and isinstance(keyword.value, ast.Constant) and keyword.value.value is True
               for keyword in call.keywords):
            findings.append(_finding("security-code", "subprocess-shell-true-ast", rel,
                getattr(call, "lineno", None), "medium", "high",
                "AST menemukan subprocess dengan shell=True, termasuk pemanggilan multiline.",
                "AST keyword shell=True; exploitability depends on argument control.",
                "Utamakan argumen berbentuk daftar dan shell=False; validasi batas kepercayaan untuk semua argumen."))

AGENT_SURFACE_NAMES = {
    "agents.md", "claude.md", "gemini.md", "copilot-instructions.md",
    ".cursorrules", ".windsurfrules",
}
PROMPT_OVERRIDE = re.compile(
    r"(?i)\b(?:ignore|disregard|override|forget)\s+(?:all\s+)?(?:the\s+)?"
    r"(?:previous|prior|above|system|developer)\s+(?:instructions?|rules?|polic(?:y|ies))\b|"
    r"\b(?:ignore|disregard)\s+(?:all\s+)?(?:safety|security)\s+(?:rules|checks|policies)\b"
)
PROMPT_SECRET_ACTION = re.compile(
    r"(?i)\b(?:reveal|print|dump|exfiltrate|upload|send|transmit|expose)\b.{0,100}"
    r"\b(?:secrets?|tokens?|passwords?|credentials?|private keys?|environment variables?|system prompts?|api keys?)\b|"
    r"\b(?:secrets?|tokens?|passwords?|credentials?|private keys?|environment variables?|system prompts?|api keys?)\b.{0,100}"
    r"\b(?:upload|send|exfiltrate|reveal|dump|print|transmit|expose)\b"
)


def _is_agent_instruction_surface(rel: str) -> bool:
    normalized = "/" + rel.replace("\\", "/").lower().strip("/") + "/"
    basename = Path(rel).name.lower()
    return (
        basename in AGENT_SURFACE_NAMES
        or any(marker in normalized for marker in (
            "/.cursor/", "/.claude/", "/.github/instructions/", "/prompts/", "/agents/",
        ))
        or basename.endswith((".prompt", ".prompt.md", ".agent.md"))
    )


DEPENDENCY_MANIFEST_NAMES = {
    "requirements.txt", "requirements-dev.txt", "requirements-test.txt",
    "pyproject.toml", "poetry.lock", "pdm.lock", "uv.lock", "pipfile", "pipfile.lock",
    "cargo.toml", "cargo.lock", "package.json", "package-lock.json", "npm-shrinkwrap.json",
    "pnpm-lock.yaml", "yarn.lock", "bun.lock", "bun.lockb", "go.mod", "go.sum",
    "composer.json", "composer.lock", "gemfile", "gemfile.lock", "pom.xml",
    "build.gradle", "build.gradle.kts", "gradle.lockfile",
}


def _is_dependency_surface(rel: str) -> bool:
    """Recognize manifests/lockfiles, not arbitrary JSON/TOML/text files, for coverage accounting."""
    path = Path(rel)
    name = path.name.lower()
    return (
        name in DEPENDENCY_MANIFEST_NAMES
        or (name.startswith("requirements") and name.endswith(".txt"))
        or (name.startswith("package") and name.endswith(".json"))
    )


def _scan_javascript_security(rel: str, text: str, findings: list[dict]) -> None:
    """Targeted JavaScript/TypeScript heuristics; findings are leads, not proof of exploitability."""
    obfuscated = re.search(
        r"\b(?:eval|Function)\s*\(\s*(?:Buffer\.from|atob|decodeURIComponent)\s*\(",
        text,
    )
    if obfuscated:
        line = text.count("\n", 0, obfuscated.start()) + 1
        findings.append(_finding("security-javascript", "node-obfuscated-execution", rel, line,
            "high", "medium",
            "JavaScript mengirim data yang didekode langsung ke primitive eksekusi dinamis.",
            "Static correlation: eval/Function + Buffer.from/atob/decodeURIComponent; payload omitted.",
            "Jangan jalankan payload. Telusuri sumber data, hilangkan eksekusi dinamis jika tidak diperlukan, dan verifikasi asal payload."))

    network = re.search(r"\b(?:fetch|axios\.(?:get|request)|https?\.get|request)\s*\(", text)
    dynamic = re.search(r"\b(?:eval|Function)\s*\(", text)
    child_import = re.search(
        r"(?:require\s*\(\s*['\"](?:node:)?child_process['\"]\s*\)|"
        r"(?:from\s+|import\s*\(\s*)['\"](?:node:)?child_process['\"])",
        text,
    )
    child_exec = re.search(r"\b(?:exec|execSync)\s*\(", text)
    if network and (dynamic or (child_import and child_exec)):
        line = text.count("\n", 0, (dynamic or child_exec).start()) + 1
        findings.append(_finding("security-javascript", "node-downloaded-code-execution", rel, line,
            "high", "medium",
            "Satu berkas menggabungkan akses jaringan dengan eksekusi kode dinamis atau primitive child-process shell.",
            "Static correlation: network-access + dynamic/process execution; data flow is not proven.",
            "Tinjau asal konten dan aliran data tanpa menjalankan berkas. Verifikasi digest/provenance dan gunakan API tanpa shell bila memungkinkan."))

    sensitive_source = re.search(
        r"(?i)(?:process\s*\.\s*env(?:\s*(?:\.\s*[A-Z_][A-Z0-9_]*|\[\s*['\"][^'\"]+['\"]\s*\]))?|"
        r"(?:\.ssh(?:/|\\)|\.aws(?:/|\\)|\.env\b|private[_ -]?key|credential|password|secret|token|api[_ -]?key))",
        text,
    )
    egress = re.search(
        r"\b(?:fetch|axios\.(?:post|put|request)|https?\.request|navigator\.sendBeacon|"
        r"new\s+WebSocket)\s*\(",
        text,
    )
    if sensitive_source and egress:
        line = text.count("\n", 0, egress.start()) + 1
        findings.append(_finding("security-javascript", "node-sensitive-data-egress", rel, line,
            "high", "medium",
            "Indikator environment/kredensial berkorelasi dengan API pengiriman jaringan dalam berkas JavaScript/TypeScript.",
            "Static source/sink correlation; values and destination omitted; data flow is not proven.",
            "Periksa tujuan dan data yang dikirim, rotasi kredensial bila benar terpapar, dan jangan mengeksekusi berkas untuk menguji temuan."))

    if child_import and child_exec:
        line = text.count("\n", 0, child_exec.start()) + 1
        findings.append(_finding("security-javascript", "node-child-process-shell-execution", rel, line,
            "medium", "medium",
            "Berkas mengimpor child_process dan memanggil exec/execSync yang menggunakan shell.",
            "Static import/call correlation; input control and runtime context are not proven.",
            "Utamakan execFile/spawn dengan argumen terpisah dan shell disabled; validasi seluruh argumen dari sumber eksternal."))


def _scan_security(rel: str, text: str, findings: list[dict]) -> None:
    """Read-only security heuristics. Never include matched secret bytes in reports."""
    suffix = Path(rel).suffix.lower()
    for number, line in enumerate(text.splitlines(), 1):
        for rule, pattern, severity, confidence in SECRET_PATTERNS:
            match = pattern.search(line)
            if not match:
                continue
            matched = match.group(1) if rule == "generic-hardcoded-secret" and match.lastindex else match.group(0)
            if rule == "generic-hardcoded-secret" and PLACEHOLDER_SECRET.search(matched):
                continue
            fingerprint = hashlib.sha256(matched.encode("utf-8")).hexdigest()[:10]
            findings.append(_finding("security-secrets", rule, rel, number, severity, confidence,
                "Kemungkinan kredensial atau materi private key tertanam di berkas; nilai rahasia sengaja tidak ditampilkan.",
                f"pattern={rule}; fingerprint_sha256_prefix={fingerprint}; matched_value_redacted=true",
                "Cabut/rotasi kredensial jika nyata, hapus dari working tree, pindahkan ke secret manager/environment, dan bersihkan riwayat Git sesuai prosedur insiden. Jangan tempelkan nilai rahasia ke laporan."))
        if rel.startswith(".github/workflows/"):
            workflow_rules = [
                ("pipe-to-shell", re.compile(r"\b(?:curl|wget)\b[^\n|]*\|\s*(?:sudo\s+)?(?:ba)?sh\b"), "high", "medium",
                 "Workflow mengalirkan konten jaringan langsung ke shell."),
                ("write-all-permissions", re.compile(r"(?m)^\s*permissions\s*:\s*write-all\s*$"), "high", "high",
                 "Workflow meminta seluruh permission token ditulis; terapkan least privilege."),
                ("pull-request-target", re.compile(r"(?m)^\s*pull_request_target\s*:"), "high", "medium",
                 "Workflow memakai pull_request_target; tinjau checkout/eksekusi kode kontribusi tak tepercaya."),
                ("mutable-action-ref", re.compile(r"\buses:\s*[^\s#]+@(main|master|latest)\b"), "medium", "high",
                 "Action pihak ketiga dirujuk ke tag/branch mutable, bukan commit SHA."),
            ]
            for rule, pattern, severity, confidence, summary in workflow_rules:
                if pattern.search(line):
                    findings.append(_finding("security-workflow", rule, rel, number, severity, confidence, summary,
                        "Pola workflow terdeteksi; bukan bukti kompromi.",
                        "Tinjau kebutuhan permission, pin action ke full commit SHA tepercaya, dan jangan menjalankan kode PR tak tepercaya dengan secret/write token."))

    if rel.startswith(".github/workflows/"):
        # Whole-document fallback for the workflow-wide permission key.
        permission_match = re.search(
            r"(?im)^[ \t]*permissions[ \t]*:[ \t]*write-all(?:[ \t]+#.*)?[ \t]*$",
            text,
        )
        if permission_match and not any(
            item["detector_id"] == "security-workflow"
            and item["rule_id"] == "write-all-permissions"
            and item["path"] == rel
            for item in findings
        ):
            line = text.count("\n", 0, permission_match.start()) + 1
            findings.append(_finding("security-workflow", "write-all-permissions", rel, line, "high", "high",
                "Workflow meminta seluruh permission token ditulis; terapkan least privilege.",
                "Whole-document fallback matched permissions: write-all; no workflow execution performed.",
                "Tinjau kebutuhan permission dan terapkan least privilege; jangan memberi write token ke kode kontribusi tak tepercaya."))

    if suffix == ".py":
        _scan_python_security(rel, text, findings)
    elif suffix in JAVASCRIPT_SUFFIXES:
        _scan_javascript_security(rel, text, findings)

    if _is_agent_instruction_surface(rel):
        override = PROMPT_OVERRIDE.search(text)
        exfil = PROMPT_SECRET_ACTION.search(text)
        if override and exfil:
            line = text.count("\n", 0, override.start()) + 1
            findings.append(_finding("security-prompt-injection", "agent-instruction-secret-exfiltration", rel, line,
                "high", "medium",
                "Berkas instruksi agen menggabungkan upaya override instruksi dengan perintah membuka atau mengirim rahasia.",
                "Matched only the co-occurrence of instruction-override and secret-action indicators; matched text omitted.",
                "Perlakukan isi sebagai data tak tepercaya; hapus instruksi berbahaya dan jangan berikan akses secret/tool sebelum ditinjau."))

    if rel.startswith(".github/workflows/"):
        for match in re.finditer(r"(?m)^\s*(?:-\s*)?uses:\s*([^\s#]+)@([^\s#]+)", text):
            action, ref = match.group(1), match.group(2)
            if action.startswith("./") or re.fullmatch(r"[0-9a-fA-F]{40}", ref):
                continue
            if ref.lower() in {"main", "master", "latest"}:
                continue
            line = text.count("\n", 0, match.start()) + 1
            findings.append(_finding("security-supply-chain", "action-not-pinned-to-commit", rel, line,
                "medium", "high",
                "GitHub Action memakai tag/ref mutable alih-alih full commit SHA immutable.",
                f"action={action}; ref={ref}; immutable_commit_pin=false",
                "Verifikasi repository dan provenance upstream, lalu pin ke full commit SHA tepercaya; lakukan update pin secara terkontrol."))

    if suffix in {".toml", ".txt", ".json", ".yml", ".yaml", ".sh", ".ps1"}:
        for match in re.finditer(r"""(?i)(?:git\+https?://[^\s'"#]+@|github:[^\s'"#]+#)(main|master|develop|latest)\b""", text):
            line = text.count("\n", 0, match.start()) + 1
            findings.append(_finding("security-supply-chain", "mutable-git-dependency-ref", rel, line,
                "medium", "medium",
                "Dependency Git menunjuk ke nama branch mutable, bukan revisi immutable.",
                "dependency_source=git; ref_is_mutable=true",
                "Pin dependency ke commit penuh dan verifikasi checksum/provenance melalui mekanisme package yang didukung."))

    if suffix in {".sh", ".ps1"}:
        remote_exec = re.search(
            r"(?is)(?:curl|wget|Invoke-WebRequest|iwr)\b.{0,300}(?:\|\s*(?:ba)?sh\b|\|\s*iex\b|Invoke-Expression)",
            text,
        )
        if remote_exec:
            line = text.count("\n", 0, remote_exec.start()) + 1
            findings.append(_finding("security-code", "download-and-execute", rel, line, "high", "medium",
                "Skrip menggabungkan pengunduhan konten jaringan dan eksekusi shell langsung.",
                "Matched download-to-interpreter pattern; URL/payload omitted.",
                "Jangan eksekusi konten jaringan secara langsung; verifikasi sumber, digest, tanda tangan, dan review payload sebelum penggunaan."))
def _scan_json(rel, text, findings, actual_sha=None):
    try: parsed = json.loads(text)
    except json.JSONDecodeError as exc:
        findings.append(_finding("syntax", "invalid-json", rel, exc.lineno, "high", "high",
            "Berkas JSON tidak dapat diparse.", exc.msg, "Perbaiki sintaks JSON lalu jalankan pemindai kembali."))
        return
    if isinstance(parsed, dict):
        if parsed.get("collector") == "tools/collect_ci_health.py":
            if parsed.get("schema_version") != "one-ci-health-evidence/2":
                findings.append(_finding("ci-evidence", "unsupported-ci-collector-schema", rel, None, "high", "high",
                    "Skema bukti CI tidak sesuai dengan kontrak collector yang berlaku.",
                    f"schema_version={parsed.get('schema_version')!r}",
                    "Jalankan ulang collector versi yang cocok; jangan gunakan metadata dari skema lama sebagai bukti current-SHA.",
                    status="blocked"))
            if parsed.get("working_tree_clean") is not True:
                findings.append(_finding("ci-evidence", "ci-evidence-worktree-not-clean", rel, None, "high", "high",
                    "Bukti CI dibuat dari working tree yang tidak terbukti bersih.",
                    f"working_tree_clean={parsed.get('working_tree_clean')!r}",
                    "Ulangi koleksi dari checkout exact-SHA yang bersih; bukti dari working tree kotor tidak dapat dipakai untuk klaim source.",
                    status="blocked"))
            source_sha = parsed.get("source_sha")
            checked_sha = parsed.get("checked_out_sha")
            if actual_sha and isinstance(source_sha, str) and source_sha.lower() != actual_sha.lower():
                findings.append(_finding("ci-evidence", "ci-evidence-source-sha-not-current", rel, None, "critical", "high",
                    "Metadata CI berasal dari SHA berbeda dari checkout yang sedang dipindai.",
                    f"source_sha={source_sha}; actual_sha={actual_sha}",
                    "Kumpulkan ulang metadata Actions pada SHA checkout saat ini.",
                    status="blocked"))
            if actual_sha and isinstance(checked_sha, str) and checked_sha.lower() != actual_sha.lower():
                findings.append(_finding("ci-evidence", "ci-evidence-checkout-sha-not-current", rel, None, "critical", "high",
                    "Checkout SHA pada metadata CI berbeda dari repository yang sedang dipindai.",
                    f"checked_out_sha={checked_sha}; actual_sha={actual_sha}",
                    "Kumpulkan ulang metadata CI dari checkout exact-SHA saat ini.",
                    status="blocked"))
            if not isinstance(parsed.get("runs"), list):
                findings.append(_finding("ci-evidence", "ci-evidence-run-list-malformed", rel, None, "high", "high",
                    "Metadata CI tidak memiliki daftar workflow run yang valid.",
                    f"runs_type={type(parsed.get('runs')).__name__}",
                    "Periksa collector output dan jalankan ulang pengumpulan metadata.",
                    status="blocked"))
        collector_status = parsed.get("collector_status")
        if collector_status in {"blocked", "partial"}:
            errors = parsed.get("collection_errors", [])
            findings.append(_finding("ci-evidence", f"live-ci-metadata-{collector_status}", rel, None, "info", "high",
                "Metadata CI langsung tidak lengkap; status ini bukan bukti kegagalan source.",
                f"collector_status={collector_status}; errors={errors!r}",
                "Periksa izin Actions API, token read-only, rate limit, dan log collector; pertahankan status bukti sebagai blocked/partial.",
                status="blocked"))
        source_sha = parsed.get("source_sha") or parsed.get("candidate_sha")
        checked_sha = parsed.get("checked_out_sha") or parsed.get("checkout_sha")
        if isinstance(source_sha, str) and isinstance(checked_sha, str) and source_sha != checked_sha:
            findings.append(_finding("evidence-freshness", "source-checkout-sha-mismatch", rel, None, "high", "high",
                "SHA sumber bukti berbeda dari SHA yang benar-benar diperiksa.",
                f"source_sha={source_sha}; checked_out_sha={checked_sha}",
                "Tandai bukti sebagai tidak cocok dan jalankan ulang pemeriksaan pada SHA yang dimaksud."))
        artifacts = parsed.get("artifacts")
        if isinstance(artifacts, list):
            seen_artifacts = {}
            for artifact in artifacts:
                if not isinstance(artifact, dict):
                    continue
                name = str(artifact.get("name") or "unnamed-artifact")
                run_id = str(artifact.get("run_id") or "unknown-run")
                artifact_key = (run_id, name)
                if artifact_key in seen_artifacts:
                    findings.append(_finding("artifact-integrity", "duplicate-artifact-name", rel, None, "medium", "medium",
                        "Nama artefak berulang pada run Actions yang sama.", f"run_id={run_id}; name={name!r}",
                        "Tinjau apakah upload artifact saling menimpa atau nama perlu dibuat unik."))
                seen_artifacts[artifact_key] = True
                if artifact.get("expired") is True:
                    findings.append(_finding("artifact-integrity", "expired-ci-artifact", rel, None, "medium", "high",
                        "Artefak CI sudah kedaluwarsa dan mungkin tidak dapat diunduh.", f"run_id={run_id}; name={name!r}; created_at={artifact.get('created_at')!r}",
                        "Jalankan ulang workflow yang menghasilkan bukti atau unggah ulang artefak dengan retensi yang sesuai."))
                if not artifact.get("digest"):
                    findings.append(_finding("artifact-integrity", "artifact-digest-unavailable", rel, None, "info", "medium",
                        "Metadata artefak tidak menyediakan digest untuk pemeriksaan integritas independen.",
                        f"run_id={run_id}; name={name!r}",
                        "Jika API/retensi mendukungnya, simpan digest dan verifikasi isi artefak terunduh; keberadaan artefak saja bukan bukti integritas."))
        correlations = parsed.get("correlations")
        if isinstance(correlations, list):
            for correlation in correlations:
                if not isinstance(correlation, dict):
                    continue
                rule = correlation.get("rule_id")
                if rule == "failed-run-without-job-metadata":
                    findings.append(_finding("ci-evidence", rule, rel, None, "medium", "high",
                        "Run Actions gagal tanpa metadata job yang dapat ditinjau; penyebab belum diketahui.",
                        f"run_id={correlation.get('run_id')!r}; evidence={correlation.get('evidence')!r}",
                        str(correlation.get("next_step") or "Periksa detail run dan ketersediaan runner; jangan menyimpulkan source test gagal."),
                        status="blocked"))
                elif rule == "no-exact-sha-runs":
                    findings.append(_finding("ci-evidence", rule, rel, None, "info", "high",
                        "Tidak ada run GitHub Actions yang cocok dengan head_sha exact; metadata kosong bukan bukti PASS.",
                        f"source_sha={parsed.get('source_sha')!r}; collector_status={parsed.get('collector_status')!r}",
                        str(correlation.get("next_step") or "Jalankan workflow yang diwajibkan pada exact SHA atau gunakan bukti verifikasi independen."),
                        status="blocked"))
                elif rule == "billing-spending-limit-blocked":
                    findings.append(_finding("ci-evidence", rule, rel, None, "info", "high",
                        "Workflow diblokir oleh billing atau spending limit GitHub Actions; ini bukan kegagalan source code.",
                        f"check_run_id={correlation.get('check_run_id')!r}; check_run={correlation.get('check_run_name')!r}; classification=billing-blocked",
                        str(correlation.get("next_step") or "Periksa status billing/spending limit GitHub Actions dan ulangi pemeriksaan setelah akses dipulihkan."),
                        status="blocked"))
                elif rule == "no-artifacts-observed":
                    findings.append(_finding("artifact-integrity", rule, rel, None, "info", "medium",
                        "Tidak ada artefak yang teramati pada run Actions yang selesai.",
                        f"run_id={correlation.get('run_id')!r}; evidence={correlation.get('evidence')!r}",
                        str(correlation.get("next_step") or "Bandingkan dengan kontrak artefak workflow; ketiadaan saja bukan kegagalan."),
                        status="triaged"))
        jobs = parsed.get("jobs")
        if isinstance(jobs, list):
            for job in jobs:
                if not isinstance(job, dict) or job.get("conclusion") != "failure":
                    continue
                steps = job.get("steps")
                name = str(job.get("name") or job.get("id") or "unknown-job")
                if not isinstance(steps, list) or not steps:
                    findings.append(_finding("ci-evidence", "failed-job-without-visible-steps", rel, None, "medium", "high",
                        "Job CI gagal tetapi metadata tidak menunjukkan langkah yang dijalankan; penyebab belum diketahui.",
                        f"job={name}; conclusion=failure; steps={steps!r}; runner_id={job.get('runner_id')!r}; job_url={job.get('job_url')!r}",
                        "Ambil logs/annotations atau minta admin memeriksa runner; jangan menyimpulkan source test gagal tanpa output perintah.",
                        status="blocked"))
                    continue
                failed_steps = [step for step in steps if isinstance(step, dict) and step.get("conclusion") == "failure"]
                if failed_steps:
                    step_names = [str(step.get("name") or step.get("number") or "unnamed-step") for step in failed_steps]
                    findings.append(_finding("ci-evidence", "failed-step-needs-log-review", rel, None, "medium", "high",
                        "Job memiliki langkah gagal; akar masalah belum dapat dipastikan dari metadata saja.",
                        f"job={name}; failed_steps={step_names!r}",
                        "Baca log langkah yang gagal sebelum mengklasifikasikan penyebab atau menyetujui perbaikan.",
                        status="triaged"))

def _scan_workflows(root, workflows, findings):
    names = {}
    command_owners = {}
    for rel, text in workflows:
        for line in text.splitlines():
            command_match = re.match(r"^\s*(?:-\s*)?run:\s*(\S.*)$", line)
            if command_match:
                command = command_match.group(1).strip()
                if command not in {"|", ">", "|-", ">-"} and not command.startswith("#"):
                    command_owners.setdefault(command, []).append(rel)
        match = re.search(r"(?m)^name:\s*(.+?)\s*$", text)
        if match:
            name = match.group(1).strip().strip("'\"")
            if name in names:
                findings.append(_finding("workflow-integrity", "duplicate-workflow-name", rel, 1, "low", "medium",
                    "Dua workflow memakai nama yang sama.", f"{name!r} juga digunakan oleh {names[name]}.",
                    "Gunakan nama yang membedakan tujuan workflow agar bukti CI mudah ditelusuri."))
            else: names[name] = rel
        for number, line in enumerate(text.splitlines(), 1):
            local = re.search(r"\buses:\s*[\"']?(\./[^\"'\s]+)", line)
            if local and not (root / local.group(1)).exists():
                findings.append(_finding("workflow-integrity", "missing-local-action", rel, number, "high", "high",
                    "Workflow merujuk ke local action yang tidak ditemukan.", local.group(1),
                    "Pulihkan action yang hilang atau perbaiki path workflow."))
            command = re.search(r"\b(?:python(?:3)?|bash|sh)\s+((?:tools|scripts)/[A-Za-z0-9_./-]+\.(?:py|sh))", line)
            if command and not (root / command.group(1)).is_file():
                findings.append(_finding("workflow-integrity", "missing-command-file", rel, number, "high", "high",
                    "Workflow menjalankan berkas skrip yang tidak ditemukan.", command.group(1),
                    "Sinkronkan path workflow dengan skrip yang benar-benar ada."))
    for command, owners in command_owners.items():
        distinct = sorted(set(owners))
        if len(distinct) > 1:
            command_key = hashlib.sha256(command.encode("utf-8")).hexdigest()[:8]
            for rel in distinct:
                findings.append(_finding("workflow-overlap", f"repeated-run-command-{command_key}", rel, None, "info", "low",
                    "Perintah identik muncul di beberapa workflow; periksa apakah cakupannya sengaja tumpang tindih.",
                    f"command={command!r}; workflows={distinct!r}",
                    "Pertahankan jika tujuan/lingkungan pengujiannya berbeda; jika redundan, konsolidasikan tanpa mengurangi cakupan."))

def _trusted_cli_binary_reason(root: Path, binary: Path) -> str | None:
    try:
        relative = binary.relative_to(root)
        cursor = root
        for part in relative.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                return f"binary path contains a symlink component: {cursor}"
        metadata = binary.lstat()
        if not stat.S_ISREG(metadata.st_mode):
            return "CLI binary is not a regular file"
        if metadata.st_nlink != 1:
            return f"CLI binary has {metadata.st_nlink} hard links; exactly one is required"
        binary.resolve(strict=True).relative_to(root.resolve(strict=True))
    except (OSError, ValueError) as error:
        return f"CLI binary is not confined to the repository: {error}"
    return None


def _check_one_source(root: Path, findings: list[dict]) -> str:
    """Invoke the trusted CLI parser on normative fixtures; never execute fixture programs."""
    candidates = [root / "target" / "debug" / "one", root / "target" / "debug" / "one.exe"]
    binary = next((path for path in candidates if path.exists() or path.is_symlink()), None)
    if binary is None:
        findings.append(_finding("one-source-contract", "one-cli-unavailable", ".", None, "info", "high",
            "Pemeriksaan grammar One belum berjalan karena binary CLI tidak ditemukan.",
            "target/debug/one dan target/debug/one.exe tidak ada.",
            "Bangun CLI dengan cargo build --locked -p one-cli lalu jalankan pemindai dengan --check-one-source.",
            status="blocked"))
        return "blocked"
    untrusted_reason = _trusted_cli_binary_reason(root, binary)
    if untrusted_reason is not None:
        findings.append(_finding("one-source-contract", "one-cli-binary-not-confined", ".", None, "high", "high",
            "Pemeriksaan grammar One diblokir karena binary CLI tidak memenuhi batas file tepercaya.",
            untrusted_reason,
            "Bangun binary CLI dari checkout exact-SHA ini; jangan jalankan binary symlink, hard-link, atau di luar root.",
            status="blocked"))
        return "blocked"
    fixtures = []
    valid_dir = root / "tests" / "conformance" / "valid"
    invalid_dir = root / "tests" / "conformance" / "invalid"
    if valid_dir.is_dir(): fixtures.extend((path, True) for path in sorted(valid_dir.glob("*.one")))
    if invalid_dir.is_dir(): fixtures.extend((path, False) for path in sorted(invalid_dir.glob("*.one")))
    grammar_examples = root / "tests" / "spec" / "grammar_examples.one"
    if grammar_examples.is_file(): fixtures.append((grammar_examples, True))
    if not fixtures:
        findings.append(_finding("one-source-contract", "no-normative-fixtures-found", ".", None, "info", "high",
            "Pemeriksaan grammar One diblokir karena tidak ada fixture v0.1 yang ditemukan.",
            "Direktori conformance valid/invalid dan tests/spec/grammar_examples.one tidak tersedia.",
            "Pulihkan fixture normatif; jangan menganggap pemindaian tanpa fixture sebagai PASS.",
            status="blocked"))
        return "blocked"
    complete = True
    for path, should_pass in fixtures:
        rel = path.relative_to(root).as_posix()
        try:
            result = subprocess.run([str(binary), "periksa", path.relative_to(root).as_posix()], cwd=root, capture_output=True,
                                    text=True, timeout=30, check=False)
        except subprocess.TimeoutExpired:
            findings.append(_finding("one-source-contract", "one-source-check-timeout", rel, None, "high", "high",
                "Pemeriksaan source One melewati batas waktu.", "one periksa tidak selesai dalam 30 detik.",
                "Reproduksi pada fixture tersebut dan periksa regresi parser/CLI."))
            complete = False
            continue
        except OSError as exc:
            findings.append(_finding("one-source-contract", "one-source-check-unavailable", rel, None, "high", "high",
                "CLI One tidak dapat dijalankan untuk memeriksa source.", str(exc),
                "Periksa hasil build dan izin eksekusi binary."))
            complete = False
            continue
        passed = result.returncode == 0
        if passed != should_pass:
            expected = "accepted" if should_pass else "rejected"
            actual = "accepted" if passed else "rejected"
            detail = (result.stderr or result.stdout or "CLI tidak menghasilkan diagnostic text").strip()[:1000]
            findings.append(_finding("one-source-contract", "fixture-acceptance-mismatch", rel, None, "high", "high",
                "Hasil parser berbeda dari status fixture conformance.", f"expected={expected}; actual={actual}; {detail}",
                "Tinjau grammar normatif dan implementasi parser; jangan ubah status fixture tanpa alasan kontraktual."))
    return "ran" if complete else "partial"

def _scan_contract_documents(root: Path, findings: list[dict]) -> None:
    """Check high-value normative invariants without rewriting or executing One source."""
    contracts = {
        "docs/spec/one-v0.1-grammar.md": [
            ("no-generic-action-production", "There is **no generic action production**", "high"),
            ("ambiguous-parse-rejection", "parsing fails with `EAMBxxx`", "high"),
        ],
        "docs/spec/one-v0.1-cli-contract.md": [
            ("bounded-cli-recognition", "Command recognition is exact and bounded.", "medium"),
            ("explicit-capability-grant", "the capability must be explicitly granted", "high"),
            ("package-artifact-contract", "`.onepkg`", "medium"),
            ("ir-artifact-contract", "`.oneir`", "medium"),
        ],
        "docs/spec/one-v0.1-diagnostics.md": [
            ("stable-diagnostic-identity", "stable error code, severity, human-readable message, and source span", "high"),
            ("deterministic-diagnostics", "Diagnostics must be deterministic", "medium"),
            ("ambiguous-source-rejected", "reject the source instead of selecting an interpretation", "high"),
        ],
        "docs/spec/one-v0.1-package-build.md": [
            ("deterministic-ir-package", "`.oneir`", "medium"),
            ("deterministic-package-artifact", "`.onepkg`", "medium"),
            ("no-implicit-dependency-resolution", "no external dependency graph or package registry", "medium"),
        ],
        "docs/spec/one-v0.1-platform-abstraction.md": [
            ("adapter-cannot-expand-capability", "An adapter must not expand a capability", "high"),
        ],
    }
    for relative, requirements in contracts.items():
        path = root / relative
        if not path.is_file():
            findings.append(_finding("contract-drift", "normative-contract-missing", relative, None, "high", "high",
                "Dokumen kontrak normatif yang dibutuhkan pemeriksa tidak ditemukan.", relative,
                "Pulihkan dokumen kontrak; jangan menganggap pemeriksaan kontrak yang tidak berjalan sebagai PASS.", status="blocked"))
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            findings.append(_finding("contract-drift", "normative-contract-unreadable", relative, None, "high", "high",
                "Dokumen kontrak normatif tidak dapat dibaca.", repr(exc),
                "Periksa encoding dan izin file; status kontrak tetap blocked.", status="blocked"))
            continue
        for rule, required, severity in requirements:
            if required not in text:
                findings.append(_finding("contract-drift", rule, relative, None, severity, "medium",
                    "Invarian penting kontrak One tidak ditemukan pada dokumen normatif.",
                    f"required_text={required!r}",
                    "Tinjau perubahan dokumen terhadap kontrak normatif dan implementasi; jangan menambahkan frasa hanya untuk membuat pemindai hijau."))
def scan_repository(root: Path, expected_sha: str | None = None, check_one_source: bool = False) -> dict:
    root = root.resolve()
    findings, workflows = [], []
    files = list(_files(root))
    json_evidence_detectors = set()
    python_syntax_failed = False
    actual_sha, branch = _git(root, "rev-parse", "HEAD"), _git(root, "branch", "--show-current")
    if expected_sha is not None:
        if not SHA_RE.fullmatch(expected_sha):
            findings.append(_finding("revision-integrity", "invalid-expected-sha", ".", None, "high", "high",
                "SHA pembanding tidak berbentuk 40 karakter heksadesimal.", expected_sha, "Berikan SHA commit Git yang lengkap."))
        elif actual_sha is None:
            findings.append(_finding("revision-integrity", "git-head-unavailable", ".", None, "high", "high",
                "SHA HEAD tidak dapat dibaca; kesesuaian revisi tidak dapat dibuktikan.",
                "Perintah git rev-parse HEAD gagal atau root bukan checkout Git.", "Jalankan pemindai di checkout Git yang valid."))
        elif actual_sha.lower() != expected_sha.lower():
            findings.append(_finding("revision-integrity", "checkout-sha-mismatch", ".", None, "critical", "high",
                "Checkout Git tidak sama dengan SHA yang diwajibkan.", f"expected={expected_sha}; actual={actual_sha}",
                "Periksa checkout dan ulangi semua bukti pada SHA yang tepat."))
    docs_root = root / "docs" / "panduan-pengguna"
    _scan_contract_documents(root, findings)
    for path, rel in files:
        suffix = path.suffix.lower()
        if path.is_symlink():
            try: path.resolve().relative_to(root)
            except ValueError:
                findings.append(_finding("path-integrity", "symlink-escapes-repository", rel, None, "high", "high",
                    "Symlink mengarah keluar dari root repositori.", str(path.readlink()), "Tinjau symlink; jangan ikuti target di luar repositori."))
            continue
        if suffix not in TEXT_SUFFIXES: continue
        try:
            # Decode bytes explicitly and strictly so invalid UTF-8 cannot be normalized by a wrapper.
            text = path.read_bytes().decode("utf-8", errors="strict")
        except (OSError, UnicodeError) as exc:
            findings.append(_finding("file-integrity", "unreadable-text-file", rel, None, "medium", "high",
                "Berkas teks tidak dapat dibaca sebagai UTF-8.", str(exc), "Periksa encoding, izin, atau apakah berkas seharusnya berupa teks."))
            continue
        _scan_security(rel, text, findings)
        if suffix == ".py":
            try: ast.parse(text, filename=rel)
            except SyntaxError as exc:
                python_syntax_failed = True
                findings.append(_finding("syntax", "invalid-python", rel, exc.lineno, "high", "high",
                    "Berkas Python memiliki kesalahan sintaks.", exc.msg, "Perbaiki sintaks dan tambahkan tes regresi bila perlu."))
        elif suffix == ".toml":
            try:
                import tomllib
                tomllib.loads(text)
            except ImportError:
                findings.append(_finding("syntax", "toml-parser-unavailable", rel, None, "info", "low",
                    "Runtime Python tidak menyediakan tomllib; TOML belum diperiksa.", "Python 3.11+ diperlukan untuk parser TOML bawaan.",
                    "Jalankan pada Python 3.11 atau lebih baru.", status="blocked"))
            except Exception as exc:
                findings.append(_finding("syntax", "invalid-toml", rel, getattr(exc, "lineno", None), "high", "high",
                    "Berkas TOML tidak dapat diparse.", str(exc), "Perbaiki sintaks TOML dan validasi ulang."))
        elif suffix == ".json":
            _scan_json(rel, text, findings)
            try:
                parsed_json = json.loads(text)
            except json.JSONDecodeError:
                parsed_json = None
            if isinstance(parsed_json, dict):
                if (parsed_json.get("source_sha") or parsed_json.get("candidate_sha")) and (parsed_json.get("checked_out_sha") or parsed_json.get("checkout_sha")):
                    json_evidence_detectors.add("evidence-freshness")
                if isinstance(parsed_json.get("jobs"), list) or "collector_status" in parsed_json:
                    json_evidence_detectors.add("ci-evidence")
                if isinstance(parsed_json.get("artifacts"), list):
                    json_evidence_detectors.add("artifact-integrity")
        elif suffix == ".md": _scan_markdown(path, rel, root, text, findings)
        if rel.startswith(".github/workflows/") and suffix in {".yml", ".yaml"}: workflows.append((rel, text))
    _scan_workflows(root, workflows, findings)
    one_source_status = "not-requested"
    if check_one_source:
        one_source_status = _check_one_source(root, findings)
    cli_contract = root / "docs/spec/one-v0.1-cli-contract.md"
    cli_guide = root / "docs/panduan-pengguna/perintah-cli.md"
    if cli_contract.is_file() and cli_guide.is_file():
        guide = cli_guide.read_text(encoding="utf-8")
        for command in CORE_COMMANDS:
            if command not in guide:
                findings.append(_finding("contract-drift", "missing-core-cli-command", "docs/panduan-pengguna/perintah-cli.md",
                    None, "medium", "high", "Panduan CLI tidak mencantumkan perintah inti yang ada di kontrak.",
                    command, "Perbarui panduan berdasarkan kontrak CLI dan bukti implementasi."))
    occurrences = {}
    unique = []
    for item in findings:
        base_id = item["finding_id"]
        occurrence = occurrences.get(base_id, 0) + 1
        occurrences[base_id] = occurrence
        if occurrence > 1:
            item = dict(item)
            item["finding_id"] = f"{base_id}-{occurrence}"
        unique.append(item)
    ordered = sorted(unique, key=lambda f: ({"critical": 0, "high": 1, "medium": 2, "low": 3, "info": 4}.get(f["severity"], 5),
                                                      f["path"], f["line"] or 0, f["finding_id"]))
    counts = {level: sum(1 for item in ordered if item["severity"] == level) for level in ("critical", "high", "medium", "low", "info")}
    findings_by_detector = {}
    for item in ordered:
        detector = item["detector_id"]
        findings_by_detector[detector] = findings_by_detector.get(detector, 0) + 1
    suffixes = {path.suffix.lower() for path, _ in files if not path.is_symlink()}
    agent_instruction_surfaces = any(_is_agent_instruction_surface(rel) for path, rel in files if not path.is_symlink())
    dependency_surfaces = bool(workflows or any(_is_dependency_surface(rel) for path, rel in files if not path.is_symlink()))
    detectors_run = ["path-integrity"]
    if expected_sha is not None:
        detectors_run.append("revision-integrity")
    if suffixes.intersection({".py", ".toml", ".json"}):
        detectors_run.append("syntax")
    if ".md" in suffixes:
        detectors_run.extend(["markdown-links", "markdown-structure"])
    if suffixes.intersection(TEXT_SUFFIXES):
        detectors_run.append("file-integrity")
    if workflows:
        detectors_run.extend(["workflow-integrity", "workflow-overlap"])
    detectors_run.extend(sorted(json_evidence_detectors))
    detectors_run.extend(["security-secrets", "security-code", "security-javascript", "security-workflow", "security-prompt-injection", "security-supply-chain"])
    detectors_run.append("contract-drift")
    if check_one_source:
        detectors_run.append("one-source-contract")
    detectors_run = sorted(set(detectors_run))
    detector_status = {
        "path-integrity": "ran",
        "security-secrets": "ran" if suffixes.intersection(TEXT_SUFFIXES) else "not-applicable-no-text-files",
        "security-code": ("partial-invalid-python-files" if python_syntax_failed else "ran") if ".py" in suffixes else "not-applicable-no-python-files",
        "security-javascript": "ran" if suffixes.intersection(JAVASCRIPT_SUFFIXES) else "not-applicable-no-javascript-typescript-files",
        "security-workflow": "ran" if workflows else "not-applicable-no-workflows",
        "security-prompt-injection": "ran" if agent_instruction_surfaces else "not-applicable-no-agent-instruction-surfaces",
        "security-supply-chain": "ran" if dependency_surfaces else "not-applicable-no-workflows-or-dependency-files",
        "revision-integrity": "ran" if expected_sha is not None else "not-requested",
        "syntax": "ran" if suffixes.intersection({".py", ".toml", ".json"}) else "not-applicable-no-parseable-files",
        "markdown-links": "ran" if ".md" in suffixes else "not-applicable-no-markdown",
        "markdown-structure": "ran" if ".md" in suffixes else "not-applicable-no-markdown",
        "file-integrity": "ran" if suffixes.intersection(TEXT_SUFFIXES) else "not-applicable-no-text-files",
        "workflow-integrity": "ran" if workflows else "not-applicable-no-workflows",
        "workflow-overlap": "ran" if workflows else "not-applicable-no-workflows",
        "ci-evidence": "ran" if "ci-evidence" in detectors_run else "not-applicable-no-ci-evidence",
        "artifact-integrity": "ran" if "artifact-integrity" in detectors_run else "not-applicable-no-artifact-evidence",
        "contract-drift": "ran",
        "one-source-contract": one_source_status,
    }
    detector_coverage = {
        "status_by_detector": detector_status,
        "ran_count": sum(1 for status in detector_status.values() if status == "ran"),
        "not_applicable_count": sum(1 for status in detector_status.values() if status.startswith("not-applicable")),
        "not_requested_count": sum(1 for status in detector_status.values() if status == "not-requested"),
        "finding_counts_by_detector": findings_by_detector,
    }
    return {"schema_version": SCHEMA_VERSION, "scanner_version": "0.2.0", "repository": root.name,
            "head_sha": actual_sha, "branch": branch, "expected_sha": expected_sha,
            "environment": {"python": platform.python_version(), "implementation": platform.python_implementation(),
                "platform": platform.system(), "platform_release": platform.release()},
            "working_tree": {"state": "clean" if _git(root, "status", "--porcelain") == "" else "dirty_or_unavailable"},
            "finding_count": len(ordered), "severity_counts": counts, "findings": ordered,
            "detectors_run": detectors_run, "detector_coverage": detector_coverage,
            "limitations": ["YAML workflow files receive targeted structural/reference checks, not full YAML schema validation.",
                "The scanner is read-only unless the separately guarded safe-fix option is explicitly requested.",
                "A finding is a lead for review; no inference is promoted to a root cause without supporting evidence."]}

def _validate_baseline(baseline: object) -> dict:
    """Reject malformed or ambiguous baselines before they influence triage."""
    if not isinstance(baseline, dict) or baseline.get("schema_version") != SCHEMA_VERSION:
        raise ValueError("unsupported baseline schema")
    findings = baseline.get("findings")
    if not isinstance(findings, list):
        raise ValueError("baseline findings must be an array")
    seen_ids = set()
    for index, item in enumerate(findings):
        if not isinstance(item, dict):
            raise ValueError(f"baseline findings[{index}] must be an object")
        finding_id = item.get("finding_id")
        detector_id = item.get("detector_id")
        if not isinstance(finding_id, str) or not finding_id.strip():
            raise ValueError(f"baseline findings[{index}].finding_id must be a non-empty string")
        if not isinstance(detector_id, str) or not detector_id.strip():
            raise ValueError(f"baseline findings[{index}].detector_id must be a non-empty string")
        if finding_id in seen_ids:
            raise ValueError(f"duplicate baseline finding_id: {finding_id}")
        seen_ids.add(finding_id)
    return baseline

def apply_baseline(report: dict, baseline: dict) -> dict:
    """Compare findings without changing the fixed-weight acceptance ledger."""
    baseline = _validate_baseline(baseline)
    previous = {item["finding_id"]: item for item in baseline["findings"]}
    current_ids = {item["finding_id"] for item in report["findings"]}
    counts = {"new": 0, "recurring": 0, "reopened": 0, "resolved": 0, "not_checked": 0}
    for item in report["findings"]:
        old = previous.get(item["finding_id"])
        if old is None:
            item["change_status"] = "new"
        elif old.get("status") == "resolved" or old.get("change_status") == "resolved":
            item["change_status"] = "reopened"
        else:
            item["change_status"] = "recurring"
        counts[item["change_status"]] += 1
        impact = {"critical": 5.0, "high": 4.0, "medium": 3.0, "low": 2.0, "info": 1.0}.get(item["severity"], 1.0)
        confidence = {"high": 1.0, "medium": 0.7, "low": 0.4}.get(item["confidence"], 0.4)
        recurrence = 1.5 if old is not None and item["change_status"] == "recurring" else 1.0
        blocker = 1.5 if item["detector_id"] in {"revision-integrity", "syntax"} else 1.0
        item["priority_score"] = round(impact * confidence * recurrence * blocker, 2)
        item["priority_inputs"] = {"impact": impact, "confidence": confidence, "recurrence_factor": recurrence,
                                   "acceptance_blocker_factor": blocker}
    resolved, not_checked = [], []
    current_detectors = set(report.get("detectors_run", []))
    coverage = report.get("detector_coverage", {})
    status_by_detector = coverage.get("status_by_detector", {}) if isinstance(coverage, dict) else {}
    for finding_id, old in previous.items():
        if finding_id in current_ids or old.get("status") == "resolved" or old.get("change_status") == "resolved":
            continue
        item = dict(old)
        detector_id = item.get("detector_id")
        detector_status = status_by_detector.get(detector_id)
        # detectors_run records the scanner's declared detector set, but some
        # entries are intentionally marked not-applicable when their input
        # surfaces do not exist. A missing finding can only be resolved when
        # the detector actually ran against applicable input.
        # Fail closed: only explicit positive coverage proves that the
        # detector actually ran against applicable input. Missing/old reports
        # must never turn an absent finding into an implicit resolution.
        detector_ran = detector_id in current_detectors and detector_status == "ran"
        if not detector_ran:
            item["status"] = "blocked"
            item["change_status"] = "not_checked"
            item["resolution_basis"] = "The current scan did not run this detector against applicable input; absence is not evidence of resolution."
            not_checked.append(item)
            counts["not_checked"] += 1
        else:
            item["status"] = "resolved"
            item["change_status"] = "resolved"
            item["resolution_basis"] = "Not reproduced by the current completed detector; review detector coverage and evidence before closure."
            resolved.append(item)
            counts["resolved"] += 1
    report["resolved_findings"] = sorted(resolved, key=lambda f: f.get("finding_id", ""))
    report["not_checked_findings"] = sorted(not_checked, key=lambda f: f.get("finding_id", ""))
    report["change_counts"] = counts
    report["active_finding_count"] = report["finding_count"]
    report["resolved_finding_count"] = len(resolved)
    report["baseline_schema_version"] = baseline.get("schema_version")
    return report

def render_markdown(report: dict) -> str:
    lines = ["# One Repository Health Report", "", f"- Schema: {report['schema_version']}",
        f"- Repository: {report['repository']}", f"- HEAD: {report['head_sha'] or 'UNKNOWN'}",
        f"- Branch: {report['branch'] or 'UNKNOWN'}", f"- Findings: **{report['finding_count']}**", "",
        "| Severity | Count |", "|---|---:|"]
    lines.extend(f"| {level} | {count} |" for level, count in report["severity_counts"].items())
    if report.get("change_counts"):
        lines.extend(["", "## Change history", "", "| Change | Count |", "|---|---:|"])
        lines.extend(f"| {name} | {count} |" for name, count in report["change_counts"].items())
    coverage = report.get("detector_coverage", {})
    if coverage:
        lines.extend(["", "## Detector coverage", "",
            f"- Detectors run: {coverage.get('ran_count', 0)}",
            f"- Not applicable (input absent): {coverage.get('not_applicable_count', 0)}",
            f"- Not requested: {coverage.get('not_requested_count', 0)}", "",
            "| Detector | Status | Findings |", "|---|---|---:|"])
        for detector, status in sorted(coverage.get("status_by_detector", {}).items()):
            count = coverage.get("finding_counts_by_detector", {}).get(detector, 0)
            lines.append(f"| {detector} | {status} | {count} |")
    lines.extend(["", "## Findings", ""])
    if not report["findings"]: lines.append("Tidak ditemukan anomali oleh pemeriksaan yang tersedia.")
    for item in report["findings"]:
        location = item["path"] + (f":{item['line']}" if item["line"] else "")
        lines.extend([f"### {item['finding_id']} — {item['summary']}", f"- Status: {item['status']}",
            f"- Change status: {item.get('change_status', 'uncompared')}",
            f"- Severity/confidence: {item['severity']} / {item['confidence']}",
            f"- Priority score: {item.get('priority_score', 'not calculated')}",
            f"- Lokasi: {location}", f"- Bukti: {item['evidence']}",
            f"- Tindak lanjut: {item['recommendation']}", ""])
    if report.get("resolved_findings"):
        lines.extend(["## Resolved since baseline (review before closure)", ""])
        lines.extend(f"- {item['finding_id']} — {item['summary']}: {item.get('resolution_basis', '')}" for item in report["resolved_findings"])
    if report.get("not_checked_findings"):
        lines.extend(["", "## Not checked in this run", ""])
        lines.extend(f"- {item['finding_id']} — {item['summary']}: {item.get('resolution_basis', '')}" for item in report["not_checked_findings"])
    lines.extend(["## Batas pemeriksaan", ""])
    lines.extend(f"- {item}" for item in report["limitations"])
    return "\n".join(lines) + "\n"

def _safe_fix_missing_markdown_newline(root: Path, report: dict, apply: bool,
                                      repair_paths: list[str] | None = None) -> list[str]:
    candidates = []
    requested = set()
    for raw in repair_paths or []:
        candidate = Path(raw)
        if candidate.is_absolute() or ".." in candidate.parts or candidate.as_posix().startswith("./"):
            raise RuntimeError(f"safe fix refused: repair path must be repository-relative and cannot traverse: {raw}")
        rel = candidate.as_posix()
        if candidate.suffix.lower() != ".md":
            raise RuntimeError(f"safe fix refused: only Markdown newline repair is allowlisted: {raw}")
        requested.add(rel)
    for path, rel in _files(root):
        if path.is_symlink() or path.suffix.lower() != ".md": continue
        if requested and rel not in requested: continue
        try: data = path.read_bytes()
        except OSError: continue
        if data and not data.endswith(b"\n"): candidates.append((path, rel))
    if not apply:
        preview = []
        for path, rel in candidates:
            before = path.read_text(encoding="utf-8").splitlines(keepends=True)
            after = before[:]
            if after:
                after[-1] = after[-1].rstrip("\r\n") + "\n"
            preview.append(f"PROPOSED: add final newline: {rel}")
            preview.extend(line.rstrip("\n") for line in difflib.unified_diff(
                before, after, fromfile=f"a/{rel}", tofile=f"b/{rel}"))
        return preview
    if not requested: raise RuntimeError("safe fix refused: specify each exact --repair-path to modify")
    existing = {rel for _, rel in candidates}
    missing = sorted(requested - existing)
    if missing: raise RuntimeError(f"safe fix refused: paths are absent, symlinks, not eligible, or already compliant: {missing}")
    branch = _git(root, "branch", "--show-current")
    dirty = _git(root, "status", "--porcelain")
    if not branch or not (branch.startswith("health/") or branch.startswith("diagnostic/")):
        raise RuntimeError("safe fix refused: branch must start with health/ or diagnostic/")
    if dirty: raise RuntimeError("safe fix refused: working tree must be clean before applying repairs")
    if report.get("expected_sha") and report.get("head_sha") != report["expected_sha"]:
        raise RuntimeError("safe fix refused: expected SHA does not match HEAD")
    changed = []
    for path, rel in candidates:
        path.write_bytes(path.read_bytes() + b"\n")
        changed.append(f"APPLIED: add final newline: {rel}")
    return changed

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--expected-sha", default=os.environ.get("GITHUB_SHA"))
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    parser.add_argument("--baseline", type=Path, help="compare findings with a previous JSON report")
    parser.add_argument("--check-one-source", action="store_true",
                        help="run one periksa on normative v0.1 conformance fixtures; never executes programs")
    parser.add_argument("--propose-safe-fixes", action="store_true")
    parser.add_argument("--apply-safe-fixes", action="store_true")
    parser.add_argument("--repair-path", action="append", default=[], help="exact repository-relative Markdown path to repair; repeat for multiple files")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)
    root = args.root.resolve()
    report = scan_repository(root, args.expected_sha, check_one_source=args.check_one_source)
    if args.baseline:
        try:
            baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            print(f"BASELINE UNAVAILABLE: {exc}", file=sys.stderr)
            return 2
        if not isinstance(baseline, dict) or baseline.get("schema_version") != SCHEMA_VERSION or not isinstance(baseline.get("findings"), list):
            print("BASELINE UNAVAILABLE: unsupported schema or missing findings list", file=sys.stderr)
            return 2
        report = apply_baseline(report, baseline)
    if args.propose_safe_fixes or args.apply_safe_fixes:
        try: proposals = _safe_fix_missing_markdown_newline(root, report, args.apply_safe_fixes, args.repair_path)
        except RuntimeError as exc:
            print(f"SAFE FIX REFUSED: {exc}", file=sys.stderr)
            return 2
        print("\n".join(proposals) if proposals else "No allowlisted Markdown newline repairs needed.")
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if args.markdown_out:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(render_markdown(report), encoding="utf-8")
    if not args.quiet: print(render_markdown(report))
    return 1 if any(f["severity"] in {"critical", "high"} for f in report["findings"]) else 0

if __name__ == "__main__":
    raise SystemExit(main())
