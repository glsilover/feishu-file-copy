# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_file_statistics_response_body import GetFileStatisticsResponseBody


class GetFileStatisticsResponse(BaseResponse):
    _types = {
        "data": GetFileStatisticsResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetFileStatisticsResponseBody] = None
        init(self, d, self._types)