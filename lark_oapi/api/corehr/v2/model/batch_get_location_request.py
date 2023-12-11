# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .batch_get_location_request_body import BatchGetLocationRequestBody


class BatchGetLocationRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[BatchGetLocationRequestBody] = None

    @staticmethod
    def builder() -> "BatchGetLocationRequestBuilder":
        return BatchGetLocationRequestBuilder()


class BatchGetLocationRequestBuilder(object):

    def __init__(self) -> None:
        batch_get_location_request = BatchGetLocationRequest()
        batch_get_location_request.http_method = HttpMethod.POST
        batch_get_location_request.uri = "/open-apis/corehr/v2/locations/batch_get"
        batch_get_location_request.token_types = {AccessTokenType.TENANT}
        self._batch_get_location_request: BatchGetLocationRequest = batch_get_location_request

    def request_body(self, request_body: BatchGetLocationRequestBody) -> "BatchGetLocationRequestBuilder":
        self._batch_get_location_request.request_body = request_body
        self._batch_get_location_request.body = request_body
        return self

    def build(self) -> BatchGetLocationRequest:
        return self._batch_get_location_request
