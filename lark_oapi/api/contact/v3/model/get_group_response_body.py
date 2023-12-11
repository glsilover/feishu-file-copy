# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .group import Group


class GetGroupResponseBody(object):
    _types = {
        "group": Group,
    }

    def __init__(self, d=None):
        self.group: Optional[Group] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetGroupResponseBodyBuilder":
        return GetGroupResponseBodyBuilder()


class GetGroupResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_group_response_body = GetGroupResponseBody()

    def group(self, group: Group) -> "GetGroupResponseBodyBuilder":
        self._get_group_response_body.group = group
        return self

    def build(self) -> "GetGroupResponseBody":
        return self._get_group_response_body
