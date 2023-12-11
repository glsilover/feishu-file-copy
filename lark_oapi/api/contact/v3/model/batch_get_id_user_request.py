# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_get_id_user_request_body import BatchGetIdUserRequestBody


class BatchGetIdUserRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[BatchGetIdUserRequestBody] = None

    @staticmethod
    def builder() -> "BatchGetIdUserRequestBuilder":
        return BatchGetIdUserRequestBuilder()


class BatchGetIdUserRequestBuilder(object):

    def __init__(self) -> None:
        batch_get_id_user_request = BatchGetIdUserRequest()
        batch_get_id_user_request.http_method = HttpMethod.POST
        batch_get_id_user_request.uri = "/open-apis/contact/v3/users/batch_get_id"
        batch_get_id_user_request.token_types = {AccessTokenType.TENANT}
        self._batch_get_id_user_request: BatchGetIdUserRequest = batch_get_id_user_request

    def user_id_type(self, user_id_type: str) -> "BatchGetIdUserRequestBuilder":
        self._batch_get_id_user_request.user_id_type = user_id_type
        self._batch_get_id_user_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: BatchGetIdUserRequestBody) -> "BatchGetIdUserRequestBuilder":
        self._batch_get_id_user_request.request_body = request_body
        self._batch_get_id_user_request.body = request_body
        return self

    def build(self) -> BatchGetIdUserRequest:
        return self._batch_get_id_user_request
