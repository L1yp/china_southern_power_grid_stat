"""Constants for the China Southern Power Grid Statistics integration."""

from datetime import timedelta

from .csg_client import LoginType

DOMAIN = "china_southern_power_grid_stat"

# integration version, keep in sync with manifest.json
VERSION = "1.3.0"

# config flow
# main account (phone number)
CONF_ACCOUNT_NUMBER = "account_number"
CONF_LOGIN_TYPE = "login_type"
CONF_AUTH_TOKEN = "auth_token"
# electricity accounts
CONF_ELE_ACCOUNTS = "accounts"
CONF_UPDATE_INTERVAL = "update_interval"
CONF_SETTINGS = "settings"
CONF_UPDATED_AT = "updated_at"
CONF_ACTION = "action"
CONF_SMS_CODE = "sms_code"
CONF_REFRESH_QR_CODE = "refresh_qr_code"

# 阶梯电价设置（存于 CONF_SETTINGS[CONF_LADDER] 子字典）
CONF_LADDER = "ladder"
CONF_LADDER_ENABLED = "ladder_enabled"
CONF_LADDER_TIER1_MAX = "ladder_tier1_max"
CONF_LADDER_TIER2_MAX = "ladder_tier2_max"
CONF_LADDER_TIER1_PRICE = "ladder_tier1_price"
CONF_LADDER_TIER2_PRICE = "ladder_tier2_price"
CONF_LADDER_TIER3_PRICE = "ladder_tier3_price"

STEP_USER = "user"
STEP_SMS_LOGIN = "sms_login"
STEP_SMS_PWD_LOGIN = "sms_pwd_login"
STEP_VALIDATE_SMS_CODE = "validate_sms_code"
STEP_CSG_QR_LOGIN = "csg_qr_login"
STEP_WX_QR_LOGIN = "wx_qr_login"
STEP_ALI_QR_LOGIN = "ali_qr_login"
STEP_QR_LOGIN = "qr_login"
STEP_VALIDATE_QR_LOGIN = "validate_qr_login"
STEP_INIT = "init"
STEP_SETTINGS = "settings"
STEP_ADD_ACCOUNT = "add_account"
STEP_LADDER = "ladder"

ABORT_NO_ACCOUNT = "no_account"
ABORT_ALL_ADDED = "all_added"

CONF_GENERAL_ERROR = "base"
ERROR_CANNOT_CONNECT = "cannot_connect"
ERROR_INVALID_AUTH = "invalid_auth"
ERROR_UNKNOWN = "unknown"
ERROR_QR_NOT_SCANNED = "qr_not_scanned"
ERROR_LADDER_THRESHOLD_ORDER = "ladder_threshold_order"

# UI
LOGIN_TYPE_TO_QR_APP_NAME = {
    LoginType.LOGIN_TYPE_CSG_QR: "南网APP",
    LoginType.LOGIN_TYPE_WX_QR: "微信",
    LoginType.LOGIN_TYPE_ALI_QR: "支付宝",
}

# api


# sensor updates
SUFFIX_BAL = "balance"
SUFFIX_ARR = "arrears"
SUFFIX_YESTERDAY_KWH = "yesterday_kwh"
SUFFIX_LATEST_DAY_KWH = "latest_day_kwh"
SUFFIX_LATEST_DAY_COST = "latest_day_cost"
SUFFIX_THIS_YEAR_KWH = "this_year_total_usage"
SUFFIX_THIS_YEAR_COST = "this_year_total_cost"
SUFFIX_THIS_MONTH_KWH = "this_month_total_usage"
SUFFIX_THIS_MONTH_COST = "this_month_total_cost"
SUFFIX_CURRENT_LADDER = "current_ladder"
SUFFIX_CURRENT_LADDER_REMAINING_KWH = "current_ladder_remaining_kwh"
SUFFIX_CURRENT_LADDER_TARIFF = "current_ladder_tariff"
SUFFIX_LAST_YEAR_KWH = "last_year_total_usage"
SUFFIX_LAST_YEAR_COST = "last_year_total_cost"
SUFFIX_LAST_MONTH_KWH = "last_month_total_usage"
SUFFIX_LAST_MONTH_COST = "last_month_total_cost"

