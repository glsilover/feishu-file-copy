# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ChatTopNotice(object):
    _types = {
        "action_type": str,
        "message_id": str,
    }

    def __init__(self, d=None):
        self.action_type: Optional[str] = None
        self.message_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatTopNoticeBuilder":
        return ChatTopNoticeBuilder()


class ChatTopNoticeBuilder(object):
    def __init__(self) -> None:
        self._chat_top_notice = ChatTopNotice()

    def action_type(self, action_type: str) -> "ChatTopNoticeBuilder":
        self._chat_top_notice.action_type = action_type
        return self

    def message_id(self, message_id: str) -> "ChatTopNoticeBuilder":
        self._chat_top_notice.message_id = message_id
        return self

    def build(self) -> "ChatTopNotice":
        return self._chat_top_notice