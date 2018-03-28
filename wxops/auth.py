LOGIN_STATUS = False


def confirm_login(cls):
    def inner(*args, **kwargs):
        # TODO: need some confirm
        # TODO: login controll
        _instance = cls(*args, **kwargs)
        _instance.__dict__['login_status'] = True
        return _instance
    return inner
