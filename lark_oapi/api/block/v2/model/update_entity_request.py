# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .entity import Entity


class UpdateEntityRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.block_id: Optional[str] = None
        self.request_body: Optional[Entity] = None

    @staticmethod
    def builder() -> "UpdateEntityRequestBuilder":
        return UpdateEntityRequestBuilder()


class UpdateEntityRequestBuilder(object):

    def __init__(self) -> None:
        update_entity_request = UpdateEntityRequest()
        update_entity_request.http_method = HttpMethod.PUT
        update_entity_request.uri = "/open-apis/block/v2/entities/:block_id"
        update_entity_request.token_types = {AccessTokenType.TENANT}
        self._update_entity_request: UpdateEntityRequest = update_entity_request

    def block_id(self, block_id: str) -> "UpdateEntityRequestBuilder":
        self._update_entity_request.block_id = block_id
        self._update_entity_request.paths["block_id"] = str(block_id)
        return self

    def request_body(self, request_body: Entity) -> "UpdateEntityRequestBuilder":
        self._update_entity_request.request_body = request_body
        self._update_entity_request.body = request_body
        return self

    def build(self) -> UpdateEntityRequest:
        return self._update_entity_request
