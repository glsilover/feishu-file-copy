# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .job_family import JobFamily


class CreateJobFamilyRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.request_body: Optional[JobFamily] = None

    @staticmethod
    def builder() -> "CreateJobFamilyRequestBuilder":
        return CreateJobFamilyRequestBuilder()


class CreateJobFamilyRequestBuilder(object):

    def __init__(self) -> None:
        create_job_family_request = CreateJobFamilyRequest()
        create_job_family_request.http_method = HttpMethod.POST
        create_job_family_request.uri = "/open-apis/corehr/v1/job_families"
        create_job_family_request.token_types = {AccessTokenType.TENANT}
        self._create_job_family_request: CreateJobFamilyRequest = create_job_family_request

    def client_token(self, client_token: str) -> "CreateJobFamilyRequestBuilder":
        self._create_job_family_request.client_token = client_token
        self._create_job_family_request.add_query("client_token", client_token)
        return self

    def request_body(self, request_body: JobFamily) -> "CreateJobFamilyRequestBuilder":
        self._create_job_family_request.request_body = request_body
        self._create_job_family_request.body = request_body
        return self

    def build(self) -> CreateJobFamilyRequest:
        return self._create_job_family_request
