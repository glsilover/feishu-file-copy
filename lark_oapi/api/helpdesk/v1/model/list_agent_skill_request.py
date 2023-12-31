# Code generated by Lark OpenAPI.

from lark_oapi.core.enum import HttpMethod, AccessTokenType
from lark_oapi.core.model import BaseRequest


class ListAgentSkillRequest(BaseRequest):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def builder() -> "ListAgentSkillRequestBuilder":
        return ListAgentSkillRequestBuilder()


class ListAgentSkillRequestBuilder(object):

    def __init__(self) -> None:
        list_agent_skill_request = ListAgentSkillRequest()
        list_agent_skill_request.http_method = HttpMethod.GET
        list_agent_skill_request.uri = "/open-apis/helpdesk/v1/agent_skills"
        list_agent_skill_request.token_types = {AccessTokenType.TENANT}
        self._list_agent_skill_request: ListAgentSkillRequest = list_agent_skill_request

    def build(self) -> ListAgentSkillRequest:
        return self._list_agent_skill_request
