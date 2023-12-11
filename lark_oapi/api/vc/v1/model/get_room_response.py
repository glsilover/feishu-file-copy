# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .get_room_response_body import GetRoomResponseBody


class GetRoomResponse(BaseResponse):
    _types = {
        "data": GetRoomResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[GetRoomResponseBody] = None
        init(self, d, self._types)