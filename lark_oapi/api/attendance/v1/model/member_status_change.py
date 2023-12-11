# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MemberStatusChange(object):
    _types = {
        "onboarding_on_no_need_punch": bool,
        "onboarding_off_no_need_punch": bool,
        "offboarding_on_no_need_punch": bool,
        "offboarding_off_no_need_punch": bool,
    }

    def __init__(self, d=None):
        self.onboarding_on_no_need_punch: Optional[bool] = None
        self.onboarding_off_no_need_punch: Optional[bool] = None
        self.offboarding_on_no_need_punch: Optional[bool] = None
        self.offboarding_off_no_need_punch: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MemberStatusChangeBuilder":
        return MemberStatusChangeBuilder()


class MemberStatusChangeBuilder(object):
    def __init__(self) -> None:
        self._member_status_change = MemberStatusChange()

    def onboarding_on_no_need_punch(self, onboarding_on_no_need_punch: bool) -> "MemberStatusChangeBuilder":
        self._member_status_change.onboarding_on_no_need_punch = onboarding_on_no_need_punch
        return self

    def onboarding_off_no_need_punch(self, onboarding_off_no_need_punch: bool) -> "MemberStatusChangeBuilder":
        self._member_status_change.onboarding_off_no_need_punch = onboarding_off_no_need_punch
        return self

    def offboarding_on_no_need_punch(self, offboarding_on_no_need_punch: bool) -> "MemberStatusChangeBuilder":
        self._member_status_change.offboarding_on_no_need_punch = offboarding_on_no_need_punch
        return self

    def offboarding_off_no_need_punch(self, offboarding_off_no_need_punch: bool) -> "MemberStatusChangeBuilder":
        self._member_status_change.offboarding_off_no_need_punch = offboarding_off_no_need_punch
        return self

    def build(self) -> "MemberStatusChange":
        return self._member_status_change