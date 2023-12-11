# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class SearchRoomLevelRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.custom_level_ids: Optional[str] = None

    @staticmethod
    def builder() -> "SearchRoomLevelRequestBuilder":
        return SearchRoomLevelRequestBuilder()


class SearchRoomLevelRequestBuilder(object):

    def __init__(self) -> None:
        search_room_level_request = SearchRoomLevelRequest()
        search_room_level_request.http_method = HttpMethod.GET
        search_room_level_request.uri = "/open-apis/vc/v1/room_levels/search"
        search_room_level_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._search_room_level_request: SearchRoomLevelRequest = search_room_level_request

    def custom_level_ids(self, custom_level_ids: str) -> "SearchRoomLevelRequestBuilder":
        self._search_room_level_request.custom_level_ids = custom_level_ids
        self._search_room_level_request.add_query("custom_level_ids", custom_level_ids)
        return self

    def build(self) -> SearchRoomLevelRequest:
        return self._search_room_level_request
