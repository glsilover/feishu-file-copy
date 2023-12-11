# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.hire.v1 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: ReconciliationReferralAccountRequest = ReconciliationReferralAccountRequest.builder() \
        .request_body(ReconciliationReferralAccountRequestBody.builder()
                      .start_trans_time("1685416831621")
                      .end_trans_time("1685416831622")
                      .trade_details([])
                      .build()) \
        .build()

    # 发起请求
    response: ReconciliationReferralAccountResponse = client.hire.v1.referral_account.reconciliation(request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.hire.v1.referral_account.reconciliation failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
