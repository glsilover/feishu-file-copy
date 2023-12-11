# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .mailgroup import Mailgroup


class PatchMailgroupRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.mailgroup_id: Optional[str] = None
        self.request_body: Optional[Mailgroup] = None

    @staticmethod
    def builder() -> "PatchMailgroupRequestBuilder":
        return PatchMailgroupRequestBuilder()


class PatchMailgroupRequestBuilder(object):

    def __init__(self) -> None:
        patch_mailgroup_request = PatchMailgroupRequest()
        patch_mailgroup_request.http_method = HttpMethod.PATCH
        patch_mailgroup_request.uri = "/open-apis/mail/v1/mailgroups/:mailgroup_id"
        patch_mailgroup_request.token_types = {AccessTokenType.TENANT}
        self._patch_mailgroup_request: PatchMailgroupRequest = patch_mailgroup_request

    def mailgroup_id(self, mailgroup_id: str) -> "PatchMailgroupRequestBuilder":
        self._patch_mailgroup_request.mailgroup_id = mailgroup_id
        self._patch_mailgroup_request.paths["mailgroup_id"] = str(mailgroup_id)
        return self

    def request_body(self, request_body: Mailgroup) -> "PatchMailgroupRequestBuilder":
        self._patch_mailgroup_request.request_body = request_body
        self._patch_mailgroup_request.body = request_body
        return self

    def build(self) -> PatchMailgroupRequest:
        return self._patch_mailgroup_request