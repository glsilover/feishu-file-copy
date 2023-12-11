# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .object_field_data import ObjectFieldData
from .previous_employer import PreviousEmployer


class PersonInfoMys(object):
    _types = {
        "id": str,
        "person_id": str,
        "previous_income_in_the_current_year": bool,
        "fresh_graduate": bool,
        "previous_employers_list": List[PreviousEmployer],
        "monthly_gross": str,
        "tax_relief_1": str,
        "tax_relief_2": str,
        "tax_relief_3": str,
        "tax_relief_4": str,
        "tax_relief_5": str,
        "common_reserve_fund": str,
        "monthly_tax_deduction": str,
        "social_insurance": str,
        "custom_fields": List[ObjectFieldData],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.person_id: Optional[str] = None
        self.previous_income_in_the_current_year: Optional[bool] = None
        self.fresh_graduate: Optional[bool] = None
        self.previous_employers_list: Optional[List[PreviousEmployer]] = None
        self.monthly_gross: Optional[str] = None
        self.tax_relief_1: Optional[str] = None
        self.tax_relief_2: Optional[str] = None
        self.tax_relief_3: Optional[str] = None
        self.tax_relief_4: Optional[str] = None
        self.tax_relief_5: Optional[str] = None
        self.common_reserve_fund: Optional[str] = None
        self.monthly_tax_deduction: Optional[str] = None
        self.social_insurance: Optional[str] = None
        self.custom_fields: Optional[List[ObjectFieldData]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PersonInfoMysBuilder":
        return PersonInfoMysBuilder()


class PersonInfoMysBuilder(object):
    def __init__(self) -> None:
        self._person_info_mys = PersonInfoMys()

    def id(self, id: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.id = id
        return self

    def person_id(self, person_id: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.person_id = person_id
        return self

    def previous_income_in_the_current_year(self, previous_income_in_the_current_year: bool) -> "PersonInfoMysBuilder":
        self._person_info_mys.previous_income_in_the_current_year = previous_income_in_the_current_year
        return self

    def fresh_graduate(self, fresh_graduate: bool) -> "PersonInfoMysBuilder":
        self._person_info_mys.fresh_graduate = fresh_graduate
        return self

    def previous_employers_list(self, previous_employers_list: List[PreviousEmployer]) -> "PersonInfoMysBuilder":
        self._person_info_mys.previous_employers_list = previous_employers_list
        return self

    def monthly_gross(self, monthly_gross: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.monthly_gross = monthly_gross
        return self

    def tax_relief_1(self, tax_relief_1: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.tax_relief_1 = tax_relief_1
        return self

    def tax_relief_2(self, tax_relief_2: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.tax_relief_2 = tax_relief_2
        return self

    def tax_relief_3(self, tax_relief_3: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.tax_relief_3 = tax_relief_3
        return self

    def tax_relief_4(self, tax_relief_4: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.tax_relief_4 = tax_relief_4
        return self

    def tax_relief_5(self, tax_relief_5: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.tax_relief_5 = tax_relief_5
        return self

    def common_reserve_fund(self, common_reserve_fund: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.common_reserve_fund = common_reserve_fund
        return self

    def monthly_tax_deduction(self, monthly_tax_deduction: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.monthly_tax_deduction = monthly_tax_deduction
        return self

    def social_insurance(self, social_insurance: str) -> "PersonInfoMysBuilder":
        self._person_info_mys.social_insurance = social_insurance
        return self

    def custom_fields(self, custom_fields: List[ObjectFieldData]) -> "PersonInfoMysBuilder":
        self._person_info_mys.custom_fields = custom_fields
        return self

    def build(self) -> "PersonInfoMys":
        return self._person_info_mys
