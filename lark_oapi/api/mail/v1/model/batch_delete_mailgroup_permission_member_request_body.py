# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init


class BatchDeleteMailgroupPermissionMemberRequestBody(object):
    _types = {
        "permission_member_id_list": List[str],
    }

    def __init__(self, d=None):
        self.permission_member_id_list: Optional[List[str]] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "BatchDeleteMailgroupPermissionMemberRequestBodyBuilder":
        return BatchDeleteMailgroupPermissionMemberRequestBodyBuilder()


class BatchDeleteMailgroupPermissionMemberRequestBodyBuilder(object):
    def __init__(self) -> None:
        self._batch_delete_mailgroup_permission_member_request_body = BatchDeleteMailgroupPermissionMemberRequestBody()

    def permission_member_id_list(self, permission_member_id_list: List[
        str]) -> "BatchDeleteMailgroupPermissionMemberRequestBodyBuilder":
        self._batch_delete_mailgroup_permission_member_request_body.permission_member_id_list = permission_member_id_list
        return self

    def build(self) -> "BatchDeleteMailgroupPermissionMemberRequestBody":
        return self._batch_delete_mailgroup_permission_member_request_body