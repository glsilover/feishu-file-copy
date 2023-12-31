# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class GetAuthorizeResponseBody(object):
    _types = {
        "redirect_uri": str,
        "code": str,
        "state": str,
    }

    def __init__(self, d=None):
        self.redirect_uri: Optional[str] = None
        self.code: Optional[str] = None
        self.state: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetAuthorizeResponseBodyBuilder":
        return GetAuthorizeResponseBodyBuilder()


class GetAuthorizeResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_authorize_response_body = GetAuthorizeResponseBody()

    def redirect_uri(self, redirect_uri: str) -> "GetAuthorizeResponseBodyBuilder":
        self._get_authorize_response_body.redirect_uri = redirect_uri
        return self

    def code(self, code: str) -> "GetAuthorizeResponseBodyBuilder":
        self._get_authorize_response_body.code = code
        return self

    def state(self, state: str) -> "GetAuthorizeResponseBodyBuilder":
        self._get_authorize_response_body.state = state
        return self

    def build(self) -> "GetAuthorizeResponseBody":
        return self._get_authorize_response_body
