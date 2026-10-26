#!/usr/bin/env python3
"""Resolve the official Android API 35 default arm64-v8a image archive from SDK metadata."""
# The workflow verifies the returned digest before extracting the image.
# This helper only selects an official API-level and ABI-matched package.

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


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: resolve_android_api35_image.py REPOSITORY_XML OUTPUT_FILE")

    root = ET.parse(sys.argv[1]).getroot()
    matches: list[tuple[tuple[int, ...], str, str, str]] = []
    for node in root.iter():
        if local(node.tag) != "system-image":
            continue
        if (
            value(node, "api-level"),
            value(node, "abi"),
            value(node, "tag-id"),
        ) != ("35", "arm64-v8a", "default"):
            continue

        revision_text = value(node, "revision")
        try:
            revision = tuple(int(part) for part in revision_text.split("."))
        except ValueError:
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
            if url and checksum is not None and checksum.text:
                matches.append(
                    (
                        revision,
                        url,
                        checksum.get("type", "").lower(),
                        checksum.text.strip(),
                    )
                )

    if not matches:
        raise SystemExit(
            "Official repository metadata has no Android API 35 default "
            "arm64-v8a system image with a digest"
        )

    _, url, algorithm, digest = max(matches)
    if algorithm not in ("sha1", "sha256") or not digest:
        raise SystemExit(f"Unsupported official system-image digest type: {algorithm!r}")

    full_url = (
        url
        if url.startswith("https://")
        else "https://dl.google.com/android/repository/sys-img/android/" + url
    )
    Path(sys.argv[2]).write_text(
        f"{algorithm} {digest} {full_url}\n",
        encoding="utf-8",
    )
    print(f"Selected official API 35 arm64-v8a image: {full_url} ({algorithm})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
