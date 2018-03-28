from wxops.server import server


if __name__ == '__main__':
    while True:
        command = input('Waiting for connect... \n')
        if command == 'login':
            print('Connected.')
            server.run()
