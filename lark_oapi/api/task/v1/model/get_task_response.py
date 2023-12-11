# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_task_response_body import GetTaskResponseBody


class GetTaskResponse(BaseResponse):
    _types = {
        "data": GetTaskResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetTaskResponseBody] = None
        init(self, d, self._types)
