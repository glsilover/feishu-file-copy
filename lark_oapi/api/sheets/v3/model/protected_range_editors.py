# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class ProtectedRangeEditors(object):
    _types = {
        "users": List[str],
        "departments": List[str],
        "chats": List[str],
    }

    def __init__(self, d=None):
        self.users: Optional[List[str]] = None
        self.departments: Optional[List[str]] = None
        self.chats: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProtectedRangeEditorsBuilder":
        return ProtectedRangeEditorsBuilder()


class ProtectedRangeEditorsBuilder(object):
    def __init__(self) -> None:
        self._protected_range_editors = ProtectedRangeEditors()

    def users(self, users: List[str]) -> "ProtectedRangeEditorsBuilder":
        self._protected_range_editors.users = users
        return self

    def departments(self, departments: List[str]) -> "ProtectedRangeEditorsBuilder":
        self._protected_range_editors.departments = departments
        return self

    def chats(self, chats: List[str]) -> "ProtectedRangeEditorsBuilder":
        self._protected_range_editors.chats = chats
        return self

    def build(self) -> "ProtectedRangeEditors":
        return self._protected_range_editors