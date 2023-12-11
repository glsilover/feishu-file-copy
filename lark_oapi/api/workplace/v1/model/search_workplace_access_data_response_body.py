# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .workplace_access_data import WorkplaceAccessData


class SearchWorkplaceAccessDataResponseBody(object):
    _types = {
        "items": List[WorkplaceAccessData],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[WorkplaceAccessData]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchWorkplaceAccessDataResponseBodyBuilder":
        return SearchWorkplaceAccessDataResponseBodyBuilder()


class SearchWorkplaceAccessDataResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_workplace_access_data_response_body = SearchWorkplaceAccessDataResponseBody()

    def items(self, items: List[WorkplaceAccessData]) -> "SearchWorkplaceAccessDataResponseBodyBuilder":
        self._search_workplace_access_data_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "SearchWorkplaceAccessDataResponseBodyBuilder":
        self._search_workplace_access_data_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchWorkplaceAccessDataResponseBodyBuilder":
        self._search_workplace_access_data_response_body.page_token = page_token
        return self

    def build(self) -> "SearchWorkplaceAccessDataResponseBody":
        return self._search_workplace_access_data_response_body