# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .search_entity_response_body import SearchEntityResponseBody


class SearchEntityResponse(BaseResponse):
    _types = {
        "data": SearchEntityResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[SearchEntityResponseBody] = None
        init(self, d, self._types)
