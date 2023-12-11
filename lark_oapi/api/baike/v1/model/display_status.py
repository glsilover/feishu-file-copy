# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init


class DisplayStatus(object):
    _types = {
        "allow_highlight": bool,
        "allow_search": bool,
    }

    def __init__(self, d=None):
        self.allow_highlight: Optional[bool] = None
        self.allow_search: Optional[bool] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "DisplayStatusBuilder":
        return DisplayStatusBuilder()


class DisplayStatusBuilder(object):
    def __init__(self) -> None:
        self._display_status = DisplayStatus()

    def allow_highlight(self, allow_highlight: bool) -> "DisplayStatusBuilder":
        self._display_status.allow_highlight = allow_highlight
        return self

    def allow_search(self, allow_search: bool) -> "DisplayStatusBuilder":
        self._display_status.allow_search = allow_search
        return self

    def build(self) -> "DisplayStatus":
        return self._display_status
