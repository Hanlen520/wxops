from .auth import confirm_login
from .operation import OPS_DICT


@confirm_login
class WOServer(object):
    SERVER_STATUS = True

    def run(self):
        """ start operation with server """
        self.SERVER_STATUS = True
        while True:
            request_content = self.get_request()
            if not self.SERVER_STATUS:
                break
            self.apply_operation(*self.parse_request(request_content))

    def get_request(self):
        """ get request content from user """
        user_input = input('DO WTF U WANT:) \n').lower()
        if user_input in ('exit', 'quit', 'disconnect', 'logout'):
            self.SERVER_STATUS = False
        return user_input

    @staticmethod
    def apply_operation(operation_name, object_name):
        """ check the operation and do it """
        if operation_name in OPS_DICT:
            OPS_DICT[operation_name](object_name)
        else:
            print('not supported!')

    @staticmethod
    def parse_request(request_content):
        """ format request content """
        operation_name, *object_name = request_content.split(' ')
        object_name = ' '.join(object_name)
        return operation_name, object_name

server = WOServer()
