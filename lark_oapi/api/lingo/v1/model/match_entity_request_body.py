# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class MatchEntityRequestBody(object):
    _types = {
        "word": str,
    }

    def __init__(self, d=None):
        self.word: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "MatchEntityRequestBodyBuilder":
        return MatchEntityRequestBodyBuilder()


class MatchEntityRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._match_entity_request_body = MatchEntityRequestBody()

    def word(self, word: str) -> "MatchEntityRequestBodyBuilder":
        self._match_entity_request_body.word = word
        return self

    def build(self) -> "MatchEntityRequestBody":
        return self._match_entity_request_body