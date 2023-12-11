# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .external_approval import ExternalApproval


class CreateExternalApprovalRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.user_id_type: Optional[str] = None
        self.request_body: Optional[ExternalApproval] = None

    @staticmethod
    def builder() -> "CreateExternalApprovalRequestBuilder":
        return CreateExternalApprovalRequestBuilder()


class CreateExternalApprovalRequestBuilder(object):

    def __init__(self) -> None:
        create_external_approval_request = CreateExternalApprovalRequest()
        create_external_approval_request.http_method = HttpMethod.POST
        create_external_approval_request.uri = "/open-apis/approval/v4/external_approvals"
        create_external_approval_request.token_types = {AccessTokenType.TENANT}
        self._create_external_approval_request: CreateExternalApprovalRequest = create_external_approval_request

    def department_id_type(self, department_id_type: str) -> "CreateExternalApprovalRequestBuilder":
        self._create_external_approval_request.department_id_type = department_id_type
        self._create_external_approval_request.add_query("department_id_type", department_id_type)
        return self

    def user_id_type(self, user_id_type: str) -> "CreateExternalApprovalRequestBuilder":
        self._create_external_approval_request.user_id_type = user_id_type
        self._create_external_approval_request.add_query("user_id_type", user_id_type)
        return self

    def request_body(self, request_body: ExternalApproval) -> "CreateExternalApprovalRequestBuilder":
        self._create_external_approval_request.request_body = request_body
        self._create_external_approval_request.body = request_body
        return self

    def build(self) -> CreateExternalApprovalRequest:
        return self._create_external_approval_request
