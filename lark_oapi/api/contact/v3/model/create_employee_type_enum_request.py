# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .employee_type_enum import EmployeeTypeEnum


class CreateEmployeeTypeEnumRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.request_body: Optional[EmployeeTypeEnum] = None

    @staticmethod
    def builder() -> "CreateEmployeeTypeEnumRequestBuilder":
        return CreateEmployeeTypeEnumRequestBuilder()


class CreateEmployeeTypeEnumRequestBuilder(object):

    def __init__(self) -> None:
        create_employee_type_enum_request = CreateEmployeeTypeEnumRequest()
        create_employee_type_enum_request.http_method = HttpMethod.POST
        create_employee_type_enum_request.uri = "/open-apis/contact/v3/employee_type_enums"
        create_employee_type_enum_request.token_types = {AccessTokenType.TENANT}
        self._create_employee_type_enum_request: CreateEmployeeTypeEnumRequest = create_employee_type_enum_request

    def request_body(self, request_body: EmployeeTypeEnum) -> "CreateEmployeeTypeEnumRequestBuilder":
        self._create_employee_type_enum_request.request_body = request_body
        self._create_employee_type_enum_request.body = request_body
        return self

    def build(self) -> CreateEmployeeTypeEnumRequest:
        return self._create_employee_type_enum_request
