"""Find a specification and its downstream path in the installed manifest."""

from oauth_delegated_authorization_governance_pack import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:oauth-scope-consent-and-grant-contract"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2000-oauth-scope-consent-and-grant-contract.yaml"
