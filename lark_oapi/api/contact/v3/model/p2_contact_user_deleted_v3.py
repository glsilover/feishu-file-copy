# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from lark_oapi.event.context import EventContext
from .old_user_object import OldUserObject
from .user_event import UserEvent


class P2ContactUserDeletedV3Data(object):
    _types = {
        "object": UserEvent,
        "old_object": OldUserObject,
    }

    def __init__(self, d=None):
        self.object: Optional[UserEvent] = None
        self.old_object: Optional[OldUserObject] = None
        init(self, d, self._types)


class P2ContactUserDeletedV3(EventContext):
    _types = {
        "event": P2ContactUserDeletedV3Data
    }

    def __init__(self, d=None):
        super().__init__(d)
        self._types.update(super()._types)
        self.event: Optional[P2ContactUserDeletedV3Data] = None
        init(self, d, self._types)