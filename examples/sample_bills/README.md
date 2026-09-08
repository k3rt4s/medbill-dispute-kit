Synthetic medical bill and EOB fixtures for offline regression tests.

SYNTHETIC SAMPLE, NOT A REAL BILL. Generated for regression testing. All names, numbers and addresses are fictional.

The generators in this folder create six cases under
`C:/Code_data/medbill-dispute-kit/examples/sample_bills` by default. Generated
Markdown, JSON and text-layer PDFs stay outside the repository. Use `--output`
to select another directory outside a checkout.

Run the three `generate_cases_*.py` files with the interpreter recorded in the
Lane 0 integration note. Each produces two cases. Run `tests/test_sample_bills.py`
to regenerate isolated test copies and validate identifiers, field names,
document banners and the tracker CSV.

`expected.json` has a `bills` envelope containing records restricted to
`schemas/bill.toml`, and a `tracker_rows` envelope containing records restricted
to the tracker columns. This keeps tracker-only fields such as `has_eob` and
`has_itemization` out of the bill schema. Its top-level `notes` is the synthetic
banner; the envelopes are fixture metadata, not new bill or tracker fields.

To add a case, use clearly fictional names and zero or visibly sequential
identifiers, keep dates and amounts consistent across its documents, and include
the banner in every generated file. Add expected values using existing schema
names and an explicit test for the behavior the case exercises. These cases test
the stated scenarios; they do not establish extraction accuracy on real bills.
