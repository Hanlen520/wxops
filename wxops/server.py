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
        # TODO: 将io修改成微信版本
        user_input = input('DO WTF U WANT:) \n').lower()
        if user_input in ('exit', 'quit', 'disconnect', 'logout'):
            self.SERVER_STATUS = False
        return user_input

    def reset(self):
        self.SERVER_STATUS = False
        self.LOGIN_STATUS = False

    @staticmethod
    def parse_request(action_name):
        """ check the operation and do it """
        if action_name in OPS_DICT:
            OPS_DICT[action_name]()
        else:
            print('not supported!')

server = WOServer()
