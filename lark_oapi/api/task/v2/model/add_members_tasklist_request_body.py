# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .member import Member


class AddMembersTasklistRequestBody(object):
    _types = {
        "members": List[Member],
    }

    def __init__(self, d=None):
        self.members: Optional[List[Member]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AddMembersTasklistRequestBodyBuilder":
        return AddMembersTasklistRequestBodyBuilder()


class AddMembersTasklistRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._add_members_tasklist_request_body = AddMembersTasklistRequestBody()

    def members(self, members: List[Member]) -> "AddMembersTasklistRequestBodyBuilder":
        self._add_members_tasklist_request_body.members = members
        return self

    def build(self) -> "AddMembersTasklistRequestBody":
        return self._add_members_tasklist_request_body