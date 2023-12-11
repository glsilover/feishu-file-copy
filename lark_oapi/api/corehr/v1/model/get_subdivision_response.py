# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_subdivision_response_body import GetSubdivisionResponseBody


class GetSubdivisionResponse(BaseResponse):
    _types = {
        "data": GetSubdivisionResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetSubdivisionResponseBody] = None
        init(self, d, self._types)
