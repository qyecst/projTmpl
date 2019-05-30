# -*- coding: utf-8 -*-
from flask import Flask
from module.config import BASE_DIR, config_dict, get_time_str
from module.logger import my_logger
from module.router import router


# app初始化函数
def create_app(config_name):
    # app初始化，设定root_path为根目录
    app = Flask(__name__, root_path=BASE_DIR)
    # 配置初始化
    app.config.from_object(config_dict[config_name])
    config_dict[config_name].init_app(app)
    # jinja自定义过滤器
    app.jinja_env.filters['get_time_str'] = get_time_str
    # logger初始化
    app.my_logger = my_logger
    # 路由注册
    app.register_blueprint(router)
    # app.register_blueprint(router, url_prefix='/auth')
    return app
