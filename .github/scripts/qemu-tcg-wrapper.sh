#!/usr/bin/env bash
set -euo pipefail
real="$(dirname "$0")/qemu-system-aarch64-headless.real"
args=()
skip_next=0
for arg in "$@"; do
  if (( skip_next )); then
    skip_next=0
    continue
  fi
  if [[ "$arg" == "-enable-hvf" ]]; then
    continue
  fi
  if [[ "$arg" == "-accel" ]]; then
    skip_next=1
    continue
  fi
  if [[ "$arg" == -accel=hvf ]]; then
    args+=("-accel=tcg")
    continue
  fi
  if [[ "$arg" == *accel=hvf* ]]; then
    arg="${arg//accel=hvf/accel=tcg}"
  fi
  args+=("$arg")
done
printf 'QEMU TCG wrapper normalized HVF acceleration flags; remaining args: ' >&2
printf '%q ' "${args[@]}" >&2
printf '\n' >&2
exec "$real" "${args[@]}"
