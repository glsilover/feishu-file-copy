# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class TerminateApplicationRequestBody(object):
    _types = {
        "termination_type": int,
        "termination_reason_list": List[str],
        "termination_reason_note": str,
    }

    def __init__(self, d=None):
        self.termination_type: Optional[int] = None
        self.termination_reason_list: Optional[List[str]] = None
        self.termination_reason_note: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "TerminateApplicationRequestBodyBuilder":
        return TerminateApplicationRequestBodyBuilder()


class TerminateApplicationRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._terminate_application_request_body = TerminateApplicationRequestBody()

    def termination_type(self, termination_type: int) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_type = termination_type
        return self

    def termination_reason_list(self, termination_reason_list: List[str]) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_reason_list = termination_reason_list
        return self

    def termination_reason_note(self, termination_reason_note: str) -> "TerminateApplicationRequestBodyBuilder":
        self._terminate_application_request_body.termination_reason_note = termination_reason_note
        return self

    def build(self) -> "TerminateApplicationRequestBody":
        return self._terminate_application_request_body
