# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class GetApprovalRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.locale: Optional[str] = None
        self.with_admin_id: Optional[bool] = None
        self.user_id_type: Optional[str] = None
        self.approval_code: Optional[str] = None

    @staticmethod
    def builder() -> "GetApprovalRequestBuilder":
        return GetApprovalRequestBuilder()


class GetApprovalRequestBuilder(object):

    def __init__(self) -> None:
        get_approval_request = GetApprovalRequest()
        get_approval_request.http_method = HttpMethod.GET
        get_approval_request.uri = "/open-apis/approval/v4/approvals/:approval_code"
        get_approval_request.token_types = {AccessTokenType.TENANT}
        self._get_approval_request: GetApprovalRequest = get_approval_request

    def locale(self, locale: str) -> "GetApprovalRequestBuilder":
        self._get_approval_request.locale = locale
        self._get_approval_request.add_query("locale", locale)
        return self

    def with_admin_id(self, with_admin_id: bool) -> "GetApprovalRequestBuilder":
        self._get_approval_request.with_admin_id = with_admin_id
        self._get_approval_request.add_query("with_admin_id", with_admin_id)
        return self

    def user_id_type(self, user_id_type: str) -> "GetApprovalRequestBuilder":
        self._get_approval_request.user_id_type = user_id_type
        self._get_approval_request.add_query("user_id_type", user_id_type)
        return self

    def approval_code(self, approval_code: str) -> "GetApprovalRequestBuilder":
        self._get_approval_request.approval_code = approval_code
        self._get_approval_request.paths["approval_code"] = str(approval_code)
        return self

    def build(self) -> GetApprovalRequest:
        return self._get_approval_request