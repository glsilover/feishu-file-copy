# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.contact.v3 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: GetGroupRequest = GetGroupRequest.builder() \
        .group_id("g193821") \
        .user_id_type("open_id") \
        .department_id_type("open_department_id") \
        .build()

    # 发起请求
    response: GetGroupResponse = client.contact.v3.group.get(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.group.get failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
