# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class EmployeeDateType(object):
    _types = {
        "date": str,
        "date_type": int,
    }

    def __init__(self, d=None):
        self.date: Optional[str] = None
        self.date_type: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "EmployeeDateTypeBuilder":
        return EmployeeDateTypeBuilder()


class EmployeeDateTypeBuilder(object):
    def __init__(self) -> None:
        self._employee_date_type = EmployeeDateType()

    def date(self, date: str) -> "EmployeeDateTypeBuilder":
        self._employee_date_type.date = date
        return self

    def date_type(self, date_type: int) -> "EmployeeDateTypeBuilder":
        self._employee_date_type.date_type = date_type
        return self

    def build(self) -> "EmployeeDateType":
        return self._employee_date_type