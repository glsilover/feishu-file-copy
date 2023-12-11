# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .custom_attr_event import CustomAttrEvent


class P2ContactCustomAttrEventUpdatedV3Data(object):
    _types = {
        "object": CustomAttrEvent,
        "old_object": CustomAttrEvent,
    }

    def __init__(self, d=None):
        self.object: Optional[CustomAttrEvent] = None
        self.old_object: Optional[CustomAttrEvent] = None
        init(self, d, self._types)


class P2ContactCustomAttrEventUpdatedV3(EventContext):
    _types = {
        "event": P2ContactCustomAttrEventUpdatedV3Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ContactCustomAttrEventUpdatedV3Data] = None
        init(self, d, self._types)
