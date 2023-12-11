# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .appli_offer_basic_cust_obj_op_v import AppliOfferBasicCustObjOpV
from .offer_schema_name import OfferSchemaName


class AppliOfferBasicCustObj(object):
    _types = {
        "id": str,
        "name": OfferSchemaName,
        "type": str,
        "value": str,
        "option_value_list": List[AppliOfferBasicCustObjOpV],
    }

    def __init__(self, d=None):
        self.id: Optional[str] = None
        self.name: Optional[OfferSchemaName] = None
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        self.option_value_list: Optional[List[AppliOfferBasicCustObjOpV]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppliOfferBasicCustObjBuilder":
        return AppliOfferBasicCustObjBuilder()


class AppliOfferBasicCustObjBuilder(object):
    def __init__(self) -> None:
        self._appli_offer_basic_cust_obj = AppliOfferBasicCustObj()

    def id(self, id: str) -> "AppliOfferBasicCustObjBuilder":
        self._appli_offer_basic_cust_obj.id = id
        return self

    def name(self, name: OfferSchemaName) -> "AppliOfferBasicCustObjBuilder":
        self._appli_offer_basic_cust_obj.name = name
        return self

    def type(self, type: str) -> "AppliOfferBasicCustObjBuilder":
        self._appli_offer_basic_cust_obj.type = type
        return self

    def value(self, value: str) -> "AppliOfferBasicCustObjBuilder":
        self._appli_offer_basic_cust_obj.value = value
        return self

    def option_value_list(self, option_value_list: List[AppliOfferBasicCustObjOpV]) -> "AppliOfferBasicCustObjBuilder":
        self._appli_offer_basic_cust_obj.option_value_list = option_value_list
        return self

    def build(self) -> "AppliOfferBasicCustObj":
        return self._appli_offer_basic_cust_obj
