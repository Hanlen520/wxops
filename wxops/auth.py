from functools import wraps


LOGIN_STATUS = False


def confirm_login(cls):
    @wraps(cls)
    def inner(*args, **kwargs):
        # TODO: need some confirm
        # TODO: 使用微信号作为id，赋予不同的访问权限，管理员需要事先注册
        _instance = cls(*args, **kwargs)
        _instance.__dict__['LOGIN_STATUS'] = True
        return _instance
    return inner
