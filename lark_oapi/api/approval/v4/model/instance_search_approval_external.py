# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class InstanceSearchApprovalExternal(object):
    _types = {
        "batch_cc_read": bool,
    }

    def __init__(self, d=None):
        self.batch_cc_read: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "InstanceSearchApprovalExternalBuilder":
        return InstanceSearchApprovalExternalBuilder()


class InstanceSearchApprovalExternalBuilder(object):
    def __init__(self) -> None:
        self._instance_search_approval_external = InstanceSearchApprovalExternal()

    def batch_cc_read(self, batch_cc_read: bool) -> "InstanceSearchApprovalExternalBuilder":
        self._instance_search_approval_external.batch_cc_read = batch_cc_read
        return self

    def build(self) -> "InstanceSearchApprovalExternal":
        return self._instance_search_approval_external