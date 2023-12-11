# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_get_employees_bp_request_body import BatchGetEmployeesBpRequestBody


class BatchGetEmployeesBpRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[BatchGetEmployeesBpRequestBody] = None

    @staticmethod
    def builder() -> "BatchGetEmployeesBpRequestBuilder":
        return BatchGetEmployeesBpRequestBuilder()


class BatchGetEmployeesBpRequestBuilder(object):

    def __init__(self) -> None:
        batch_get_employees_bp_request = BatchGetEmployeesBpRequest()
        batch_get_employees_bp_request.http_method = HttpMethod.POST
        batch_get_employees_bp_request.uri = "/open-apis/corehr/v2/employees/bps/batch_get"
        batch_get_employees_bp_request.token_types = {AccessTokenType.TENANT}
        self._batch_get_employees_bp_request: BatchGetEmployeesBpRequest = batch_get_employees_bp_request

    def user_id_type(self, user_id_type: str) -> "BatchGetEmployeesBpRequestBuilder":
        self._batch_get_employees_bp_request.user_id_type = user_id_type
        self._batch_get_employees_bp_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: BatchGetEmployeesBpRequestBody) -> "BatchGetEmployeesBpRequestBuilder":
        self._batch_get_employees_bp_request.request_body = request_body
        self._batch_get_employees_bp_request.body = request_body
        return self

    def build(self) -> BatchGetEmployeesBpRequest:
        return self._batch_get_employees_bp_request
