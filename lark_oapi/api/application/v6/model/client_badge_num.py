# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ClientBadgeNum(object):
    _types = {
        "web_app": int,
        "gadget": int,
    }

    def __init__(self, d=None):
        self.web_app: Optional[int] = None
        self.gadget: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ClientBadgeNumBuilder":
        return ClientBadgeNumBuilder()


class ClientBadgeNumBuilder(object):
    def __init__(self) -> None:
        self._client_badge_num = ClientBadgeNum()

    def web_app(self, web_app: int) -> "ClientBadgeNumBuilder":
        self._client_badge_num.web_app = web_app
        return self

    def gadget(self, gadget: int) -> "ClientBadgeNumBuilder":
        self._client_badge_num.gadget = gadget
        return self

    def build(self) -> "ClientBadgeNum":
        return self._client_badge_num
