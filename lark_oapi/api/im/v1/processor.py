# Code generated by Lark OpenAPI.

from typing import Callable, Type

from lark_oapi.event.processor import IEventProcessor
from .model.p2_im_chat_disbanded_v1 import P2ImChatDisbandedV1
from .model.p2_im_chat_member_bot_added_v1 import P2ImChatMemberBotAddedV1
from .model.p2_im_chat_member_bot_deleted_v1 import P2ImChatMemberBotDeletedV1
from .model.p2_im_chat_member_user_added_v1 import P2ImChatMemberUserAddedV1
from .model.p2_im_chat_member_user_deleted_v1 import P2ImChatMemberUserDeletedV1
from .model.p2_im_chat_member_user_withdrawn_v1 import P2ImChatMemberUserWithdrawnV1
from .model.p2_im_chat_updated_v1 import P2ImChatUpdatedV1
from .model.p2_im_message_message_read_v1 import P2ImMessageMessageReadV1
from .model.p2_im_message_reaction_created_v1 import P2ImMessageReactionCreatedV1
from .model.p2_im_message_reaction_deleted_v1 import P2ImMessageReactionDeletedV1
from .model.p2_im_message_recalled_v1 import P2ImMessageRecalledV1
from .model.p2_im_message_receive_v1 import P2ImMessageReceiveV1


class P2ImChatDisbandedV1Processor(IEventProcessor[P2ImChatDisbandedV1]):
    def __init__(self, f: Callable[[P2ImChatDisbandedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatDisbandedV1]:
        return P2ImChatDisbandedV1

    def do(self, data: P2ImChatDisbandedV1) -> None:
        self.f(data)


class P2ImChatUpdatedV1Processor(IEventProcessor[P2ImChatUpdatedV1]):
    def __init__(self, f: Callable[[P2ImChatUpdatedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatUpdatedV1]:
        return P2ImChatUpdatedV1

    def do(self, data: P2ImChatUpdatedV1) -> None:
        self.f(data)


class P2ImChatMemberBotAddedV1Processor(IEventProcessor[P2ImChatMemberBotAddedV1]):
    def __init__(self, f: Callable[[P2ImChatMemberBotAddedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatMemberBotAddedV1]:
        return P2ImChatMemberBotAddedV1

    def do(self, data: P2ImChatMemberBotAddedV1) -> None:
        self.f(data)


class P2ImChatMemberBotDeletedV1Processor(IEventProcessor[P2ImChatMemberBotDeletedV1]):
    def __init__(self, f: Callable[[P2ImChatMemberBotDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatMemberBotDeletedV1]:
        return P2ImChatMemberBotDeletedV1

    def do(self, data: P2ImChatMemberBotDeletedV1) -> None:
        self.f(data)


class P2ImChatMemberUserAddedV1Processor(IEventProcessor[P2ImChatMemberUserAddedV1]):
    def __init__(self, f: Callable[[P2ImChatMemberUserAddedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatMemberUserAddedV1]:
        return P2ImChatMemberUserAddedV1

    def do(self, data: P2ImChatMemberUserAddedV1) -> None:
        self.f(data)


class P2ImChatMemberUserDeletedV1Processor(IEventProcessor[P2ImChatMemberUserDeletedV1]):
    def __init__(self, f: Callable[[P2ImChatMemberUserDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatMemberUserDeletedV1]:
        return P2ImChatMemberUserDeletedV1

    def do(self, data: P2ImChatMemberUserDeletedV1) -> None:
        self.f(data)


class P2ImChatMemberUserWithdrawnV1Processor(IEventProcessor[P2ImChatMemberUserWithdrawnV1]):
    def __init__(self, f: Callable[[P2ImChatMemberUserWithdrawnV1], None]):
        self.f = f

    def type(self) -> Type[P2ImChatMemberUserWithdrawnV1]:
        return P2ImChatMemberUserWithdrawnV1

    def do(self, data: P2ImChatMemberUserWithdrawnV1) -> None:
        self.f(data)


class P2ImMessageMessageReadV1Processor(IEventProcessor[P2ImMessageMessageReadV1]):
    def __init__(self, f: Callable[[P2ImMessageMessageReadV1], None]):
        self.f = f

    def type(self) -> Type[P2ImMessageMessageReadV1]:
        return P2ImMessageMessageReadV1

    def do(self, data: P2ImMessageMessageReadV1) -> None:
        self.f(data)


class P2ImMessageRecalledV1Processor(IEventProcessor[P2ImMessageRecalledV1]):
    def __init__(self, f: Callable[[P2ImMessageRecalledV1], None]):
        self.f = f

    def type(self) -> Type[P2ImMessageRecalledV1]:
        return P2ImMessageRecalledV1

    def do(self, data: P2ImMessageRecalledV1) -> None:
        self.f(data)


class P2ImMessageReceiveV1Processor(IEventProcessor[P2ImMessageReceiveV1]):
    def __init__(self, f: Callable[[P2ImMessageReceiveV1], None]):
        self.f = f

    def type(self) -> Type[P2ImMessageReceiveV1]:
        return P2ImMessageReceiveV1

    def do(self, data: P2ImMessageReceiveV1) -> None:
        self.f(data)


class P2ImMessageReactionCreatedV1Processor(IEventProcessor[P2ImMessageReactionCreatedV1]):
    def __init__(self, f: Callable[[P2ImMessageReactionCreatedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImMessageReactionCreatedV1]:
        return P2ImMessageReactionCreatedV1

    def do(self, data: P2ImMessageReactionCreatedV1) -> None:
        self.f(data)


class P2ImMessageReactionDeletedV1Processor(IEventProcessor[P2ImMessageReactionDeletedV1]):
    def __init__(self, f: Callable[[P2ImMessageReactionDeletedV1], None]):
        self.f = f

    def type(self) -> Type[P2ImMessageReactionDeletedV1]:
        return P2ImMessageReactionDeletedV1

    def do(self, data: P2ImMessageReactionDeletedV1) -> None:
        self.f(data)
