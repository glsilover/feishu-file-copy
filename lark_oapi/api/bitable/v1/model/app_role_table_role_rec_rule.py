# Code generated by Lark OpenAPI.

from typing import Optional, List

from lark_oapi.core.construct import init
from .app_role_table_role_rec_rule_condition import AppRoleTableRoleRecRuleCondition


class AppRoleTableRoleRecRule(object):
    _types = {
        "conditions": List[AppRoleTableRoleRecRuleCondition],
        "conjunction": str,
        "other_perm": int,
    }

    def __init__(self, d=None):
        self.conditions: Optional[List[AppRoleTableRoleRecRuleCondition]] = None
        self.conjunction: Optional[str] = None
        self.other_perm: Optional[int] = None
        init(self, d, self._types)

    @staticmethod
    def builder() -> "AppRoleTableRoleRecRuleBuilder":
        return AppRoleTableRoleRecRuleBuilder()


class AppRoleTableRoleRecRuleBuilder(object):
    def __init__(self) -> None:
        self._app_role_table_role_rec_rule = AppRoleTableRoleRecRule()

    def conditions(self, conditions: List[AppRoleTableRoleRecRuleCondition]) -> "AppRoleTableRoleRecRuleBuilder":
        self._app_role_table_role_rec_rule.conditions = conditions
        return self

    def conjunction(self, conjunction: str) -> "AppRoleTableRoleRecRuleBuilder":
        self._app_role_table_role_rec_rule.conjunction = conjunction
        return self

    def other_perm(self, other_perm: int) -> "AppRoleTableRoleRecRuleBuilder":
        self._app_role_table_role_rec_rule.other_perm = other_perm
        return self

    def build(self) -> "AppRoleTableRoleRecRule":
        return self._app_role_table_role_rec_rule