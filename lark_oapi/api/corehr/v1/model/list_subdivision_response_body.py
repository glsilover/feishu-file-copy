# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .subdivision import Subdivision


class ListSubdivisionResponseBody(object):
    _types = {
        "items": List[Subdivision],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[Subdivision]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ListSubdivisionResponseBodyBuilder":
        return ListSubdivisionResponseBodyBuilder()


class ListSubdivisionResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._list_subdivision_response_body = ListSubdivisionResponseBody()

    def items(self, items: List[Subdivision]) -> "ListSubdivisionResponseBodyBuilder":
        self._list_subdivision_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "ListSubdivisionResponseBodyBuilder":
        self._list_subdivision_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "ListSubdivisionResponseBodyBuilder":
        self._list_subdivision_response_body.page_token = page_token
        return self

    def build(self) -> "ListSubdivisionResponseBody":
        return self._list_subdivision_response_body
