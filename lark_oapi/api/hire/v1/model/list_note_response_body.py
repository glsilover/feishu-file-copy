# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .note import Note


class ListNoteResponseBody(object):
    _types = {
        "items": List[Note],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Note]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListNoteResponseBodyBuilder":
        return ListNoteResponseBodyBuilder()


class ListNoteResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_note_response_body = ListNoteResponseBody()

    def items(self, items: List[Note]) -> "ListNoteResponseBodyBuilder":
        self._list_note_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListNoteResponseBodyBuilder":
        self._list_note_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListNoteResponseBodyBuilder":
        self._list_note_response_body.page_token = page_token
        return self

    def build(self) -> "ListNoteResponseBody":
        return self._list_note_response_body
