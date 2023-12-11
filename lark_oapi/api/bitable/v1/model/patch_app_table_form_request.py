# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .app_table_form import AppTableForm


class PatchAppTableFormRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.app_token: Optional[str] = None
        self.table_id: Optional[str] = None
        self.form_id: Optional[str] = None
        self.request_body: Optional[AppTableForm] = None

    @staticmethod
    def builder() -> "PatchAppTableFormRequestBuilder":
        return PatchAppTableFormRequestBuilder()


class PatchAppTableFormRequestBuilder(object):

    def __init__(self) -> None:
        patch_app_table_form_request = PatchAppTableFormRequest()
        patch_app_table_form_request.http_method = HttpMethod.PATCH
        patch_app_table_form_request.uri = "/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id"
        patch_app_table_form_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_app_table_form_request: PatchAppTableFormRequest = patch_app_table_form_request

    def app_token(self, app_token: str) -> "PatchAppTableFormRequestBuilder":
        self._patch_app_table_form_request.app_token = app_token
        self._patch_app_table_form_request.paths["app_token"] = str(app_token)
        return self

    def table_id(self, table_id: str) -> "PatchAppTableFormRequestBuilder":
        self._patch_app_table_form_request.table_id = table_id
        self._patch_app_table_form_request.paths["table_id"] = str(table_id)
        return self

    def form_id(self, form_id: str) -> "PatchAppTableFormRequestBuilder":
        self._patch_app_table_form_request.form_id = form_id
        self._patch_app_table_form_request.paths["form_id"] = str(form_id)
        return self

    def request_body(self, request_body: AppTableForm) -> "PatchAppTableFormRequestBuilder":
        self._patch_app_table_form_request.request_body = request_body
        self._patch_app_table_form_request.body = request_body
        return self

    def build(self) -> PatchAppTableFormRequest:
        return self._patch_app_table_form_request
