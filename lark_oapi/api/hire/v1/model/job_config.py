# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .interview_appointment_config import InterviewAppointmentConfig
from .job_config_interview_round_conf import JobConfigInterviewRoundConf
from .job_config_round_type import JobConfigRoundType


class JobConfig(object):
    _types = {
        "offer_apply_schema_id": str,
        "offer_process_conf": str,
        "recommended_evaluator_id_list": List[str],
        "update_option_list": List[int],
        "assessment_template_biz_id": str,
        "interview_round_conf_list": List[JobConfigInterviewRoundConf],
        "jr_id_list": List[str],
        "interview_registration_schema_id": str,
        "onboard_registration_schema_id": str,
        "interview_round_type_conf_list": List[JobConfigRoundType],
        "related_job_id_list": List[str],
        "interview_appointment_config": InterviewAppointmentConfig,
    }

    def __init__(self, d=None):
        self.offer_apply_schema_id: Optional[str] = None
        self.offer_process_conf: Optional[str] = None
        self.recommended_evaluator_id_list: Optional[List[str]] = None
        self.update_option_list: Optional[List[int]] = None
        self.assessment_template_biz_id: Optional[str] = None
        self.interview_round_conf_list: Optional[List[JobConfigInterviewRoundConf]] = None
        self.jr_id_list: Optional[List[str]] = None
        self.interview_registration_schema_id: Optional[str] = None
        self.onboard_registration_schema_id: Optional[str] = None
        self.interview_round_type_conf_list: Optional[List[JobConfigRoundType]] = None
        self.related_job_id_list: Optional[List[str]] = None
        self.interview_appointment_config: Optional[InterviewAppointmentConfig] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "JobConfigBuilder":
        return JobConfigBuilder()


class JobConfigBuilder(object):
    def __init__(self) -> None:
        self._job_config = JobConfig()

    def offer_apply_schema_id(self, offer_apply_schema_id: str) -> "JobConfigBuilder":
        self._job_config.offer_apply_schema_id = offer_apply_schema_id
        return self

    def offer_process_conf(self, offer_process_conf: str) -> "JobConfigBuilder":
        self._job_config.offer_process_conf = offer_process_conf
        return self

    def recommended_evaluator_id_list(self, recommended_evaluator_id_list: List[str]) -> "JobConfigBuilder":
        self._job_config.recommended_evaluator_id_list = recommended_evaluator_id_list
        return self

    def update_option_list(self, update_option_list: List[int]) -> "JobConfigBuilder":
        self._job_config.update_option_list = update_option_list
        return self

    def assessment_template_biz_id(self, assessment_template_biz_id: str) -> "JobConfigBuilder":
        self._job_config.assessment_template_biz_id = assessment_template_biz_id
        return self

    def interview_round_conf_list(self,
                                  interview_round_conf_list: List[JobConfigInterviewRoundConf]) -> "JobConfigBuilder":
        self._job_config.interview_round_conf_list = interview_round_conf_list
        return self

    def jr_id_list(self, jr_id_list: List[str]) -> "JobConfigBuilder":
        self._job_config.jr_id_list = jr_id_list
        return self

    def interview_registration_schema_id(self, interview_registration_schema_id: str) -> "JobConfigBuilder":
        self._job_config.interview_registration_schema_id = interview_registration_schema_id
        return self

    def onboard_registration_schema_id(self, onboard_registration_schema_id: str) -> "JobConfigBuilder":
        self._job_config.onboard_registration_schema_id = onboard_registration_schema_id
        return self

    def interview_round_type_conf_list(self,
                                       interview_round_type_conf_list: List[JobConfigRoundType]) -> "JobConfigBuilder":
        self._job_config.interview_round_type_conf_list = interview_round_type_conf_list
        return self

    def related_job_id_list(self, related_job_id_list: List[str]) -> "JobConfigBuilder":
        self._job_config.related_job_id_list = related_job_id_list
        return self

    def interview_appointment_config(self,
                                     interview_appointment_config: InterviewAppointmentConfig) -> "JobConfigBuilder":
        self._job_config.interview_appointment_config = interview_appointment_config
        return self

    def build(self) -> "JobConfig":
        return self._job_config
