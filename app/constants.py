# -*- coding: utf-8 -*-

SUCCESS = 0

PARM_FORMAT_ERROR = 1

GROUP_NOT_EXIST = 2

PHONE_FORMAT_ERROR = 3

EMAIL_FORMAT_ERROR = 4

CALL_NOT_NULL = 5


status_message = {
    SUCCESS: '请求成功',

    PARM_FORMAT_ERROR: '参数格式错误',

    GROUP_NOT_EXIST: '队伍不存在',

    PHONE_FORMAT_ERROR: '手机号码不为11位',

    EMAIL_FORMAT_ERROR: '邮箱格式错误',

    CALL_NOT_NULL: '联系方式不能为空'
}
