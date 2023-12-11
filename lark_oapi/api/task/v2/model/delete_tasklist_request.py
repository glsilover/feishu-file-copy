# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class DeleteTasklistRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.tasklist_guid: Optional[str] = None

    @staticmethod
    def builder() -> "DeleteTasklistRequestBuilder":
        return DeleteTasklistRequestBuilder()


class DeleteTasklistRequestBuilder(object):

    def __init__(self) -> None:
        delete_tasklist_request = DeleteTasklistRequest()
        delete_tasklist_request.http_method = HttpMethod.DELETE
        delete_tasklist_request.uri = "/open-apis/task/v2/tasklists/:tasklist_guid"
        delete_tasklist_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._delete_tasklist_request: DeleteTasklistRequest = delete_tasklist_request

    def tasklist_guid(self, tasklist_guid: str) -> "DeleteTasklistRequestBuilder":
        self._delete_tasklist_request.tasklist_guid = tasklist_guid
        self._delete_tasklist_request.paths["tasklist_guid"] = str(tasklist_guid)
        return self

    def build(self) -> DeleteTasklistRequest:
        return self._delete_tasklist_request
