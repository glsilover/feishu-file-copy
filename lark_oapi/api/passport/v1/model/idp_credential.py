# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class IdpCredential(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "IdpCredentialBuilder":
        return IdpCredentialBuilder()


class IdpCredentialBuilder(object):
    def __init__(self) -> None:
        self._idp_credential = IdpCredential()

    def build(self) -> "IdpCredential":
        return self._idp_credential
