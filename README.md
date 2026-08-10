# oauth-delegated-authorization-governance-pack

Governance for OAuth clients, grants, scopes, consent, authorization code with PKCE, PAR, JAR, resource indicators, token exchange, and grant evidence.

## Package identity

- Pack ID: `pack:oauth-delegated-authorization`
- PyPI distribution: `oauth-delegated-authorization-governance-pack`
- Python import: `oauth_delegated_authorization_governance_pack`
- Reservation owner: `extension-pack:oauth-delegated-authorization-governance-pack`

## Normative ownership

This package is the canonical owner of the governance surfaces represented by its packaged ADRs and SPECs. Adjacent governance packs reference these documents rather than restating their requirements.

## Install

```bash
uv add oauth-delegated-authorization-governance-pack
uv run ssot pack sync . oauth_delegated_authorization_governance_pack --all --trust --yes
uv run ssot validate .
```

## Authority sources

- https://www.rfc-editor.org/rfc/rfc9700
- https://www.rfc-editor.org/rfc/rfc6749
