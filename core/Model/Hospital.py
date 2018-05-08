from Exception.OperationException import OperationException
from Model.Base import Base


class Hospital(Base):
    def __init__(self, name, address):
        """
        Constructor for Hospital class

        :param name:        string
        :param address:     string

        :type name str
        :type address str
        """
        super().__init__()
        self.name = name
        self.address = address

    def __str__(self):
        return "Hospital: %-30s | address: %-30s" % (self.name, self.address)

    def get_db_insert_string(self):
        return "INSERT INTO Hospitals (Name, Address) VALUES (\'%s\', \'%s\')" % (self.name, self.address)

    def update_id(self, new_id):
        pass

    def get_db_update_string(self):
        raise OperationException('Operation not allowed!')

