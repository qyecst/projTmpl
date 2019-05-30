# -*- coding: utf-8 -*-
from functools import wraps
from flask import Blueprint, jsonify, request, render_template_string, current_app

# from flask import render_template, current_app, request, jsonify
# render_template渲染模板
# current_app当前app对象
# request req.method req.form req.args req.files req.cookies
# jsonify return jsonify({"key":"value"})

# 路由蓝本，需在app中注册
router = Blueprint('router', __name__)


# 普通函数
def some_func():
    pass


# 添加路由
@router.route('/')
def some_route():
    return jsonify({"code": 200, "status": "success", "sec": str(current_app.config['SECRET_KEY'])})


# 其他路由
@router.route('/some/', defaults={'int_var': 0}, methods=['GET', 'POST'])
@router.route('/some/path/<int:int_var>', defaults={'int_var': 0})
def some_args_route(int_var):
    return jsonify({"code": 200, "status": "success", "args": [int_var]})


# 自定错误
class UserException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self)
        self.err_info = 'some info'
    # other function


# 错误处理 使用app_errorhandler捕捉全局错误 用error_handler只会捕捉本蓝本的错误
@router.app_errorhandler(404)
@router.app_errorhandler(500)
@router.app_errorhandler(UserException)
def err_handle_func(e):
    # 请求支持json不支持html格式时返回json数据
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({"code": "err_code", "status": "error"})
        response.status_code = 500
        return response
    # 返回渲染页面
    return render_template_string('{"code": "err_code", "status": "error"}'), 500


# 装饰器
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'call {func.__name__}():')
        return func(*args, **kwargs)

    return wrapper


# 带参数装饰器
def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                print('Insufficient permissions')
                return False
            return f(*args, **kwargs)

        return decorated_function

    return decorator


# 装饰器使用
@log
def some_f():
    pass


# 参数装饰器使用
@router.route('/some/path')
@permission_required('some_permission')
def some_args_f():
    pass

# 模块化蓝本
# |- /<dir>/blue_print/
#   |- __init__.py
#   |- views.py
#   |- errors.py
# /<dir>/blue_print/__init__.py
#    from flask import Blueprint
#    router = Blueprint('router', __name__)
#    from . import views, errors
# /<dir>/blue_print/[views|errors].py
#    from . import router
#    @router.route('/path/to/route')
#    def some_route_func():
#      pass
# /<dir>/initial.py
#    from <dir>.blue_print import router
#    app.register_blueprint(router)

# 带版本的api
# |- /<dir>/app/
#   |- api_1_0/
#     |- __init__.py
#     |- views.py
# <蓝本编写&注册同上>
# /<dir>/initial.py
#    from <dir>.api_1_0 import router
#    app.register_blueprint(router, url_prefix='/api/v1.0')
