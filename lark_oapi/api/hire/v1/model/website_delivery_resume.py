# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .website_delivery_award import WebsiteDeliveryAward
from .website_delivery_basic_info import WebsiteDeliveryBasicInfo
from .website_delivery_career import WebsiteDeliveryCareer
from .website_delivery_customized_data_parent import WebsiteDeliveryCustomizedDataParent
from .website_delivery_education import WebsiteDeliveryEducation
from .website_delivery_internship import WebsiteDeliveryInternship
from .website_delivery_language import WebsiteDeliveryLanguage
from .website_delivery_project import WebsiteDeliveryProject
from .website_delivery_self_evaluation import WebsiteDeliverySelfEvaluation
from .website_delivery_sns import WebsiteDeliverySns
from .website_delivery_works import WebsiteDeliveryWorks


class WebsiteDeliveryResume(object):
    _types = {
        "internship_list": List[WebsiteDeliveryInternship],
        "basic_info": WebsiteDeliveryBasicInfo,
        "education_list": List[WebsiteDeliveryEducation],
        "self_evaluation": WebsiteDeliverySelfEvaluation,
        "career_list": List[WebsiteDeliveryCareer],
        "customized_data": List[WebsiteDeliveryCustomizedDataParent],
        "resume_attachment_id": str,
        "sns_list": List[WebsiteDeliverySns],
        "works_list": List[WebsiteDeliveryWorks],
        "award_list": List[WebsiteDeliveryAward],
        "project_list": List[WebsiteDeliveryProject],
        "language_list": List[WebsiteDeliveryLanguage],
    }

    def __init__(self, d=None):
        self.internship_list: Optional[List[WebsiteDeliveryInternship]] = None
        self.basic_info: Optional[WebsiteDeliveryBasicInfo] = None
        self.education_list: Optional[List[WebsiteDeliveryEducation]] = None
        self.self_evaluation: Optional[WebsiteDeliverySelfEvaluation] = None
        self.career_list: Optional[List[WebsiteDeliveryCareer]] = None
        self.customized_data: Optional[List[WebsiteDeliveryCustomizedDataParent]] = None
        self.resume_attachment_id: Optional[str] = None
        self.sns_list: Optional[List[WebsiteDeliverySns]] = None
        self.works_list: Optional[List[WebsiteDeliveryWorks]] = None
        self.award_list: Optional[List[WebsiteDeliveryAward]] = None
        self.project_list: Optional[List[WebsiteDeliveryProject]] = None
        self.language_list: Optional[List[WebsiteDeliveryLanguage]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "WebsiteDeliveryResumeBuilder":
        return WebsiteDeliveryResumeBuilder()


class WebsiteDeliveryResumeBuilder(object):
    def __init__(self) -> None:
        self._website_delivery_resume = WebsiteDeliveryResume()

    def internship_list(self, internship_list: List[WebsiteDeliveryInternship]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.internship_list = internship_list
        return self

    def basic_info(self, basic_info: WebsiteDeliveryBasicInfo) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.basic_info = basic_info
        return self

    def education_list(self, education_list: List[WebsiteDeliveryEducation]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.education_list = education_list
        return self

    def self_evaluation(self, self_evaluation: WebsiteDeliverySelfEvaluation) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.self_evaluation = self_evaluation
        return self

    def career_list(self, career_list: List[WebsiteDeliveryCareer]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.career_list = career_list
        return self

    def customized_data(self,
                        customized_data: List[WebsiteDeliveryCustomizedDataParent]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.customized_data = customized_data
        return self

    def resume_attachment_id(self, resume_attachment_id: str) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.resume_attachment_id = resume_attachment_id
        return self

    def sns_list(self, sns_list: List[WebsiteDeliverySns]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.sns_list = sns_list
        return self

    def works_list(self, works_list: List[WebsiteDeliveryWorks]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.works_list = works_list
        return self

    def award_list(self, award_list: List[WebsiteDeliveryAward]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.award_list = award_list
        return self

    def project_list(self, project_list: List[WebsiteDeliveryProject]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.project_list = project_list
        return self

    def language_list(self, language_list: List[WebsiteDeliveryLanguage]) -> "WebsiteDeliveryResumeBuilder":
        self._website_delivery_resume.language_list = language_list
        return self

    def build(self) -> "WebsiteDeliveryResume":
        return self._website_delivery_resume
