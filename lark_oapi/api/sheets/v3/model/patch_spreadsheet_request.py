# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .update_spreadsheet_properties import UpdateSpreadsheetProperties


class PatchSpreadsheetRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.spreadsheet_token: Optional[str] = None
        self.request_body: Optional[UpdateSpreadsheetProperties] = None

    @staticmethod
    def builder() -> "PatchSpreadsheetRequestBuilder":
        return PatchSpreadsheetRequestBuilder()


class PatchSpreadsheetRequestBuilder(object):

    def __init__(self) -> None:
        patch_spreadsheet_request = PatchSpreadsheetRequest()
        patch_spreadsheet_request.http_method = HttpMethod.PATCH
        patch_spreadsheet_request.uri = "/open-apis/sheets/v3/spreadsheets/:spreadsheet_token"
        patch_spreadsheet_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._patch_spreadsheet_request: PatchSpreadsheetRequest = patch_spreadsheet_request

    def spreadsheet_token(self, spreadsheet_token: str) -> "PatchSpreadsheetRequestBuilder":
        self._patch_spreadsheet_request.spreadsheet_token = spreadsheet_token
        self._patch_spreadsheet_request.paths["spreadsheet_token"] = str(spreadsheet_token)
        return self

    def request_body(self, request_body: UpdateSpreadsheetProperties) -> "PatchSpreadsheetRequestBuilder":
        self._patch_spreadsheet_request.request_body = request_body
        self._patch_spreadsheet_request.body = request_body
        return self

    def build(self) -> PatchSpreadsheetRequest:
        return self._patch_spreadsheet_request
