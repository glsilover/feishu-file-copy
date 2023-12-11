# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .custom_workplace_access_data import CustomWorkplaceAccessData


class SearchCustomWorkplaceAccessDataResponseBody(object):
    _types = {
        "items": List[CustomWorkplaceAccessData],
        "has_more": bool,
        "page_token": str,
    }

    def __init__(self, d=None):
        self.items: Optional[List[CustomWorkplaceAccessData]] = None
        self.has_more: Optional[bool] = None
        self.page_token: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchCustomWorkplaceAccessDataResponseBodyBuilder":
        return SearchCustomWorkplaceAccessDataResponseBodyBuilder()


class SearchCustomWorkplaceAccessDataResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._search_custom_workplace_access_data_response_body = SearchCustomWorkplaceAccessDataResponseBody()

    def items(self, items: List[CustomWorkplaceAccessData]) -> "SearchCustomWorkplaceAccessDataResponseBodyBuilder":
        self._search_custom_workplace_access_data_response_body.items = items
        return self

    def has_more(self, has_more: bool) -> "SearchCustomWorkplaceAccessDataResponseBodyBuilder":
        self._search_custom_workplace_access_data_response_body.has_more = has_more
        return self

    def page_token(self, page_token: str) -> "SearchCustomWorkplaceAccessDataResponseBodyBuilder":
        self._search_custom_workplace_access_data_response_body.page_token = page_token
        return self

    def build(self) -> "SearchCustomWorkplaceAccessDataResponseBody":
        return self._search_custom_workplace_access_data_response_body