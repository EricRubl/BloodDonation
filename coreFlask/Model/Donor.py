import datetime

from Exception.OperationException import OperationException
from Utils.BloodType import BloodType
from Model.Base import Base


class Donor(Base):
    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Donor
        :type argument: tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return Donor(argument[0], argument[1], argument[2], argument[3], argument[4], argument[5])
        elif isinstance(argument, dict):
            return Donor(argument['name'], argument['date_of_birth'], argument['email'], argument['address'],
                         argument['password'], argument['blood'])
        raise TypeError

    def to_dict(self):
        return {
            'name': self.name,
            'date_of_birth': self.date_of_birth,
            'email': self.email,
            'address': self.address,
            'password': self.password,
            'blood': self.blood
        }

    def __init__(self, name, date_of_birth, email, address, password, blood):
        """
        Constructor for Donor class

        :param name:            string
        :param date_of_birth:   datetime.datetime object
        :param email:           string
        :param address:         string
        :param password:        must be a sha-256 (string of len 64)
        :param blood:           must be a code of BloodType

        :type name: str
        :type date_of_birth: datetime.date
        :type email: str
        :type address: str
        :type password: str
        :type blood: str,int
        """
        super().__init__()
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.password = password  # :type int

        #  switching to codes
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood

    def __str__(self):
        return "Donor: %-30s | Date of birth: %-30s | email: %-30s | blood: %-4s" % (
            self.name, str(self.date_of_birth), self.email, BloodType.to_string[self.blood]
        )

    def get_db_insert_string(self):
        return "INSERT INTO Donors (Name, DOB, Email, Address, Password, Blood) " \
               "VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')" % \
               (self.name, self.date_of_birth, self.email, self.address, self.password, BloodType.to_string[self.blood])

    def get_db_update_string(self):
        raise OperationException('Operation not allowed!')

    def update_id(self, new_id):
        pass
