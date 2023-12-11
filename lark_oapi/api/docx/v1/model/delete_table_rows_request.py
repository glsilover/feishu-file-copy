# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DeleteTableRowsRequest(object):
    _types = {
        "row_start_index": int,
        "row_end_index": int,
    }

    def __init__(self, d=None):
        self.row_start_index: Optional[int] = None
        self.row_end_index: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DeleteTableRowsRequestBuilder":
        return DeleteTableRowsRequestBuilder()


class DeleteTableRowsRequestBuilder(object):
    def __init__(self) -> None:
        self._delete_table_rows_request = DeleteTableRowsRequest()

    def row_start_index(self, row_start_index: int) -> "DeleteTableRowsRequestBuilder":
        self._delete_table_rows_request.row_start_index = row_start_index
        return self

    def row_end_index(self, row_end_index: int) -> "DeleteTableRowsRequestBuilder":
        self._delete_table_rows_request.row_end_index = row_end_index
        return self

    def build(self) -> "DeleteTableRowsRequest":
        return self._delete_table_rows_request