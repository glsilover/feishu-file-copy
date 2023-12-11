# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ChatManagers(object):
    _types = {
        "manager_id": int,
    }

    def __init__(self, d=None):
        self.manager_id: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ChatManagersBuilder":
        return ChatManagersBuilder()


class ChatManagersBuilder(object):
    def __init__(self) -> None:
        self._chat_managers = ChatManagers()

    def manager_id(self, manager_id: int) -> "ChatManagersBuilder":
        self._chat_managers.manager_id = manager_id
        return self

    def build(self) -> "ChatManagers":
        return self._chat_managers