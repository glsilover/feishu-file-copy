# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .note import Note


class CreateNoteResponseBody(object):
    _types = {
        "note": Note,
    }

    def __init__(self, d=None):
        self.note: Optional[Note] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateNoteResponseBodyBuilder":
        return CreateNoteResponseBodyBuilder()


class CreateNoteResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_note_response_body = CreateNoteResponseBody()

    def note(self, note: Note) -> "CreateNoteResponseBodyBuilder":
        self._create_note_response_body.note = note
        return self

    def build(self) -> "CreateNoteResponseBody":
        return self._create_note_response_body
