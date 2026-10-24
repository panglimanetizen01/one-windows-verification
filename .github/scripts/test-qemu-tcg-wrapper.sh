#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/../.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp "$root/.github/scripts/qemu-tcg-wrapper.sh" "$tmp/qemu-system-aarch64-headless"
cat > "$tmp/qemu-system-aarch64-headless.real" <<'STUB'
#!/usr/bin/env bash
printf '%s\n' "$@"
STUB
chmod +x "$tmp/qemu-system-aarch64-headless" "$tmp/qemu-system-aarch64-headless.real"
actual="$("$tmp/qemu-system-aarch64-headless" -enable-hvf -accel hvf -machine virt,accel=hvf -accel=hvf -m 2048 -name test 2>/dev/null)"
expected="$(printf '%s\n' '-machine' 'virt,accel=tcg' '-accel=tcg' '-m' '2048' '-name' 'test')"
if [[ "$actual" != "$expected" ]]; then
  printf 'QEMU wrapper regression failed.\nExpected:\n%s\nActual:\n%s\n' "$expected" "$actual" >&2
  exit 1
fi
printf 'PASS: QEMU wrapper removes HVF flags and preserves TCG-compatible arguments.\n'
