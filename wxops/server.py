from .auth import confirm_login
from .operation import OPS_DICT


SERVER_STATUS = True


@confirm_login
def run_server():
    set_server(True)
    while True:
        request_content = get_request()
        if not SERVER_STATUS:
            break
        operation_name, object_name = parse_request(request_content)
        apply_operation(operation_name, object_name)


def set_server(status):
    global SERVER_STATUS
    SERVER_STATUS = bool(status)


def get_request():
    user_input = input('DO WTF U WANT:) \n').lower()
    if user_input in ('exit', 'quit', 'disconnect', 'logout'):
        set_server(False)
    return user_input


def apply_operation(operation_name, object_name):
    if operation_name in OPS_DICT:
        OPS_DICT[operation_name](object_name)
    else:
        print('not supported!')


def parse_request(request_content):
    operation_name, *object_name = request_content.split(' ')
    object_name = ' '.join(object_name)
    return operation_name, object_name
