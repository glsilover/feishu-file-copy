# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .match_entity_response_body import MatchEntityResponseBody


class MatchEntityResponse(BaseResponse):
    _types = {
        "data": MatchEntityResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[MatchEntityResponseBody] = None
        init(self, d, self._types)
