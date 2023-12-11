# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.core.model import BaseResponse
from .list_department_unit_response_body import ListDepartmentUnitResponseBody


class ListDepartmentUnitResponse(BaseResponse):
    _types = {
        "data": ListDepartmentUnitResponseBody
    }

    def __init__(self, d=None):
        super().__init__(d)
        self.data: Optional[ListDepartmentUnitResponseBody] = None
        init(self, d, self._types)
