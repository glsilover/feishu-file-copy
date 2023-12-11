# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListRegistrationSchemaRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.page_size: Optional[int] = None
        self.page_token: Optional[str] = None
        self.scenario: Optional[int] = None

    @staticmethod
    def builder() -> "ListRegistrationSchemaRequestBuilder":
        return ListRegistrationSchemaRequestBuilder()


class ListRegistrationSchemaRequestBuilder(object):

    def __init__(self) -> None:
        list_registration_schema_request = ListRegistrationSchemaRequest()
        list_registration_schema_request.http_method = HttpMethod.GET
        list_registration_schema_request.uri = "/open-apis/hire/v1/registration_schemas"
        list_registration_schema_request.token_types = {AccessTokenType.TENANT}
        self._list_registration_schema_request: ListRegistrationSchemaRequest = list_registration_schema_request

    def page_size(self, page_size: int) -> "ListRegistrationSchemaRequestBuilder":
        self._list_registration_schema_request.page_size = page_size
        self._list_registration_schema_request.add_query("page_size", page_size)
        return self

    def page_token(self, page_token: str) -> "ListRegistrationSchemaRequestBuilder":
        self._list_registration_schema_request.page_token = page_token
        self._list_registration_schema_request.add_query("page_token", page_token)
        return self

    def scenario(self, scenario: int) -> "ListRegistrationSchemaRequestBuilder":
        self._list_registration_schema_request.scenario = scenario
        self._list_registration_schema_request.add_query("scenario", scenario)
        return self

    def build(self) -> ListRegistrationSchemaRequest:
        return self._list_registration_schema_request
