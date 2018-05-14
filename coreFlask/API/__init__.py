from flask_login import UserMixin

from Dispatcher.Controller import Controller

ctrl = Controller()


class User(UserMixin):
    def __init__(self, name):
        self.id = name
        self.password = ctrl.get_user_password(self.id)
        self.type = ctrl.get_user_type(self.id, self.password)
        print(self.id, self.password, self.type)
