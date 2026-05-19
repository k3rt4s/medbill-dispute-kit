# Security policy

The kit ships no executable code by default; it is a pack of Markdown, TOML, and CSV files. The optional helper script in `scripts/` uses the Python standard library only. The repository is therefore low-risk by design.

## What's in scope

- The optional Python helper scripts in `scripts/`
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
