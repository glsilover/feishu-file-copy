# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .appendix import Appendix
from .extend_field import ExtendField
from .legal_entity_bank import LegalEntityBank


class LegalEntity(object):
    _types = {
        "id": int,
        "legal_entity": str,
        "legal_entity_text": str,
        "short_text": str,
        "certification_type": str,
        "certification_id": str,
        "legal_person": str,
        "country": str,
        "province": str,
        "city": str,
        "address": str,
        "taxpayer_type": str,
        "telephone": str,
        "bank_id": str,
        "bank_name": str,
        "bank_account": str,
        "status": int,
        "legal_entity_banks": List[LegalEntityBank],
        "extend_info": List[ExtendField],
        "appendix": List[Appendix],
    }

    def __init__(self, d=None):
        self.id: Optional[int] = None
        self.legal_entity: Optional[str] = None
        self.legal_entity_text: Optional[str] = None
        self.short_text: Optional[str] = None
        self.certification_type: Optional[str] = None
        self.certification_id: Optional[str] = None
        self.legal_person: Optional[str] = None
        self.country: Optional[str] = None
        self.province: Optional[str] = None
        self.city: Optional[str] = None
        self.address: Optional[str] = None
        self.taxpayer_type: Optional[str] = None
        self.telephone: Optional[str] = None
        self.bank_id: Optional[str] = None
        self.bank_name: Optional[str] = None
        self.bank_account: Optional[str] = None
        self.status: Optional[int] = None
        self.legal_entity_banks: Optional[List[LegalEntityBank]] = None
        self.extend_info: Optional[List[ExtendField]] = None
        self.appendix: Optional[List[Appendix]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "LegalEntityBuilder":
        return LegalEntityBuilder()


class LegalEntityBuilder(object):
    def __init__(self) -> None:
        self._legal_entity = LegalEntity()

    def id(self, id: int) -> "LegalEntityBuilder":
        self._legal_entity.id = id
        return self

    def legal_entity(self, legal_entity: str) -> "LegalEntityBuilder":
        self._legal_entity.legal_entity = legal_entity
        return self

    def legal_entity_text(self, legal_entity_text: str) -> "LegalEntityBuilder":
        self._legal_entity.legal_entity_text = legal_entity_text
        return self

    def short_text(self, short_text: str) -> "LegalEntityBuilder":
        self._legal_entity.short_text = short_text
        return self

    def certification_type(self, certification_type: str) -> "LegalEntityBuilder":
        self._legal_entity.certification_type = certification_type
        return self

    def certification_id(self, certification_id: str) -> "LegalEntityBuilder":
        self._legal_entity.certification_id = certification_id
        return self

    def legal_person(self, legal_person: str) -> "LegalEntityBuilder":
        self._legal_entity.legal_person = legal_person
        return self

    def country(self, country: str) -> "LegalEntityBuilder":
        self._legal_entity.country = country
        return self

    def province(self, province: str) -> "LegalEntityBuilder":
        self._legal_entity.province = province
        return self

    def city(self, city: str) -> "LegalEntityBuilder":
        self._legal_entity.city = city
        return self

    def address(self, address: str) -> "LegalEntityBuilder":
        self._legal_entity.address = address
        return self

    def taxpayer_type(self, taxpayer_type: str) -> "LegalEntityBuilder":
        self._legal_entity.taxpayer_type = taxpayer_type
        return self

    def telephone(self, telephone: str) -> "LegalEntityBuilder":
        self._legal_entity.telephone = telephone
        return self

    def bank_id(self, bank_id: str) -> "LegalEntityBuilder":
        self._legal_entity.bank_id = bank_id
        return self

    def bank_name(self, bank_name: str) -> "LegalEntityBuilder":
        self._legal_entity.bank_name = bank_name
        return self

    def bank_account(self, bank_account: str) -> "LegalEntityBuilder":
        self._legal_entity.bank_account = bank_account
        return self

    def status(self, status: int) -> "LegalEntityBuilder":
        self._legal_entity.status = status
        return self

    def legal_entity_banks(self, legal_entity_banks: List[LegalEntityBank]) -> "LegalEntityBuilder":
        self._legal_entity.legal_entity_banks = legal_entity_banks
        return self

    def extend_info(self, extend_info: List[ExtendField]) -> "LegalEntityBuilder":
        self._legal_entity.extend_info = extend_info
        return self

    def appendix(self, appendix: List[Appendix]) -> "LegalEntityBuilder":
        self._legal_entity.appendix = appendix
        return self

    def build(self) -> "LegalEntity":
        return self._legal_entity
