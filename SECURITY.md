# Security policy

The repository has two trust models. The instruction kit in `rules/`, `references/`, `schemas/`, `templates/`, `llm/`, and `docs/` consists of documents and structured data. Reading those files locally executes no pipeline and transmits no patient data. Uploading them or patient documents to a service is a separate user action with that service's privacy implications.

The optional local-operations pipeline in `scripts/` is executable Python and is not required to use the instruction kit. Static inspection of all 17 Python files on 2026-09-07 found:

- `classify_rename_medical_bills.py` and `parse_spd.py` import both PyMuPDF (`fitz`) and the OpenAI client. They send rendered document-page images to the configured Azure OpenAI endpoint for bill classification or plan-document extraction.
- `index_bills_and_claims.py`, `draft_letters_by_state.py`, and `match_claims_to_bills.py` import the OpenAI client. Their cloud paths send bill/EOB text, drafting evidence and patient context, or claim and candidate-bill fields respectively. These fields can include identifiers, service dates and amounts. The destination is the configured `AZURE_OPENAI_ENDPOINT`, with `/openai/v1/` appended; matching can invoke the client as a fallback.
- `fetch_mrf.py` uses standard-library HTTP to download the supplied hospital price-file URL. `bundle_to_cloud.py` uses standard-library subprocess calls to invoke the external `rclone` program and copy bundles to the user's configured cloud remote. Standard-library imports do not mean a script is offline.
- `_kit_config.py`, `analyze_self_pay_election.py`, `audit_billing_errors.py`, `bundle_evidence.py`, `check_completeness.py`, `deadline_watch.py`, `fetch_price_benchmarks.py`, `log_interaction.py`, `restructure_to_billers_eob.py`, and `validate_tracker.py` have only standard-library or local-module imports. In particular, the tracker validator and deadline watcher require neither PyMuPDF nor the OpenAI client. Local processing can still read, change or package sensitive files.

The five OpenAI-client scripts read credentials from a local `.env` path, defaulting to `~/.medbill-dispute-kit/.env` and configurable through `MEDBILL_KIT_ENV_FILE`. They use the endpoint, API key and deployment configured there. Patient-document roots default to `~/Health_Bills`, with `HEALTHBILLS_ROOT` and script-specific options providing overrides. Generated documents, indexes and drafts can retain patient information locally; cloud requests transmit the selected content outside the machine. Review the actual inputs, endpoint and storage destination before running these optional paths. This policy does not assert that a configured endpoint or cloud remote has any particular contractual privacy protection.

## What's in scope

- All optional Python scripts and their local-processing, credential-loading, network-request and cloud-copy behavior in `scripts/`
- The GitHub Actions workflow in `.github/workflows/`
- Schema validators or any future code we add

## What's out of scope

- The content of any LLM session a user runs with the kit. The kit does not control how an LLM processes a user's bill, and the LLM is not part of this repository.
- Third-party services the kit refers users to (Dollar For, Turquoise Health, GoodRx, etc.).
- Privacy and security of the user's own data on their own machine.

## Reporting a vulnerability

If you discover a security issue, do **not** open a public issue. Email the maintainer at the address listed on the GitHub profile of [k3rt4s](https://github.com/k3rt4s), or, if that is unavailable, open a private security advisory at https://github.com/k3rt4s/medbill-dispute-kit/security/advisories/new.

Please include:

- The specific file, line, or behavior at issue
- Reproduction steps
- The impact you believe the vulnerability has
- Any mitigation suggestions

You will receive an acknowledgment within seven days. We will work in good faith toward a fix and coordinated disclosure.

## Patient-data security guidance

This is not a vulnerability report channel but worth saying. If a patient using the kit is concerned about a third-party service mishandling their data:

- For cloud LLM providers: review the provider's privacy policy and (if applicable) their HIPAA Business Associate Agreement options.
- For consumer-facing services we link to (Dollar For, Turquoise Health, etc.): contact those services directly.
- For state insurance department or attorney general complaint portals: those are official government channels with their own protections.

## Disclosure timeline

When the maintainer fixes a reported vulnerability:

1. Patch is committed.
2. CHANGELOG entry notes the change without disclosing the specific vector until the patch is broadly available.
3. After a reasonable embargo, a public security advisory is published describing the issue and the fix.
