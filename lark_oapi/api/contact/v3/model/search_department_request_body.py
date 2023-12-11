# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class SearchDepartmentRequestBody(object):
    _types = {
        "query": str,
    }

    def __init__(self, d=None):
        self.query: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SearchDepartmentRequestBodyBuilder":
        return SearchDepartmentRequestBodyBuilder()


class SearchDepartmentRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._search_department_request_body = SearchDepartmentRequestBody()

    def query(self, query: str) -> "SearchDepartmentRequestBodyBuilder":
        self._search_department_request_body.query = query
        return self

    def build(self) -> "SearchDepartmentRequestBody":
        return self._search_department_request_body
