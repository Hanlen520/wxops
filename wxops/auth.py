def confirm_login(func):
    def inner(*args, **kwargs):
        # TODO: need some confirm
        return func(*args, **kwargs)
    return inner
