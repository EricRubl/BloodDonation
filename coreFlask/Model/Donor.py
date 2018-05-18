import datetime

from Utils.BloodType import BloodType
from Model.Base import Base


class Donor(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertDonor'

    def to_insert_list(self):
        return [self.name, self.date_of_birth, self.email, self.address, self.password, self.blood]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Donor
        :type argument: tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            # must be called only with the tuple returned from the database
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
            'blood': BloodType.to_string[self.blood]
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
        :type blood: str, int
        """
        super().__init__()

        if not isinstance(name, str):
            raise TypeError
        if not isinstance(date_of_birth, datetime.date):
            raise TypeError
        if not isinstance(email, str):
            raise TypeError
        if not isinstance(address, str):
            raise TypeError
        if not isinstance(password, str):
            raise TypeError
        if not isinstance(blood, str) and not isinstance(blood, int):
            raise TypeError
        if isinstance(blood, str) and blood not in BloodType.to_code:
            raise TypeError

        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.address = address
        self.password = password  # :type int
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood

    def __str__(self):
        return "Donor: %-30s | Date of birth: %-30s | email: %-30s | blood: %-4d" % (
            self.name, str(self.date_of_birth), self.email, self.blood
        )

    def update_id(self, new_id):
        pass

    def __eq__(self, other):
        # noinspection PyBroadException
        try:
            if other.name == self.name and \
                    other.date_of_birth == self.date_of_birth and \
                    other.email == self.email and \
                    other.address == self.address and \
                    other.password == self.password and \
                    other.blood == self.blood:
                return True
            return False
        except Exception:
            return False
