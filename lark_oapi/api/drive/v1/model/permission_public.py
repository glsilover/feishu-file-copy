# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class PermissionPublic(object):
    _types = {
        "external_access": bool,
        "security_entity": str,
        "comment_entity": str,
        "share_entity": str,
        "link_share_entity": str,
        "invite_external": bool,
        "lock_switch": bool,
    }

    def __init__(self, d=None):
        self.external_access: Optional[bool] = None
        self.security_entity: Optional[str] = None
        self.comment_entity: Optional[str] = None
        self.share_entity: Optional[str] = None
        self.link_share_entity: Optional[str] = None
        self.invite_external: Optional[bool] = None
        self.lock_switch: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "PermissionPublicBuilder":
        return PermissionPublicBuilder()


class PermissionPublicBuilder(object):
    def __init__(self) -> None:
        self._permission_public = PermissionPublic()

    def external_access(self, external_access: bool) -> "PermissionPublicBuilder":
        self._permission_public.external_access = external_access
        return self

    def security_entity(self, security_entity: str) -> "PermissionPublicBuilder":
        self._permission_public.security_entity = security_entity
        return self

    def comment_entity(self, comment_entity: str) -> "PermissionPublicBuilder":
        self._permission_public.comment_entity = comment_entity
        return self

    def share_entity(self, share_entity: str) -> "PermissionPublicBuilder":
        self._permission_public.share_entity = share_entity
        return self

    def link_share_entity(self, link_share_entity: str) -> "PermissionPublicBuilder":
        self._permission_public.link_share_entity = link_share_entity
        return self

    def invite_external(self, invite_external: bool) -> "PermissionPublicBuilder":
        self._permission_public.invite_external = invite_external
        return self

    def lock_switch(self, lock_switch: bool) -> "PermissionPublicBuilder":
        self._permission_public.lock_switch = lock_switch
        return self

    def build(self) -> "PermissionPublic":
        return self._permission_public