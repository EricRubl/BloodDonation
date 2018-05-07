import datetime
from Utils.BloodType import BloodType


class Donor(object):
    def __init__(self, name, date_of_birth, email, password, blood):
        """
        Constructor for Donor class

        :param name:            str
        :param date_of_birth:   datetime.datetime object
        :param email:           str
        :param password:        must be a sha-256
        :param blood:           must be a code of BloodType

        :type name: str
        :type date_of_birth: datetime.datetime
        :type email: str
        :type password: str
        :type blood: str,int
        """
        self.name = name
        self.date_of_birth = date_of_birth
        self.email = email
        self.password = password
        if isinstance(blood, str):
            self.blood = BloodType.to_code[blood]
        else:
            self.blood = blood

    def __str__(self):
        return "Donor: %-30s | Date of birth: %-30s | email: %-30s | blood: %-4s" % (
            self.name, str(self.date_of_birth), self.email, BloodType.to_string[self.blood]
        )

    pass


x = Donor("mata", datetime.datetime(year=2018, month=1, day=1), "mata", "mata", 3)
print(x)

