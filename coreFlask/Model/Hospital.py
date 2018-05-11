from Exception.OperationException import OperationException
from Model.Base import Base


class Hospital(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertHospital'

    def to_insert_list(self):
        return [self.name, self.address]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Hospital
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return Hospital(argument[0], argument[1])
        elif isinstance(argument, dict):
            return Hospital(argument['name'], argument['address'])
        raise TypeError

    def to_dict(self):
        return {
            'name': self.name,
            'address': self.address
        }

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
