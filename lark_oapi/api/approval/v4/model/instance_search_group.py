# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class InstanceSearchGroup(object):
    _types = {
        "external_id": str,
        "name": str,
    }

    def __init__(self, d=None):
        self.external_id: Optional[str] = None
        self.name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceSearchGroupBuilder":
        return InstanceSearchGroupBuilder()


class InstanceSearchGroupBuilder(object):
    def __init__(self) -> None:
        self._instance_search_group = InstanceSearchGroup()

    def external_id(self, external_id: str) -> "InstanceSearchGroupBuilder":
        self._instance_search_group.external_id = external_id
        return self

    def name(self, name: str) -> "InstanceSearchGroupBuilder":
        self._instance_search_group.name = name
        return self

    def build(self) -> "InstanceSearchGroup":
        return self._instance_search_group