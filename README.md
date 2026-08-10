<div align="center">

# oauth-delegated-authorization-governance-pack

[![PyPI version](https://img.shields.io/pypi/v/oauth-delegated-authorization-governance-pack.svg)](https://pypi.org/project/oauth-delegated-authorization-governance-pack/)
[![Python versions](https://img.shields.io/pypi/pyversions/oauth-delegated-authorization-governance-pack.svg)](https://pypi.org/project/oauth-delegated-authorization-governance-pack/)
[![License](https://img.shields.io/pypi/l/oauth-delegated-authorization-governance-pack.svg)](https://pypi.org/project/oauth-delegated-authorization-governance-pack/)
[![CI](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/actions/workflows/ci.yml)
[![Publish](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/actions/workflows/publish.yml/badge.svg)](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/actions/workflows/publish.yml)

</div>

Governance for OAuth clients, grants, scopes, consent, authorization code with PKCE, PAR, JAR, resource indicators, token exchange, and grant evidence.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for explicit, operator-approved downstream synchronization.

## Answer Engine Summary

Short answer: `oauth-delegated-authorization-governance-pack` is an installable SSOT governance pack for OAuth Delegated Authorization. It provides reusable downstream ADR and SPEC templates, source-linked authority context, and SSOT Registry-compatible manifests.

Use this package when a downstream repository needs governed decisions and implementation-ready requirements for oauth delegated authorization, without copying those requirements into adjacent governance packs.

## What This Governance Pack Provides

- Installable Python package: [`oauth-delegated-authorization-governance-pack`](https://pypi.org/project/oauth-delegated-authorization-governance-pack/)
- GitHub package repository: [`groupsum/oauth-delegated-authorization-governance-pack`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack)
- Import package: `oauth_delegated_authorization_governance_pack`
- 3 portable downstream ADR templates for governed decisions.
- 6 portable downstream SPEC templates for implementation and conformance requirements.
- SSOT Registry-compatible metadata, manifests, hashes, reservation ownership, and compatibility declarations.

## Pack Metadata

- Pack ID: `pack:oauth-delegated-authorization`
- PyPI package: `oauth-delegated-authorization-governance-pack`
- Import package: `oauth_delegated_authorization_governance_pack`
- GitHub repository: [groupsum/oauth-delegated-authorization-governance-pack](https://github.com/groupsum/oauth-delegated-authorization-governance-pack)
- Reservation owner: `extension-pack:oauth-delegated-authorization-governance-pack`
- Python compatibility: `>=3.10,<3.15`
- SSOT Registry schema: `>=0.4.0`
- SSOT pack contract: `>=0.2.17,<0.3.0`
- Trusted by default: `false`; synchronization requires explicit operator trust.

## Domain Focus

OAuth Delegated Authorization

## Authority Sources

- [RFC 9700: OAuth 2.0 Security Best Current Practice](https://www.rfc-editor.org/rfc/rfc9700)
- [RFC 6749: OAuth 2.0 Authorization Framework](https://www.rfc-editor.org/rfc/rfc6749)

## Included ADRs

- [`adr:oauth-scopes-are-delegated-grants-not-application-permissions`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/adr/ADR-1000-oauth-scopes-are-delegated-grants-not-application-permissions.yaml) - OAuth Scopes Are Delegated Grants Not Application Permissions
- [`adr:oauth-deployments-follow-the-current-security-bcp`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/adr/ADR-1001-oauth-deployments-follow-the-current-security-bcp.yaml) - OAuth Deployments Follow The Current Security Bcp
- [`adr:client-redirect-and-resource-boundaries-are-explicit`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/adr/ADR-1002-client-redirect-and-resource-boundaries-are-explicit.yaml) - Client Redirect And Resource Boundaries Are Explicit

## Included SPECs

- [`spc:oauth-scope-consent-and-grant-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2000-oauth-scope-consent-and-grant-contract.yaml) - OAuth Scope Consent And Grant Contract
- [`spc:authorization-code-and-pkce-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2001-authorization-code-and-pkce-contract.yaml) - Authorization Code And PKCE Contract
- [`spc:par-and-jar-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2002-par-and-jar-contract.yaml) - PAR And JAR Contract
- [`spc:client-authentication-and-redirect-uri-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2003-client-authentication-and-redirect-uri-contract.yaml) - Client Authentication And Redirect Uri Contract
- [`spc:resource-indicator-and-token-exchange-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2004-resource-indicator-and-token-exchange-contract.yaml) - Resource Indicator And Token Exchange Contract
- [`spc:oauth-grant-audit-evidence-contract`](https://github.com/groupsum/oauth-delegated-authorization-governance-pack/blob/master/src/oauth_delegated_authorization_governance_pack/templates/specs/SPEC-2005-oauth-grant-audit-evidence-contract.yaml) - OAuth Grant Audit Evidence Contract

## Install With uv

```bash
uv add oauth-delegated-authorization-governance-pack
uv add ssot-registry oauth-delegated-authorization-governance-pack
```

## Use With The SSOT Registry CLI

The pack is not trusted implicitly. Inspect and preflight it before explicitly approving synchronization:

```bash
uvx --from ssot-registry ssot pack inspect oauth_delegated_authorization_governance_pack
uvx --from ssot-registry ssot pack preflight . oauth_delegated_authorization_governance_pack --all
uvx --from ssot-registry ssot pack sync . oauth_delegated_authorization_governance_pack --all --trust --yes
uvx --from ssot-registry ssot validate .
```

Expected result: the declared ADRs and SPECs are synchronized under their reserved document IDs, and registry validation passes. Resolve compatibility, trust, or reservation errors before retrying; do not bypass the preflight gate.

## Programmatic Usage

```python
from oauth_delegated_authorization_governance_pack import load_document_manifest, read_packaged_document_text

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
text = read_packaged_document_text("spec", "SPEC-2000-oauth-scope-consent-and-grant-contract.yaml")
```

## Resources

- GitHub package repository: [groupsum/oauth-delegated-authorization-governance-pack](https://github.com/groupsum/oauth-delegated-authorization-governance-pack)
- PyPI package: [oauth-delegated-authorization-governance-pack](https://pypi.org/project/oauth-delegated-authorization-governance-pack/)
- SSOT Registry: [ssot-registry](https://pypi.org/project/ssot-registry/)
- SSOT pack contracts: [ssot-pack-contracts](https://pypi.org/project/ssot-pack-contracts/)

## Normative Ownership Boundary

This package is the canonical owner of the oauth delegated authorization governance surfaces represented by its packaged ADRs and SPECs. Adjacent packs may define integration profiles, but must reference these document identities instead of restating their normative requirements.
