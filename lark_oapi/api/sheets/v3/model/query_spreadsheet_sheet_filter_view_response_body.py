# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .filter_view import FilterView


class QuerySpreadsheetSheetFilterViewResponseBody(object):
    _types = {
        "items": List[FilterView],
    }

    def __init__(self, d=None):
        self.items: Optional[List[FilterView]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "QuerySpreadsheetSheetFilterViewResponseBodyBuilder":
        return QuerySpreadsheetSheetFilterViewResponseBodyBuilder()


class QuerySpreadsheetSheetFilterViewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._query_spreadsheet_sheet_filter_view_response_body = QuerySpreadsheetSheetFilterViewResponseBody()

    def items(self, items: List[FilterView]) -> "QuerySpreadsheetSheetFilterViewResponseBodyBuilder":
        self._query_spreadsheet_sheet_filter_view_response_body.items = items
        return self

    def build(self) -> "QuerySpreadsheetSheetFilterViewResponseBody":
        return self._query_spreadsheet_sheet_filter_view_response_body
