# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ChatMember(object):
    _types = {
        "user_id": str,
    }

    def __init__(self, d=None):
        self.user_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatMemberBuilder":
        return ChatMemberBuilder()


class ChatMemberBuilder(object):
    def __init__(self) -> None:
        self._chat_member = ChatMember()

    def user_id(self, user_id: str) -> "ChatMemberBuilder":
        self._chat_member.user_id = user_id
        return self

    def build(self) -> "ChatMember":
        return self._chat_member