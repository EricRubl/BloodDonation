from Exception.OperationException import OperationException
from Model.Base import Base


class Personnel(Base):
    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Personnel
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return Personnel(argument[0], argument[1], argument[2])
        elif isinstance(argument, dict):
            return Personnel(argument['name'], argument['email'], argument['password'])
        raise TypeError

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password
        }

    def __init__(self, name, email, password):
        """
        Constructor for Personnel class

        :param name:        string
        :param email:       string
        :param password:    must be a sha-256 (string of len 64)
        :type name str
        :type name str
        :type name str
        """
        super().__init__()
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "Personnel: %-30s | email: %-30s" % (self.name, self.email)

    def get_db_insert_string(self):
        return "INSERT INTO Personnel (Name, Email, Password) VALUES " \
               "(\'%s\', \'%s\', \'%s\')" % \
               (self.name, self.email, self.password)

    def get_db_update_string(self):
        raise OperationException('Operation not allowed!')

    def update_id(self, new_id):
        pass