# 本地计算的阶梯电价相关 sensor（基于用户配置的阶梯 + 年累计用电量本地计算）
SUFFIX_LOCAL_LADDER = "local_ladder"
SUFFIX_LOCAL_LADDER_TARIFF = "local_ladder_tariff"
SUFFIX_LOCAL_LADDER_REMAINING_KWH = "local_ladder_remaining_kwh"
SUFFIX_LOCAL_YEAR_EST_COST = "local_year_est_cost"

# 传感器中文显示名（英文后缀 -> 中文名），仅影响实体的友好名称(name)，
# 不影响 unique_id / entity_id，因此不会产生重复实体
SUFFIX_TO_NAME_ZH = {
    SUFFIX_BAL: "账户余额",
    SUFFIX_ARR: "欠费金额",
    SUFFIX_YESTERDAY_KWH: "昨日用电量",
    SUFFIX_LATEST_DAY_KWH: "最近一日用电量",
    SUFFIX_LATEST_DAY_COST: "最近一日电费",
    SUFFIX_THIS_YEAR_KWH: "今年累计用电量",
    SUFFIX_THIS_YEAR_COST: "今年累计电费",
    SUFFIX_THIS_MONTH_KWH: "本月累计用电量",
    SUFFIX_THIS_MONTH_COST: "本月累计电费",
    SUFFIX_CURRENT_LADDER: "当前阶梯档位",
    SUFFIX_CURRENT_LADDER_REMAINING_KWH: "当前阶梯剩余电量",
    SUFFIX_CURRENT_LADDER_TARIFF: "当前阶梯电价",
    SUFFIX_LAST_YEAR_KWH: "去年累计用电量",
    SUFFIX_LAST_YEAR_COST: "去年累计电费",
    SUFFIX_LAST_MONTH_KWH: "上月累计用电量",
    SUFFIX_LAST_MONTH_COST: "上月累计电费",
    SUFFIX_LOCAL_LADDER: "本地阶梯档位",
    SUFFIX_LOCAL_LADDER_TARIFF: "本地阶梯电价",
    SUFFIX_LOCAL_LADDER_REMAINING_KWH: "本地阶梯剩余电量",
    SUFFIX_LOCAL_YEAR_EST_COST: "本年阶梯预估电费",
}

ATTR_KEY_THIS_MONTH_BY_DAY = "this_month_by_day"
ATTR_KEY_THIS_YEAR_BY_MONTH = "this_year_by_month"
ATTR_KEY_LAST_MONTH_BY_DAY = "last_month_by_day"
ATTR_KEY_LAST_YEAR_BY_MONTH = "last_year_by_month"
ATTR_KEY_LATEST_DAY_DATE = "latest_day_date"
ATTR_KEY_CURRENT_LADDER_START_DATE = "current_ladder_start_date"

STATE_UPDATE_UNCHANGED = "unchanged"
DATA_KEY_LAST_UPDATE_DAY = "last_update_day"

# settings

# currently, this timeout is for each request, user should not need to set it manually
SETTING_UPDATE_TIMEOUT = 60
# the first n days in a month that will get data of last month
SETTING_LAST_MONTH_UPDATE_DAY_THRESHOLD = 3
# the first n days in a year that will get data of last year
SETTING_LAST_YEAR_UPDATE_DAY_THRESHOLD = 7


# defaults
DEFAULT_UPDATE_INTERVAL = timedelta(hours=4).seconds

# 阶梯电价默认值（按年累计，3 档；阈值/电价仅为占位示例，需用户按本地实际填写）
DEFAULT_LADDER = {
    CONF_LADDER_ENABLED: False,
    CONF_LADDER_TIER1_MAX: 2400,
    CONF_LADDER_TIER2_MAX: 4800,
    CONF_LADDER_TIER1_PRICE: 0.6,
    CONF_LADDER_TIER2_PRICE: 0.65,
    CONF_LADDER_TIER3_PRICE: 0.9,
}
