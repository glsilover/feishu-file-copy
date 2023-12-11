# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .conditions import Conditions
from .options import Options


class CustomList(object):
    _types = {
        "custom_type": int,
        "key": str,
        "need_fill": bool,
        "title": str,
        "placeholder": str,
        "options": List[Options],
        "conditions": List[Conditions],
    }

    def __init__(self, d=None):
        self.custom_type: Optional[int] = None
        self.key: Optional[str] = None
        self.need_fill: Optional[bool] = None
        self.title: Optional[str] = None
        self.placeholder: Optional[str] = None
        self.options: Optional[List[Options]] = None
        self.conditions: Optional[List[Conditions]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CustomListBuilder":
        return CustomListBuilder()


class CustomListBuilder(object):
    def __init__(self) -> None:
        self._custom_list = CustomList()

    def custom_type(self, custom_type: int) -> "CustomListBuilder":
        self._custom_list.custom_type = custom_type
        return self

    def key(self, key: str) -> "CustomListBuilder":
        self._custom_list.key = key
        return self

    def need_fill(self, need_fill: bool) -> "CustomListBuilder":
        self._custom_list.need_fill = need_fill
        return self

    def title(self, title: str) -> "CustomListBuilder":
        self._custom_list.title = title
        return self

    def placeholder(self, placeholder: str) -> "CustomListBuilder":
        self._custom_list.placeholder = placeholder
        return self

    def options(self, options: List[Options]) -> "CustomListBuilder":
        self._custom_list.options = options
        return self

    def conditions(self, conditions: List[Conditions]) -> "CustomListBuilder":
        self._custom_list.conditions = conditions
        return self

    def build(self) -> "CustomList":
        return self._custom_list