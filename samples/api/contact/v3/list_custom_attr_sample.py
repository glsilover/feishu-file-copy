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
    request: ListCustomAttrRequest = ListCustomAttrRequest.builder() \
        .page_size(20) \
        .page_token("AQD9/Rn9eij9Pm39ED40/RYU5lvOM4s6zgbeeNNaWd%2BVKwAsoreeRWk0J2noGvJy") \
        .build()

    # 发起请求
    response: ListCustomAttrResponse = client.contact.v3.custom_attr.list(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.custom_attr.list failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
