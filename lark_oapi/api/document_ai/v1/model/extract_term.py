# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class ExtractTerm(object):
    _types = {
        "initial_time": str,
        "initial_unit": str,
    }

    def __init__(self, d=None):
        self.initial_time: Optional[str] = None
        self.initial_unit: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ExtractTermBuilder":
        return ExtractTermBuilder()


class ExtractTermBuilder(object):
    def __init__(self) -> None:
        self._extract_term = ExtractTerm()

    def initial_time(self, initial_time: str) -> "ExtractTermBuilder":
        self._extract_term.initial_time = initial_time
        return self

    def initial_unit(self, initial_unit: str) -> "ExtractTermBuilder":
        self._extract_term.initial_unit = initial_unit
        return self

    def build(self) -> "ExtractTerm":
        return self._extract_term
