# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .room_level import RoomLevel


class ListRoomLevelResponseBody(object):
    _types = {
        "items": List[RoomLevel],
        "page_token": str,
        "has_more": bool,
    }

    def __init__(self, d=None):
        self.items: Optional[List[RoomLevel]] = None
        self.page_token: Optional[str] = None
        self.has_more: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListRoomLevelResponseBodyBuilder":
        return ListRoomLevelResponseBodyBuilder()


class ListRoomLevelResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_room_level_response_body = ListRoomLevelResponseBody()

    def items(self, items: List[RoomLevel]) -> "ListRoomLevelResponseBodyBuilder":
        self._list_room_level_response_body.items = items
        return self

    def page_token(self, page_token: str) -> "ListRoomLevelResponseBodyBuilder":
        self._list_room_level_response_body.page_token = page_token
        return self

    def has_more(self, has_more: bool) -> "ListRoomLevelResponseBodyBuilder":
        self._list_room_level_response_body.has_more = has_more
        return self

    def build(self) -> "ListRoomLevelResponseBody":
        return self._list_room_level_response_body