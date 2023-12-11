# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .department_overview_application_app_usage_request_body import DepartmentOverviewApplicationAppUsageRequestBody


class DepartmentOverviewApplicationAppUsageRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.department_id_type: Optional[str] = None
        self.app_id: Optional[str] = None
        self.request_body: Optional[DepartmentOverviewApplicationAppUsageRequestBody] = None

    @staticmethod
    def builder() -> "DepartmentOverviewApplicationAppUsageRequestBuilder":
        return DepartmentOverviewApplicationAppUsageRequestBuilder()


class DepartmentOverviewApplicationAppUsageRequestBuilder(object):

    def __init__(self) -> None:
        department_overview_application_app_usage_request = DepartmentOverviewApplicationAppUsageRequest()
        department_overview_application_app_usage_request.http_method = HttpMethod.POST
        department_overview_application_app_usage_request.uri = "/open-apis/application/v6/applications/:app_id/app_usage/department_overview"
        department_overview_application_app_usage_request.token_types = {AccessTokenType.TENANT}
        self._department_overview_application_app_usage_request: DepartmentOverviewApplicationAppUsageRequest = department_overview_application_app_usage_request

    def department_id_type(self, department_id_type: str) -> "DepartmentOverviewApplicationAppUsageRequestBuilder":
        self._department_overview_application_app_usage_request.department_id_type = department_id_type
        self._department_overview_application_app_usage_request.add_query("department_id_type", department_id_type)
        return self

    def app_id(self, app_id: str) -> "DepartmentOverviewApplicationAppUsageRequestBuilder":
        self._department_overview_application_app_usage_request.app_id = app_id
        self._department_overview_application_app_usage_request.paths["app_id"] = str(app_id)
        return self

    def request_body(self,
                     request_body: DepartmentOverviewApplicationAppUsageRequestBody) -> "DepartmentOverviewApplicationAppUsageRequestBuilder":
        self._department_overview_application_app_usage_request.request_body = request_body
        self._department_overview_application_app_usage_request.body = request_body
        return self

    def build(self) -> DepartmentOverviewApplicationAppUsageRequest:
        return self._department_overview_application_app_usage_request