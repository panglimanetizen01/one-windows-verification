#!/usr/bin/env python3
"""Resolve the official Android API 35 default arm64-v8a image archive from SDK metadata."""

from __future__ import annotations

import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def child(node: ET.Element, name: str) -> ET.Element | None:
    return next((item for item in list(node) if local(item.tag) == name), None)


def value(node: ET.Element, name: str) -> str:
    item = child(node, name)
    return item.text.strip() if item is not None and item.text else ""


def revision_tuple(node: ET.Element) -> tuple[int, ...]:
    revision = child(node, "revision")
    if revision is None:
        return (0,)
    parts = [value(revision, key) for key in ("major", "minor", "micro", "preview")]
    return tuple(int(part) if part.isdigit() else 0 for part in parts)


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: resolve_android_api35_image.py REPOSITORY_XML OUTPUT_FILE")

    root = ET.parse(sys.argv[1]).getroot()
    target_path = "system-images;android-35;default;arm64-v8a"
    matches: list[tuple[tuple[int, ...], str, str, str]] = []

    # Current repository2-1.xml metadata uses remotePackage path attributes.
    for node in root.iter():
        if local(node.tag) != "remotePackage" or node.get("path") != target_path:
            continue
        archives = child(node, "archives")
        if archives is None:
            continue
        for archive in list(archives):
            complete = child(archive, "complete")
            if complete is None:
                continue
            url = value(complete, "url")
            checksum = child(complete, "checksum")
            if not url or checksum is None or not checksum.text:
                continue
            digest = checksum.text.strip()
            algorithm = checksum.get("type", "").lower()
            if not algorithm:
                algorithm = "sha1" if len(digest) == 40 else "sha256" if len(digest) == 64 else ""
            matches.append((revision_tuple(node), url, algorithm, digest))

    if not matches:
        raise SystemExit(
            "Official repository metadata has no Android API 35 default "
            "arm64-v8a system image archive with a digest"
        )

    _, url, algorithm, digest = max(matches)
    if algorithm not in ("sha1", "sha256") or not digest:
        raise SystemExit(f"Unsupported official system-image digest type: {algorithm!r}")

    full_url = (
        url
        if url.startswith("https://")
        else "https://dl.google.com/android/repository/" + url.lstrip("/")
    )
    Path(sys.argv[2]).write_text(
        f"{algorithm} {digest} {full_url}\n",
        encoding="utf-8",
    )
    print(f"Selected official API 35 arm64-v8a image: {full_url} ({algorithm})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
