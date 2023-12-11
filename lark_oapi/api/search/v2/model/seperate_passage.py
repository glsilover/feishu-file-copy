# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class SeperatePassage(object):
    _types = {
        "passage_id": str,
        "obj_id": str,
        "content": str,
        "num_tokens": int,
    }

    def __init__(self, d=None):
        self.passage_id: Optional[str] = None
        self.obj_id: Optional[str] = None
        self.content: Optional[str] = None
        self.num_tokens: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SeperatePassageBuilder":
        return SeperatePassageBuilder()


class SeperatePassageBuilder(object):
    def __init__(self) -> None:
        self._seperate_passage = SeperatePassage()

    def passage_id(self, passage_id: str) -> "SeperatePassageBuilder":
        self._seperate_passage.passage_id = passage_id
        return self

    def obj_id(self, obj_id: str) -> "SeperatePassageBuilder":
        self._seperate_passage.obj_id = obj_id
        return self

    def content(self, content: str) -> "SeperatePassageBuilder":
        self._seperate_passage.content = content
        return self

    def num_tokens(self, num_tokens: int) -> "SeperatePassageBuilder":
        self._seperate_passage.num_tokens = num_tokens
        return self

    def build(self) -> "SeperatePassage":
        return self._seperate_passage
