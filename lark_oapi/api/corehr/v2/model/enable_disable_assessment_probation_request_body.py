# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class EnableDisableAssessmentProbationRequestBody(object):
    _types = {
        "active": bool,
        "app_url": str,
    }

    def __init__(self, d=None):
        self.active: Optional[bool] = None
        self.app_url: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EnableDisableAssessmentProbationRequestBodyBuilder":
        return EnableDisableAssessmentProbationRequestBodyBuilder()


class EnableDisableAssessmentProbationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._enable_disable_assessment_probation_request_body = EnableDisableAssessmentProbationRequestBody()

    def active(self, active: bool) -> "EnableDisableAssessmentProbationRequestBodyBuilder":
        self._enable_disable_assessment_probation_request_body.active = active
        return self

    def app_url(self, app_url: str) -> "EnableDisableAssessmentProbationRequestBodyBuilder":
        self._enable_disable_assessment_probation_request_body.app_url = app_url
        return self

    def build(self) -> "EnableDisableAssessmentProbationRequestBody":
        return self._enable_disable_assessment_probation_request_body
