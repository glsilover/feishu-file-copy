# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_calendar_event_attendee_response_body import ListCalendarEventAttendeeResponseBody


class ListCalendarEventAttendeeResponse(BaseResponse):
    _types = {
        "data": ListCalendarEventAttendeeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListCalendarEventAttendeeResponseBody] = None
        init(self, d, self._types)
