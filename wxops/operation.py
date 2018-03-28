from . import APP_DICT
import os


# TODO: need more function
def open_app(app_name):
    if app_name in APP_DICT:
        app_path = APP_DICT[app_name]
        os.startfile(app_path)
        print('starting {} ...'.format(app_path))
        return True
    else:
        print('{} is not found.'.format(app_name))
        return False


def screen_shot():
    pass


OPS_DICT = {
    'open': open_app,
}
