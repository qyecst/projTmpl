# -*- coding: utf-8 -*-
import os
from datetime import datetime

# 项目根路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    # region ======== USER ========
    # 文件目录/**手动调用**/
    SOME_RESOURCE_PATH = os.path.join(BASE_DIR, 'static', 'some_resource')
    # endregion ======== USER ========

    # region ======== FLASK配置 ========
    # 加密字符串。自动注入
    SECRET_KEY = os.urandom(24)
    # JSON转码。自动注入
    JSON_AS_ASCII = True

    # endregion ======== FLASK配置 ========

    @staticmethod
    def init_app(app):
        pass


class DevConfig(Config):
    # 开发环境SECRET_KEY
    SECRET_KEY = 'dev secret'
    JSON_AS_ASCII = False

    @staticmethod
    def init_app(app):
        pass


class ProConfig(Config):
    # 生产环境SECRET_KEY
    SECRET_KEY = os.urandom(24)

    @staticmethod
    def init_app(app):
        pass


# 配置字典
config_dict = {
    'dev': DevConfig,
    'pro': ProConfig,

    'default': ProConfig
}


# 时间格式化函数
def get_time_str(format_type=0):
    now_time = datetime.now()
    if format_type == 1:
        return now_time.strftime('%Y-%m-%d')
    else:
        return now_time.strftime('%Y-%m-%d %H:%M:%S')
