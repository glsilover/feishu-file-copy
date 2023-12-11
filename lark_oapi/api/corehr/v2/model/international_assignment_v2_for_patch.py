# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .enum import Enum


class InternationalAssignmentV2ForPatch(object):
    _types = {
        "effective_time": str,
        "international_assignment_expected_end_date": str,
        "expiration_time": str,
        "assignment_country": str,
        "assignment_city": str,
        "assignment_company": str,
        "international_assignment_status": Enum,
        "international_assignment_type": Enum,
        "international_assignment_allowance": bool,
        "accommodation": bool,
        "description": str,
    }

    def __init__(self, d=None):
        self.effective_time: Optional[str] = None
        self.international_assignment_expected_end_date: Optional[str] = None
        self.expiration_time: Optional[str] = None
        self.assignment_country: Optional[str] = None
        self.assignment_city: Optional[str] = None
        self.assignment_company: Optional[str] = None
        self.international_assignment_status: Optional[Enum] = None
        self.international_assignment_type: Optional[Enum] = None
        self.international_assignment_allowance: Optional[bool] = None
        self.accommodation: Optional[bool] = None
        self.description: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InternationalAssignmentV2ForPatchBuilder":
        return InternationalAssignmentV2ForPatchBuilder()


class InternationalAssignmentV2ForPatchBuilder(object):
    def __init__(self) -> None:
        self._international_assignment_v2_for_patch = InternationalAssignmentV2ForPatch()

    def effective_time(self, effective_time: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.effective_time = effective_time
        return self

    def international_assignment_expected_end_date(self,
                                                   international_assignment_expected_end_date: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.international_assignment_expected_end_date = international_assignment_expected_end_date
        return self

    def expiration_time(self, expiration_time: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.expiration_time = expiration_time
        return self

    def assignment_country(self, assignment_country: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.assignment_country = assignment_country
        return self

    def assignment_city(self, assignment_city: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.assignment_city = assignment_city
        return self

    def assignment_company(self, assignment_company: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.assignment_company = assignment_company
        return self

    def international_assignment_status(self,
                                        international_assignment_status: Enum) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.international_assignment_status = international_assignment_status
        return self

    def international_assignment_type(self,
                                      international_assignment_type: Enum) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.international_assignment_type = international_assignment_type
        return self

    def international_assignment_allowance(self,
                                           international_assignment_allowance: bool) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.international_assignment_allowance = international_assignment_allowance
        return self

    def accommodation(self, accommodation: bool) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.accommodation = accommodation
        return self

    def description(self, description: str) -> "InternationalAssignmentV2ForPatchBuilder":
        self._international_assignment_v2_for_patch.description = description
        return self

    def build(self) -> "InternationalAssignmentV2ForPatch":
        return self._international_assignment_v2_for_patch
