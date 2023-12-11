# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .contract import Contract


class PatchContractResponseBody(object):
    _types = {
        "contract": Contract,
    }

    def __init__(self, d=None):
        self.contract: Optional[Contract] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PatchContractResponseBodyBuilder":
        return PatchContractResponseBodyBuilder()


class PatchContractResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._patch_contract_response_body = PatchContractResponseBody()

    def contract(self, contract: Contract) -> "PatchContractResponseBodyBuilder":
        self._patch_contract_response_body.contract = contract
        return self

    def build(self) -> "PatchContractResponseBody":
        return self._patch_contract_response_body
