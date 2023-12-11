# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class UserContactInfo(object):
    _types = {
        "name": str,
        "mobile": str,
        "email": str,
        "first_name": str,
        "last_name": str,
    }

    def __init__(self, d=None):
        self.name: Optional[str] = None
        self.mobile: Optional[str] = None
        self.email: Optional[str] = None
        self.first_name: Optional[str] = None
        self.last_name: Optional[str] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UserContactInfoBuilder":
        return UserContactInfoBuilder()


class UserContactInfoBuilder(object):
    def __init__(self) -> None:
        self._user_contact_info = UserContactInfo()

    def name(self, name: str) -> "UserContactInfoBuilder":
        self._user_contact_info.name = name
        return self

    def mobile(self, mobile: str) -> "UserContactInfoBuilder":
        self._user_contact_info.mobile = mobile
        return self

    def email(self, email: str) -> "UserContactInfoBuilder":
        self._user_contact_info.email = email
        return self

    def first_name(self, first_name: str) -> "UserContactInfoBuilder":
        self._user_contact_info.first_name = first_name
        return self

    def last_name(self, last_name: str) -> "UserContactInfoBuilder":
        self._user_contact_info.last_name = last_name
        return self

    def build(self) -> "UserContactInfo":
        return self._user_contact_info
