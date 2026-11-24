"""Inspect the installed pack identity."""

from oauth_delegated_authorization_governance_pack import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:oauth-delegated-authorization"
print(metadata["origin"]["id"])
