from . import APP_DICT
import os


# TODO: need more function
def open_app(app_name):
    if app_name in APP_DICT:
        os.startfile(APP_DICT[app_name])
        return True
    else:
        return False


def screen_shot():
    pass


OPS_DICT = {
    'open': open_app,
}
