# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_calendar_response_body import GetCalendarResponseBody


class GetCalendarResponse(BaseResponse):
    _types = {
        "data": GetCalendarResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetCalendarResponseBody] = None
        init(self, d, self._types)