# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetChatModerationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.chat_id: Optional[str] = None

    @staticmethod
    def builder() -> "GetChatModerationRequestBuilder":
        return GetChatModerationRequestBuilder()


class GetChatModerationRequestBuilder(object):

    def __init__(self) -> None:
        get_chat_moderation_request = GetChatModerationRequest()
        get_chat_moderation_request.http_method = HttpMethod.GET
        get_chat_moderation_request.uri = "/open-apis/im/v1/chats/:chat_id/moderation"
        get_chat_moderation_request.token_types = {AccessTokenType.USER, AccessTokenType.TENANT}
        self._get_chat_moderation_request: GetChatModerationRequest = get_chat_moderation_request

    def user_id_type(self, user_id_type: str) -> "GetChatModerationRequestBuilder":
        self._get_chat_moderation_request.user_id_type = user_id_type
        self._get_chat_moderation_request.add_query("user_id_type", user_id_type)
        return self

    def page_size(self, page_size: int) -> "GetChatModerationRequestBuilder":
        self._get_chat_moderation_request.page_size = page_size
        self._get_chat_moderation_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "GetChatModerationRequestBuilder":
        self._get_chat_moderation_request.page_token = page_token
        self._get_chat_moderation_request.add_query("page_token", page_token)
        return self

    def chat_id(self, chat_id: str) -> "GetChatModerationRequestBuilder":
        self._get_chat_moderation_request.chat_id = chat_id
        self._get_chat_moderation_request.paths["chat_id"] = str(chat_id)
        return self

    def build(self) -> GetChatModerationRequest:
        return self._get_chat_moderation_request