# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetAttachmentRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.user_id_type: Optional[str] = None
        self.attachment_guid: Optional[str] = None

    @staticmethod
    def builder() -> "GetAttachmentRequestBuilder":
        return GetAttachmentRequestBuilder()


class GetAttachmentRequestBuilder(object):

    def __init__(self) -> None:
        get_attachment_request = GetAttachmentRequest()
        get_attachment_request.http_method = HttpMethod.GET
        get_attachment_request.uri = "/open-apis/task/v2/attachments/:attachment_guid"
        get_attachment_request.token_types = {AccessTokenType.TENANT, AccessTokenType.USER}
        self._get_attachment_request: GetAttachmentRequest = get_attachment_request

    def user_id_type(self, user_id_type: str) -> "GetAttachmentRequestBuilder":
        self._get_attachment_request.user_id_type = user_id_type
        self._get_attachment_request.add_query("user_id_type", user_id_type)
        return self

    def attachment_guid(self, attachment_guid: str) -> "GetAttachmentRequestBuilder":
        self._get_attachment_request.attachment_guid = attachment_guid
        self._get_attachment_request.paths["attachment_guid"] = str(attachment_guid)
        return self

    def build(self) -> GetAttachmentRequest:
        return self._get_attachment_request
