# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .attachment import Attachment
from .contract_company import ContractCompany
from .education import Education
from .emergency_contact import EmergencyContact
from .job import Job
from .job_level import JobLevel
from .manager import Manager
from .native_region import NativeRegion
from .work_experience import WorkExperience
from .work_location import WorkLocation


class SystemFields(object):
    _types = {
        "name": str,
        "en_name": str,
        "email": str,
        "mobile": str,
        "department_id": str,
        "manager": Manager,
        "job": Job,
        "job_level": JobLevel,
        "work_location": WorkLocation,
        "gender": int,
        "birthday": str,
        "native_region": NativeRegion,
        "ethnicity": int,
        "marital_status": int,
        "political_status": int,
        "entered_workforce_date": str,
        "id_type": int,
        "id_number": str,
        "hukou_type": int,
        "hukou_location": str,
        "bank_account_number": str,
        "bank_name": str,
        "social_security_account": str,
        "provident_fund_account": str,
        "employee_no": str,
        "employee_type": int,
        "status": int,
        "hire_date": str,
        "probation_months": float,
        "conversion_date": str,
        "application": int,
        "application_status": int,
        "last_day": str,
        "departure_type": int,
        "departure_reason": int,
        "departure_notes": str,
        "contract_company": ContractCompany,
        "contract_type": int,
        "contract_start_date": str,
        "contract_expiration_date": str,
        "contract_sign_times": int,
        "personal_email": str,
        "family_address": str,
        "primary_emergency_contact": EmergencyContact,
        "emergency_contact": List[EmergencyContact],
        "highest_level_of_edu": Education,
        "education": List[Education],
        "former_work_exp": WorkExperience,
        "work_exp": List[WorkExperience],
        "id_photo_po_side": List[Attachment],
        "id_photo_em_side": List[Attachment],
        "id_photo": List[Attachment],
        "diploma_photo": List[Attachment],
        "graduation_cert": List[Attachment],
        "cert_of_merit": List[Attachment],
        "offboarding_file": List[Attachment],
        "cancel_onboarding_reason": int,
        "cancel_onboarding_notes": str,
        "employee_form_status": int,
        "create_time": int,
        "update_time": int,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.en_name: Optional[str] = None
        self.email: Optional[str] = None
        self.mobile: Optional[str] = None
        self.department_id: Optional[str] = None
        self.manager: Optional[Manager] = None
        self.job: Optional[Job] = None
        self.job_level: Optional[JobLevel] = None
        self.work_location: Optional[WorkLocation] = None
        self.gender: Optional[int] = None
        self.birthday: Optional[str] = None
        self.native_region: Optional[NativeRegion] = None
        self.ethnicity: Optional[int] = None
        self.marital_status: Optional[int] = None
        self.political_status: Optional[int] = None
        self.entered_workforce_date: Optional[str] = None
        self.id_type: Optional[int] = None
        self.id_number: Optional[str] = None
        self.hukou_type: Optional[int] = None
        self.hukou_location: Optional[str] = None
        self.bank_account_number: Optional[str] = None
        self.bank_name: Optional[str] = None
        self.social_security_account: Optional[str] = None
        self.provident_fund_account: Optional[str] = None
        self.employee_no: Optional[str] = None
        self.employee_type: Optional[int] = None
        self.status: Optional[int] = None
        self.hire_date: Optional[str] = None
        self.probation_months: Optional[float] = None
        self.conversion_date: Optional[str] = None
        self.application: Optional[int] = None
        self.application_status: Optional[int] = None
        self.last_day: Optional[str] = None
        self.departure_type: Optional[int] = None
        self.departure_reason: Optional[int] = None
        self.departure_notes: Optional[str] = None
        self.contract_company: Optional[ContractCompany] = None
        self.contract_type: Optional[int] = None
        self.contract_start_date: Optional[str] = None
        self.contract_expiration_date: Optional[str] = None
        self.contract_sign_times: Optional[int] = None
        self.personal_email: Optional[str] = None
        self.family_address: Optional[str] = None
        self.primary_emergency_contact: Optional[EmergencyContact] = None
        self.emergency_contact: Optional[List[EmergencyContact]] = None
        self.highest_level_of_edu: Optional[Education] = None
        self.education: Optional[List[Education]] = None
        self.former_work_exp: Optional[WorkExperience] = None
        self.work_exp: Optional[List[WorkExperience]] = None
        self.id_photo_po_side: Optional[List[Attachment]] = None
        self.id_photo_em_side: Optional[List[Attachment]] = None
        self.id_photo: Optional[List[Attachment]] = None
        self.diploma_photo: Optional[List[Attachment]] = None
        self.graduation_cert: Optional[List[Attachment]] = None
        self.cert_of_merit: Optional[List[Attachment]] = None
        self.offboarding_file: Optional[List[Attachment]] = None
        self.cancel_onboarding_reason: Optional[int] = None
        self.cancel_onboarding_notes: Optional[str] = None
        self.employee_form_status: Optional[int] = None
        self.create_time: Optional[int] = None
        self.update_time: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "SystemFieldsBuilder":
        return SystemFieldsBuilder()


class SystemFieldsBuilder(object):
    def __init__(self) -> None:
        self._system_fields = SystemFields()

    def name(self, name: str) -> "SystemFieldsBuilder":
        self._system_fields.name = name
        return self

    def en_name(self, en_name: str) -> "SystemFieldsBuilder":
        self._system_fields.en_name = en_name
        return self

    def email(self, email: str) -> "SystemFieldsBuilder":
        self._system_fields.email = email
        return self

    def mobile(self, mobile: str) -> "SystemFieldsBuilder":
        self._system_fields.mobile = mobile
        return self

    def department_id(self, department_id: str) -> "SystemFieldsBuilder":
        self._system_fields.department_id = department_id
        return self

    def manager(self, manager: Manager) -> "SystemFieldsBuilder":
        self._system_fields.manager = manager
        return self

    def job(self, job: Job) -> "SystemFieldsBuilder":
        self._system_fields.job = job
        return self

    def job_level(self, job_level: JobLevel) -> "SystemFieldsBuilder":
        self._system_fields.job_level = job_level
        return self

    def work_location(self, work_location: WorkLocation) -> "SystemFieldsBuilder":
        self._system_fields.work_location = work_location
        return self

    def gender(self, gender: int) -> "SystemFieldsBuilder":
        self._system_fields.gender = gender
        return self

    def birthday(self, birthday: str) -> "SystemFieldsBuilder":
        self._system_fields.birthday = birthday
        return self

    def native_region(self, native_region: NativeRegion) -> "SystemFieldsBuilder":
        self._system_fields.native_region = native_region
        return self

    def ethnicity(self, ethnicity: int) -> "SystemFieldsBuilder":
        self._system_fields.ethnicity = ethnicity
        return self

    def marital_status(self, marital_status: int) -> "SystemFieldsBuilder":
        self._system_fields.marital_status = marital_status
        return self

    def political_status(self, political_status: int) -> "SystemFieldsBuilder":
        self._system_fields.political_status = political_status
        return self

    def entered_workforce_date(self, entered_workforce_date: str) -> "SystemFieldsBuilder":
        self._system_fields.entered_workforce_date = entered_workforce_date
        return self

    def id_type(self, id_type: int) -> "SystemFieldsBuilder":
        self._system_fields.id_type = id_type
        return self

    def id_number(self, id_number: str) -> "SystemFieldsBuilder":
        self._system_fields.id_number = id_number
        return self

    def hukou_type(self, hukou_type: int) -> "SystemFieldsBuilder":
        self._system_fields.hukou_type = hukou_type
        return self

    def hukou_location(self, hukou_location: str) -> "SystemFieldsBuilder":
        self._system_fields.hukou_location = hukou_location
        return self

    def bank_account_number(self, bank_account_number: str) -> "SystemFieldsBuilder":
        self._system_fields.bank_account_number = bank_account_number
        return self

    def bank_name(self, bank_name: str) -> "SystemFieldsBuilder":
        self._system_fields.bank_name = bank_name
        return self

    def social_security_account(self, social_security_account: str) -> "SystemFieldsBuilder":
        self._system_fields.social_security_account = social_security_account
        return self

    def provident_fund_account(self, provident_fund_account: str) -> "SystemFieldsBuilder":
        self._system_fields.provident_fund_account = provident_fund_account
        return self

    def employee_no(self, employee_no: str) -> "SystemFieldsBuilder":
        self._system_fields.employee_no = employee_no
        return self

    def employee_type(self, employee_type: int) -> "SystemFieldsBuilder":
        self._system_fields.employee_type = employee_type
        return self

    def status(self, status: int) -> "SystemFieldsBuilder":
        self._system_fields.status = status
        return self

    def hire_date(self, hire_date: str) -> "SystemFieldsBuilder":
        self._system_fields.hire_date = hire_date
        return self

    def probation_months(self, probation_months: float) -> "SystemFieldsBuilder":
        self._system_fields.probation_months = probation_months
        return self

    def conversion_date(self, conversion_date: str) -> "SystemFieldsBuilder":
        self._system_fields.conversion_date = conversion_date
        return self

    def application(self, application: int) -> "SystemFieldsBuilder":
        self._system_fields.application = application
        return self

    def application_status(self, application_status: int) -> "SystemFieldsBuilder":
        self._system_fields.application_status = application_status
        return self

    def last_day(self, last_day: str) -> "SystemFieldsBuilder":
        self._system_fields.last_day = last_day
        return self

    def departure_type(self, departure_type: int) -> "SystemFieldsBuilder":
        self._system_fields.departure_type = departure_type
        return self

    def departure_reason(self, departure_reason: int) -> "SystemFieldsBuilder":
        self._system_fields.departure_reason = departure_reason
        return self

    def departure_notes(self, departure_notes: str) -> "SystemFieldsBuilder":
        self._system_fields.departure_notes = departure_notes
        return self

    def contract_company(self, contract_company: ContractCompany) -> "SystemFieldsBuilder":
        self._system_fields.contract_company = contract_company
        return self

    def contract_type(self, contract_type: int) -> "SystemFieldsBuilder":
        self._system_fields.contract_type = contract_type
        return self

    def contract_start_date(self, contract_start_date: str) -> "SystemFieldsBuilder":
        self._system_fields.contract_start_date = contract_start_date
        return self

    def contract_expiration_date(self, contract_expiration_date: str) -> "SystemFieldsBuilder":
        self._system_fields.contract_expiration_date = contract_expiration_date
        return self

    def contract_sign_times(self, contract_sign_times: int) -> "SystemFieldsBuilder":
        self._system_fields.contract_sign_times = contract_sign_times
        return self

    def personal_email(self, personal_email: str) -> "SystemFieldsBuilder":
        self._system_fields.personal_email = personal_email
        return self

    def family_address(self, family_address: str) -> "SystemFieldsBuilder":
        self._system_fields.family_address = family_address
        return self

    def primary_emergency_contact(self, primary_emergency_contact: EmergencyContact) -> "SystemFieldsBuilder":
        self._system_fields.primary_emergency_contact = primary_emergency_contact
        return self

    def emergency_contact(self, emergency_contact: List[EmergencyContact]) -> "SystemFieldsBuilder":
        self._system_fields.emergency_contact = emergency_contact
        return self

    def highest_level_of_edu(self, highest_level_of_edu: Education) -> "SystemFieldsBuilder":
        self._system_fields.highest_level_of_edu = highest_level_of_edu
        return self

    def education(self, education: List[Education]) -> "SystemFieldsBuilder":
        self._system_fields.education = education
        return self

    def former_work_exp(self, former_work_exp: WorkExperience) -> "SystemFieldsBuilder":
        self._system_fields.former_work_exp = former_work_exp
        return self

    def work_exp(self, work_exp: List[WorkExperience]) -> "SystemFieldsBuilder":
        self._system_fields.work_exp = work_exp
        return self

    def id_photo_po_side(self, id_photo_po_side: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.id_photo_po_side = id_photo_po_side
        return self

    def id_photo_em_side(self, id_photo_em_side: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.id_photo_em_side = id_photo_em_side
        return self

    def id_photo(self, id_photo: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.id_photo = id_photo
        return self

    def diploma_photo(self, diploma_photo: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.diploma_photo = diploma_photo
        return self

    def graduation_cert(self, graduation_cert: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.graduation_cert = graduation_cert
        return self

    def cert_of_merit(self, cert_of_merit: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.cert_of_merit = cert_of_merit
        return self

    def offboarding_file(self, offboarding_file: List[Attachment]) -> "SystemFieldsBuilder":
        self._system_fields.offboarding_file = offboarding_file
        return self

    def cancel_onboarding_reason(self, cancel_onboarding_reason: int) -> "SystemFieldsBuilder":
        self._system_fields.cancel_onboarding_reason = cancel_onboarding_reason
        return self

    def cancel_onboarding_notes(self, cancel_onboarding_notes: str) -> "SystemFieldsBuilder":
        self._system_fields.cancel_onboarding_notes = cancel_onboarding_notes
        return self

    def employee_form_status(self, employee_form_status: int) -> "SystemFieldsBuilder":
        self._system_fields.employee_form_status = employee_form_status
        return self

    def create_time(self, create_time: int) -> "SystemFieldsBuilder":
        self._system_fields.create_time = create_time
        return self

    def update_time(self, update_time: int) -> "SystemFieldsBuilder":
        self._system_fields.update_time = update_time
        return self

    def build(self) -> "SystemFields":
        return self._system_fields
