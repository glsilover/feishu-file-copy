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
    request: CreateUserRequest = CreateUserRequest.builder() \
        .user_id_type("open_id") \
        .department_id_type("open_department_id") \
        .client_token("xxxx-xxxxx-xxx") \
        .request_body(User.builder()
                      .user_id("str")
                      .name("张三")
                      .en_name("San Zhang")
                      .nickname("Alex Zhang")
                      .email("zhangsan@gmail.com")
                      .mobile("+41446681800")
                      .mobile_visible(False)
                      .gender(0)
                      .avatar_key("2500c7a9-5fff-4d9a-a2de-3d59614ae28g")
                      .department_ids([])
                      .leader_user_id("ou_7dab8a3d3cdcc9da365777c7ad535d62")
                      .city("杭州")
                      .country("CN")
                      .work_station("北楼-H34")
                      .join_time(2147483647)
                      .employee_no("1")
                      .employee_type(1)
                      .orders([])
                      .custom_attrs([])
                      .enterprise_email("demo@mail.com")
                      .job_title("xxxxx")
                      .geo("cn")
                      .job_level_id("mga5oa8ayjlp9rb")
                      .job_family_id("mga5oa8ayjlp9rb")
                      .subscription_ids([])
                      .dotted_line_leader_user_ids([])
                      .build()) \
        .build()

    # 发起请求
    response: CreateUserResponse = client.contact.v3.user.create(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.contact.v3.user.create failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
