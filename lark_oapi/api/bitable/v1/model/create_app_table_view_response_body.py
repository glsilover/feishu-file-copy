# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .app_table_view import AppTableView


class CreateAppTableViewResponseBody(object):
    _types = {
        "view": AppTableView,
    }

    def __init__(self, d=None):
        self.view: Optional[AppTableView] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CreateAppTableViewResponseBodyBuilder":
        return CreateAppTableViewResponseBodyBuilder()


class CreateAppTableViewResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._create_app_table_view_response_body = CreateAppTableViewResponseBody()

    def view(self, view: AppTableView) -> "CreateAppTableViewResponseBodyBuilder":
        self._create_app_table_view_response_body.view = view
        return self

    def build(self) -> "CreateAppTableViewResponseBody":
        return self._create_app_table_view_response_body