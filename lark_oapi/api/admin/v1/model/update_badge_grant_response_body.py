# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .grant import Grant


class UpdateBadgeGrantResponseBody(object):
    _types = {
        "grant": Grant,
    }

    def __init__(self, d=None):
        self.grant: Optional[Grant] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UpdateBadgeGrantResponseBodyBuilder":
        return UpdateBadgeGrantResponseBodyBuilder()


class UpdateBadgeGrantResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._update_badge_grant_response_body = UpdateBadgeGrantResponseBody()

    def grant(self, grant: Grant) -> "UpdateBadgeGrantResponseBodyBuilder":
        self._update_badge_grant_response_body.grant = grant
        return self

    def build(self) -> "UpdateBadgeGrantResponseBody":
        return self._update_badge_grant_response_body