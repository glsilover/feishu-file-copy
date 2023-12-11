# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.baike.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: CreateDraftRequest = CreateDraftRequest.builder() \
        .user_id_type("user_id") \
        .request_body(Entity.builder()
                      .id("enterprise_40217521")
                      .main_keys([])
                      .aliases([])
                      .description(
        "企业百科是飞书提供的一款知识管理工具，通过企业百科可以帮助企业将分散的知识信息进行聚合，并通过UGC的方式，促进企业知识的保鲜和流通")
                      .related_meta(RelatedMeta.builder().build())
                      .outer_info(OuterInfo.builder().build())
                      .rich_text("")
                      .build()) \
        .build()

    # 发起请求
    response: CreateDraftResponse = client.baike.v1.draft.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.baike.v1.draft.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
