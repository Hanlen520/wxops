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
            self.parse_request(request_content)

    def get_request(self):
        """ get request content from user """
        user_input = input('DO WTF U WANT:) \n').lower()
        if user_input in ('exit', 'quit', 'disconnect', 'logout'):
            self.SERVER_STATUS = False
        return user_input

    @staticmethod
    def parse_request(request_content):
        """ format request content, check the operation and do it """
        operation_name, *object_name = request_content.split(' ')
        if not object_name:
            print('need object name!')
            return
        object_name = ' '.join(object_name)

        if operation_name in OPS_DICT:
            OPS_DICT[operation_name](object_name)
        else:
            print('not supported!')

server = WOServer()
