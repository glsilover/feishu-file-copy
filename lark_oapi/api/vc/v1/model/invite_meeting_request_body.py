# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .meeting_user import MeetingUser


class InviteMeetingRequestBody(object):
    _types = {
        "invitees": List[MeetingUser],
    }

    def __init__(self, d=None):
        self.invitees: Optional[List[MeetingUser]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InviteMeetingRequestBodyBuilder":
        return InviteMeetingRequestBodyBuilder()


class InviteMeetingRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._invite_meeting_request_body = InviteMeetingRequestBody()

    def invitees(self, invitees: List[MeetingUser]) -> "InviteMeetingRequestBodyBuilder":
        self._invite_meeting_request_body.invitees = invitees
        return self

    def build(self) -> "InviteMeetingRequestBody":
        return self._invite_meeting_request_body