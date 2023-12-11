# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .meeting_list_export_response_body import MeetingListExportResponseBody


class MeetingListExportResponse(BaseResponse):
    _types = {
        "data": MeetingListExportResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[MeetingListExportResponseBody] = None
        init(self, d, self._types)
