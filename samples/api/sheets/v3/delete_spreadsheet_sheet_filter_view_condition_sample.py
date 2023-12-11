# Code generated by Lark OpenAPI.

import lark_oapi as lark
from lark_oapi.api.sheets.v3 import *


def main():
    # 创建client
    client = lark.Client.builder() \
        .app_id(lark.APP_ID) \
        .app_secret(lark.APP_SECRET) \
        .log_level(lark.LogLevel.DEBUG) \
        .build()

    # 构造请求对象
    request: DeleteSpreadsheetSheetFilterViewConditionRequest = DeleteSpreadsheetSheetFilterViewConditionRequest.builder() \
        .spreadsheet_token("shtcnmBA*****yGehy8") \
        .sheet_id("0b**12") \
        .filter_view_id("pH9hbVcCXA") \
        .condition_id("E") \
        .build()

    # 发起请求
    response: DeleteSpreadsheetSheetFilterViewConditionResponse = client.sheets.v3.spreadsheet_sheet_filter_view_condition.delete(
        request)

    # 处理失败返回
    if not response.success():
        lark.logger.error(
            f"client.sheets.v3.spreadsheet_sheet_filter_view_condition.delete failed, code: {response.code}, msg: {response.msg}, log_id: {response.get_log_id()}")
        return

    # 处理业务结果
    lark.logger.info(lark.JSON.marshal(response.data, indent=4))


if __name__ == "__main__":
    main()
