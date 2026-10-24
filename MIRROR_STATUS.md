Status: exact source selector aligned to the current ONE branch checkpoint; mirror execution still requires independent confirmation.
Canonical repository: panglimanetizen01/one
Canonical branch: milestone/100-ecosystem-20261023
Canonical commit: dab0a03e5d364150fd8a28a2c657af02bc19ee74

The selector CANONICAL_COMMIT.txt points to this exact SHA. Canonical Actions runs on this SHA:
- One CI: https://github.com/panglimanetizen01/one/actions/runs/40062436612
- Linux distribution conformance: https://github.com/panglimanetizen01/one/actions/runs/40062436625
- Standard-library focused verification: https://github.com/panglimanetizen01/one/actions/runs/40062436613

All three failed again on attempt 2 before recording any steps (jobs report empty step arrays; no usable test logs). This does not establish source tests as passing or failing. A selector update alone is not verification. The independent mirror must successfully fetch the private source via CANONICAL_READ_TOKEN and produce inspectable exact-SHA logs for Linux/Windows build, contract, Clippy, workspace, real-network, and offline checks before this snapshot is considered verified.
