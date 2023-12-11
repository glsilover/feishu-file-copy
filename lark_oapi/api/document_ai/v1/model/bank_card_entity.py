# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class BankCardEntity(object):
    _types = {
        "type": str,
        "value": str,
    }

    def __init__(self, d=None):
        self.type: Optional[str] = None
        self.value: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BankCardEntityBuilder":
        return BankCardEntityBuilder()


class BankCardEntityBuilder(object):
    def __init__(self) -> None:
        self._bank_card_entity = BankCardEntity()

    def type(self, type: str) -> "BankCardEntityBuilder":
        self._bank_card_entity.type = type
        return self

    def value(self, value: str) -> "BankCardEntityBuilder":
        self._bank_card_entity.value = value
        return self

    def build(self) -> "BankCardEntity":
        return self._bank_card_entity
