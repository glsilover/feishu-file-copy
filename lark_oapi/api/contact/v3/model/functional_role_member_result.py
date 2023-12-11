# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class FunctionalRoleMemberResult(object):
    _types = {
        "user_id": str,
        "reason": int,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        self.reason: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "FunctionalRoleMemberResultBuilder":
        return FunctionalRoleMemberResultBuilder()


class FunctionalRoleMemberResultBuilder(object):
    def __init__(self) -> None:
        self._functional_role_member_result = FunctionalRoleMemberResult()

    def user_id(self, user_id: str) -> "FunctionalRoleMemberResultBuilder":
        self._functional_role_member_result.user_id = user_id
        return self

    def reason(self, reason: int) -> "FunctionalRoleMemberResultBuilder":
        self._functional_role_member_result.reason = reason
        return self

    def build(self) -> "FunctionalRoleMemberResult":
        return self._functional_role_member_result