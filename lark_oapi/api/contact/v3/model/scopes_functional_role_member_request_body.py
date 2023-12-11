# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class ScopesFunctionalRoleMemberRequestBody(object):
    _types = {
        "members": List[str],
        "departments": List[str],
    }

    def __init__(self, d=None):
        self.members: Optional[List[str]] = None
        self.departments: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ScopesFunctionalRoleMemberRequestBodyBuilder":
        return ScopesFunctionalRoleMemberRequestBodyBuilder()


class ScopesFunctionalRoleMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._scopes_functional_role_member_request_body = ScopesFunctionalRoleMemberRequestBody()

    def members(self, members: List[str]) -> "ScopesFunctionalRoleMemberRequestBodyBuilder":
        self._scopes_functional_role_member_request_body.members = members
        return self

    def departments(self, departments: List[str]) -> "ScopesFunctionalRoleMemberRequestBodyBuilder":
        self._scopes_functional_role_member_request_body.departments = departments
        return self

    def build(self) -> "ScopesFunctionalRoleMemberRequestBody":
        return self._scopes_functional_role_member_request_body
