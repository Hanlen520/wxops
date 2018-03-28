from . import APP_DICT
from PIL import ImageGrab
import os


# TODO: need more function
def open_app():
    print(os.linesep.join(APP_DICT.keys()))
    app_name = input('need app name: (options showed above)' + os.linesep)
    if app_name in APP_DICT:
        app_path = APP_DICT[app_name]
        os.startfile(app_path)
        print('starting {} ...'.format(app_path))
        return True
    else:
        print('{} is not found.'.format(app_name))
        return False


def screen_shot():
    pic = ImageGrab.grab()
    pic.save('temp.jpg')
    print('shot!')
    # TODO: 发送出去


def terminal_command():
    # TODO: 这里需要改成调用现有脚本而不是直接输入命令
    print('terminal mode. enter \'qqq\' to exit.')
    while True:
        user_input = input('>> ')
        if user_input == 'qqq':
            print('quited.')
            break
        print(os.popen(user_input).read())


OPS_DICT = {
    'open': open_app,
    'screenshot': screen_shot,
    'terminal': terminal_command
}
