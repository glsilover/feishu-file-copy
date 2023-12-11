# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class Collaborator(object):
    _types = {
        "member_type": str,
        "member_open_id": str,
        "member_user_id": str,
        "perm": str,
    }

    def __init__(self, d=None):
        self.member_type: Optional[str] = None
        self.member_open_id: Optional[str] = None
        self.member_user_id: Optional[str] = None
        self.perm: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "CollaboratorBuilder":
        return CollaboratorBuilder()


class CollaboratorBuilder(object):
    def __init__(self) -> None:
        self._collaborator = Collaborator()

    def member_type(self, member_type: str) -> "CollaboratorBuilder":
        self._collaborator.member_type = member_type
        return self

    def member_open_id(self, member_open_id: str) -> "CollaboratorBuilder":
        self._collaborator.member_open_id = member_open_id
        return self

    def member_user_id(self, member_user_id: str) -> "CollaboratorBuilder":
        self._collaborator.member_user_id = member_user_id
        return self

    def perm(self, perm: str) -> "CollaboratorBuilder":
        self._collaborator.perm = perm
        return self

    def build(self) -> "Collaborator":
        return self._collaborator