# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .person_info import PersonInfo
from .pre_hire_contract_info import PreHireContractInfo
from .pre_hire_employment_info import PreHireEmploymentInfo
from .pre_hire_onboarding_info import PreHireOnboardingInfo
from .pre_hire_probation_info import PreHireProbationInfo


class PreHire(object):
    _types = {
        "person_info": PersonInfo,
        "employment_info": PreHireEmploymentInfo,
        "onboarding_info": PreHireOnboardingInfo,
        "probation_info": PreHireProbationInfo,
        "contract_info": PreHireContractInfo,
        "pre_hire_id": str,
    }

    def __init__(self, d=None):
        self.person_info: Optional[PersonInfo] = None
        self.employment_info: Optional[PreHireEmploymentInfo] = None
        self.onboarding_info: Optional[PreHireOnboardingInfo] = None
        self.probation_info: Optional[PreHireProbationInfo] = None
        self.contract_info: Optional[PreHireContractInfo] = None
        self.pre_hire_id: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PreHireBuilder":
        return PreHireBuilder()


class PreHireBuilder(object):
    def __init__(self) -> None:
        self._pre_hire = PreHire()

    def person_info(self, person_info: PersonInfo) -> "PreHireBuilder":
        self._pre_hire.person_info = person_info
        return self

    def employment_info(self, employment_info: PreHireEmploymentInfo) -> "PreHireBuilder":
        self._pre_hire.employment_info = employment_info
        return self

    def onboarding_info(self, onboarding_info: PreHireOnboardingInfo) -> "PreHireBuilder":
        self._pre_hire.onboarding_info = onboarding_info
        return self

    def probation_info(self, probation_info: PreHireProbationInfo) -> "PreHireBuilder":
        self._pre_hire.probation_info = probation_info
        return self

    def contract_info(self, contract_info: PreHireContractInfo) -> "PreHireBuilder":
        self._pre_hire.contract_info = contract_info
        return self

    def pre_hire_id(self, pre_hire_id: str) -> "PreHireBuilder":
        self._pre_hire.pre_hire_id = pre_hire_id
        return self

    def build(self) -> "PreHire":
        return self._pre_hire