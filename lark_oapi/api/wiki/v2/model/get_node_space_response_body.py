# Code generated by Lark OpenAPI.

from typing import Optional

from lark_oapi.core.construct import init
from .node import Node


class GetNodeSpaceResponseBody(object):
    _types = {
        "node": Node,
    }

    def __init__(self, d=None):
        self.node: Optional[Node] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "GetNodeSpaceResponseBodyBuilder":
        return GetNodeSpaceResponseBodyBuilder()


class GetNodeSpaceResponseBodyBuilder(object):
    def __init__(self) -> None:
        self._get_node_space_response_body = GetNodeSpaceResponseBody()

    def node(self, node: Node) -> "GetNodeSpaceResponseBodyBuilder":
        self._get_node_space_response_body.node = node
        return self

    def build(self) -> "GetNodeSpaceResponseBody":
        return self._get_node_space_response_body