# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class Undefined(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "UndefinedBuilder":
        return UndefinedBuilder()


class UndefinedBuilder(object):
    def __init__(self) -> None:
        self._undefined = Undefined()

    def build(self) -> "Undefined":
        return self._undefined
