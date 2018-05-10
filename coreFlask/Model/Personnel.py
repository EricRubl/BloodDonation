from Exception.OperationException import OperationException
from Model.Base import Base


class Personnel(Base):
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
