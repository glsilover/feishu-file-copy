# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .custom_field_data import CustomFieldData
from .enum import Enum


class ProbationInfoForSubmit(object):
    _types = {
        "employment_id": str,
        "probation_id": str,
        "probation_start_date": str,
        "probation_expected_end_date": str,
        "actual_probation_end_date": str,
        "initiating_time": str,
        "submission_type": Enum,
        "initiator_id": str,
        "probation_status": Enum,
        "self_review": str,
        "notes": str,
        "process_id": str,
        "converted_via_bpm": bool,
        "custom_fields": List[CustomFieldData],
        "final_assessment_status": Enum,
        "final_assessment_result": Enum,
        "final_assessment_score": float,
        "final_assessment_grade": Enum,
        "final_assessment_comment": str,
        "final_assessment_detail": str,
    }

    def __init__(self, d=None):
        self.employment_id: Optional[str] = None
        self.probation_id: Optional[str] = None
        self.probation_start_date: Optional[str] = None
        self.probation_expected_end_date: Optional[str] = None
        self.actual_probation_end_date: Optional[str] = None
        self.initiating_time: Optional[str] = None
        self.submission_type: Optional[Enum] = None
        self.initiator_id: Optional[str] = None
        self.probation_status: Optional[Enum] = None
        self.self_review: Optional[str] = None
        self.notes: Optional[str] = None
        self.process_id: Optional[str] = None
        self.converted_via_bpm: Optional[bool] = None
        self.custom_fields: Optional[List[CustomFieldData]] = None
        self.final_assessment_status: Optional[Enum] = None
        self.final_assessment_result: Optional[Enum] = None
        self.final_assessment_score: Optional[float] = None
        self.final_assessment_grade: Optional[Enum] = None
        self.final_assessment_comment: Optional[str] = None
        self.final_assessment_detail: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "ProbationInfoForSubmitBuilder":
        return ProbationInfoForSubmitBuilder()


class ProbationInfoForSubmitBuilder(object):
    def __init__(self) -> None:
        self._probation_info_for_submit = ProbationInfoForSubmit()

    def employment_id(self, employment_id: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.employment_id = employment_id
        return self

    def probation_id(self, probation_id: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.probation_id = probation_id
        return self

    def probation_start_date(self, probation_start_date: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.probation_start_date = probation_start_date
        return self

    def probation_expected_end_date(self, probation_expected_end_date: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.probation_expected_end_date = probation_expected_end_date
        return self

    def actual_probation_end_date(self, actual_probation_end_date: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.actual_probation_end_date = actual_probation_end_date
        return self

    def initiating_time(self, initiating_time: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.initiating_time = initiating_time
        return self

    def submission_type(self, submission_type: Enum) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.submission_type = submission_type
        return self

    def initiator_id(self, initiator_id: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.initiator_id = initiator_id
        return self

    def probation_status(self, probation_status: Enum) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.probation_status = probation_status
        return self

    def self_review(self, self_review: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.self_review = self_review
        return self

    def notes(self, notes: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.notes = notes
        return self

    def process_id(self, process_id: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.process_id = process_id
        return self

    def converted_via_bpm(self, converted_via_bpm: bool) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.converted_via_bpm = converted_via_bpm
        return self

    def custom_fields(self, custom_fields: List[CustomFieldData]) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.custom_fields = custom_fields
        return self

    def final_assessment_status(self, final_assessment_status: Enum) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_status = final_assessment_status
        return self

    def final_assessment_result(self, final_assessment_result: Enum) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_result = final_assessment_result
        return self

    def final_assessment_score(self, final_assessment_score: float) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_score = final_assessment_score
        return self

    def final_assessment_grade(self, final_assessment_grade: Enum) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_grade = final_assessment_grade
        return self

    def final_assessment_comment(self, final_assessment_comment: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_comment = final_assessment_comment
        return self

    def final_assessment_detail(self, final_assessment_detail: str) -> "ProbationInfoForSubmitBuilder":
        self._probation_info_for_submit.final_assessment_detail = final_assessment_detail
        return self

    def build(self) -> "ProbationInfoForSubmit":
        return self._probation_info_for_submit