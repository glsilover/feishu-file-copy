# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_job_change_response_body import SearchJobChangeResponseBody


class SearchJobChangeResponse(BaseResponse):
    _types = {
        "data": SearchJobChangeResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchJobChangeResponseBody] = None
        init(self, d, self._types)
