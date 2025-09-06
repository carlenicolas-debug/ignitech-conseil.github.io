# Ignitech Conseil

## Anchor validation

This site includes a small check to ensure that internal links resolve to existing anchors in `index.html`.

Run the script locally:

```bash
python scripts/check_anchors.py
```

The script runs in CI via [`.github/workflows/anchor-check.yml`](.github/workflows/anchor-check.yml). It exits with a non-zero status and lists missing anchors such as `#contact`.
