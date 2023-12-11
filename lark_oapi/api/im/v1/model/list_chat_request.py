# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListChatRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.sort_type: Optional[str] = None
        self.page_token: Optional[str] = None
        self.page_size: Optional[int] = None

    @staticmethod
    def builder() -> "ListChatRequestBuilder":
        return ListChatRequestBuilder()


class ListChatRequestBuilder(object):

    def __init__(self) -> None:
        list_chat_request = ListChatRequest()
        list_chat_request.http_method = HttpMethod.GET
        list_chat_request.uri = "/open-apis/im/v1/chats"
        list_chat_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._list_chat_request: ListChatRequest = list_chat_request

    def user_id_type(self, user_id_type: str) -> "ListChatRequestBuilder":
        self._list_chat_request.user_id_type = user_id_type
        self._list_chat_request.add_query("user_id_type", user_id_type)
        return self

    def sort_type(self, sort_type: str) -> "ListChatRequestBuilder":
        self._list_chat_request.sort_type = sort_type
        self._list_chat_request.add_query("sort_type", sort_type)
        return self

    def page_token(self, page_token: str) -> "ListChatRequestBuilder":
        self._list_chat_request.page_token = page_token
        self._list_chat_request.add_query("page_token", page_token)
        return self

    def page_size(self, page_size: int) -> "ListChatRequestBuilder":
        self._list_chat_request.page_size = page_size
        self._list_chat_request.add_query("page_size", page_size)
        return self

    def build(self) -> ListChatRequest:
        return self._list_chat_request