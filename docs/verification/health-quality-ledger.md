# One Health Detector Quality Ledger

This ledger measures **reviewed evidence**, not guesses. It is separate from the One fixed-weight completion ledger and cannot approve a merge or production release.

## Generate a report

Start from the empty schema example:

~~~sh
cp docs/verification/health-quality-ledger.example.json /tmp/health-quality.json
python tools/health_quality.py /tmp/health-quality.json \
  --json-out /tmp/health-quality-report.json \
  --markdown-out /tmp/health-quality-report.md
python -m unittest discover -s tools -p "test_health_quality.py" -v
~~~

On Windows PowerShell, use a suitable temporary directory instead of /tmp.

## Record detector adjudications

Each reviewed finding must have a unique finding_id, detector_id, outcome, review date, and evidence note. Allowed outcomes:

- true_positive: finding reproduced and the detector correctly identified the condition.
- false_positive: finding was reviewed and the reported condition was not present.
- false_negative: a confirmed issue was missed by the detector; record a stable finding ID such as MISS-... and explain how it was found.
- not_reproducible: reviewers could not reproduce it; do not silently count this as true or false.
- pending: review has not finished.

Do not add adjudications without evidence. Do not record secrets, tokens, personal data, or private logs in this file.

## Record repair outcomes

Each repair attempt has a unique repair_id, linked finding_id, repair type, outcome, boolean verified, date, and evidence note. Allowed outcomes are success, failed, reverted, and pending. A repair counts as successful only when outcome is success and verified is true. Verification should name the tests or re-scan that checked the resulting exact commit.

## Interpretation

The report exposes:
- observed false-positive share among reviewed true/false detections;
- observed miss share among reviewed true positives and false negatives;
- counts by detector and adjudication outcome;
- verified terminal repair success rate and unverified terminal attempts.

These are sample metrics, **not statistically representative precision/recall guarantees**. Unreviewed findings and unknown outcomes are not counted as correct. Keep the evidence note concise and reproducible, and review the ledger changes in code review. The quality report never changes the fixed-weight acceptance ledger.
