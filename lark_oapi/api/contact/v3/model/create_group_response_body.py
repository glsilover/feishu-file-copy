# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class CreateGroupResponseBody(object):
    _types = {
        "group_id": str,
    }

    def __init__(self, d=None):
        self.group_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateGroupResponseBodyBuilder":
        return CreateGroupResponseBodyBuilder()


class CreateGroupResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_group_response_body = CreateGroupResponseBody()

    def group_id(self, group_id: str) -> "CreateGroupResponseBodyBuilder":
        self._create_group_response_body.group_id = group_id
        return self

    def build(self) -> "CreateGroupResponseBody":
        return self._create_group_response_body
