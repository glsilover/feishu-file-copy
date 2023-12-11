# Code generated by Lark OpenAPI.

from lark_oapi.core.construct import init


class DocDivider(object):
    _types = {
    }

    def __init__(self, d=None):
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DocDividerBuilder":
        return DocDividerBuilder()


class DocDividerBuilder(object):
    def __init__(self) -> None:
        self._doc_divider = DocDivider()

    def build(self) -> "DocDivider":
        return self._doc_divider
