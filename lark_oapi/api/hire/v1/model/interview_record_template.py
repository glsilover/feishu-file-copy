# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .interview_assessment_template import InterviewAssessmentTemplate


class InterviewRecordTemplate(object):
    _types = {
        "assessment_template": InterviewAssessmentTemplate,
    }

    def __init__(self, d=None):
        self.assessment_template: Optional[InterviewAssessmentTemplate] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InterviewRecordTemplateBuilder":
        return InterviewRecordTemplateBuilder()


class InterviewRecordTemplateBuilder(object):
    def __init__(self) -> None:
        self._interview_record_template = InterviewRecordTemplate()

    def assessment_template(self, assessment_template: InterviewAssessmentTemplate) -> "InterviewRecordTemplateBuilder":
        self._interview_record_template.assessment_template = assessment_template
        return self

    def build(self) -> "InterviewRecordTemplate":
        return self._interview_record_template