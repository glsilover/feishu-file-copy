# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .deactivate_referral_account_response_body import DeactivateReferralAccountResponseBody


class DeactivateReferralAccountResponse(BaseResponse):
    _types = {
        "data": DeactivateReferralAccountResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[DeactivateReferralAccountResponseBody] = None
        init(self, d, self._types)
