# Code generated by Lark OpenAPI.

from lark_oapi.core.model import Config
from .v6.version import V6


class ApplicationService(object):
    def __init__(self, config: Config) -> None:
        self.v6: V6 = V6(config)
