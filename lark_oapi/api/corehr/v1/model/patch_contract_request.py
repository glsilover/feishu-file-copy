# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest
from .contract import Contract


class PatchContractRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()
        self.client_token: Optional[str] = None
        self.contract_id: Optional[str] = None
        self.request_body: Optional[Contract] = None

    @staticmethod
    def builder() -> "PatchContractRequestBuilder":
        return PatchContractRequestBuilder()


class PatchContractRequestBuilder(object):

    def __init__(self) -> None:
        patch_contract_request = PatchContractRequest()
        patch_contract_request.http_method = HttpMethod.PATCH
        patch_contract_request.uri = "/open-apis/corehr/v1/contracts/:contract_id"
        patch_contract_request.token_types = {AccessTokenType.TENANT}
        self._patch_contract_request: PatchContractRequest = patch_contract_request

    def client_token(self, client_token: str) -> "PatchContractRequestBuilder":
        self._patch_contract_request.client_token = client_token
        self._patch_contract_request.add_query("client_token", client_token)
        return self

    def contract_id(self, contract_id: str) -> "PatchContractRequestBuilder":
        self._patch_contract_request.contract_id = contract_id
        self._patch_contract_request.paths["contract_id"] = str(contract_id)
        return self

    def request_body(self, request_body: Contract) -> "PatchContractRequestBuilder":
        self._patch_contract_request.request_body = request_body
        self._patch_contract_request.body = request_body
        return self

    def build(self) -> PatchContractRequest:
        return self._patch_contract_request