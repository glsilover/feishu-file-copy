# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DocCode(object):
    _types = {
        "text": str,
    }

    def __init__(self, d=None):
        self.text: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocCodeBuilder":
        return DocCodeBuilder()


class DocCodeBuilder(object):
    def __init__(self) -> None:
        self._doc_code = DocCode()

    def text(self, text: str) -> "DocCodeBuilder":
        self._doc_code.text = text
        return self

    def build(self) -> "DocCode":
        return self._doc_code