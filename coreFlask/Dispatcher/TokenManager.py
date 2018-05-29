import datetime
import random
import string
import threading
from time import sleep


class TokenManager:

    def __init__(self):
        self.active_tokens = []
        threading.Thread(target=self.__run_forever, daemon=False).start()
        self.expire_time = 2

    def __run_forever(self):
        while True:
            for index in self.active_tokens:
                print(index, datetime.datetime.now() - index['timestamp'])
            for index in self.active_tokens:
                if datetime.datetime.now() - index['timestamp'] > datetime.timedelta(minutes=self.expire_time):
                    self.active_tokens.remove(index)
                    break
            sleep(5)
        pass

    @staticmethod
    def random_string(length):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    def new_token(self, user_mail, new_password):
        now = datetime.datetime.now()
        token = self.random_string(64)
        self.active_tokens.append({
            'timestamp': now,
            'user_email': user_mail,
            'new_password': new_password,
            'token': token
        })
        return token

    def verify_token(self, token):
        result = None
        for index in self.active_tokens:
            if index['token'] == token and datetime.datetime.now() - \
                    index['timestamp'] < datetime.timedelta(minutes=self.expire_time):
                result = index.copy()
                self.active_tokens.remove(index)
                break
        return result
    pass


pass


if __name__ == '__main__':
    asd = TokenManager()
    asd.new_token('asd', 'zxc')
    tk = asd.new_token('qwe', 'qqq')
    asd.new_token('xcv', 'fgh')
    for i in asd.active_tokens:
        print(i)
    res = asd.verify_token(tk)
    print("asdasd", res)
    for i in asd.active_tokens:
        print(i)
    pass
