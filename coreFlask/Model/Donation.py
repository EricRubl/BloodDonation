import datetime

from Utils.BloodType import BloodType
from Model.Base import Base


class Donation(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertDonation'

    def to_insert_list(self):
        return [self.donor, self.personnel, self.date, self.blood, self.expire_date, self.in_bank]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Donation
        :type argument: tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            # must be called only with the tuple returned from the database
            donation_id = argument[0]
            donor = argument[1]
            personnel = argument[2]
            date = argument[3]
            blood = argument[4]
            expire_date = argument[5]
            in_bank = argument[6]

            if isinstance(in_bank, int):
                in_bank = bool(in_bank)

            new_obj = Donation(donor, personnel, date, blood, expire_date, in_bank)
            new_obj.donation_id = donation_id
            return new_obj
        elif isinstance(argument, dict):
            new_obj = Donation(argument['donor'], argument['personnel'], argument['date'], argument['blood'],
                               argument['expire_date'], argument['in_bank'])
            new_obj.donation_id = argument['donation_id']
            return new_obj
        raise TypeError

    def to_dict(self):
        return {
            'donation_id': self.donation_id,
            'donor': self.donor,
            'personnel': self.personnel,
            'date': self.date,
            'blood': BloodType.to_string[self.blood],
            'expire_date': self.expire_date,
            'in_bank': self.in_bank,
        }

    def __init__(self, donor, personnel, date, blood, expire_date, in_bank):
        """

        :param donor:               string, FOREIGN KEY
        :param personnel:           string, FOREIGN KEY
        :param date:                datetime.datetime object
        :param blood:               must be a code of BloodType
        :param expire_date:         datetime.datetime object
        :param in_bank              bool, if in back

        :type donor: str
        :type personnel: str
        :type date: datetime.datetime
        :type blood: str, int
        :type expire_date: datetime.datetime
        :type in_bank: bool
        """
        super().__init__()

        if not isinstance(donor, str):
            raise TypeError
        if not isinstance(personnel, str):
            raise TypeError
        if not isinstance(date, datetime.datetime):
            raise TypeError
        if not isinstance(blood, str) and not isinstance(blood, int):
            raise TypeError
        if isinstance(blood, str) and blood not in BloodType.to_code:
            raise TypeError
        if not isinstance(expire_date, datetime.datetime):
            raise TypeError
        if not isinstance(in_bank, bool):
            raise TypeError

        self.donation_id = None
        self.donor = donor
        self.personnel = personnel
        self.date = date
        self.expire_date = expire_date
        self.in_bank = in_bank

        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood

    def __str__(self):
        return "Donation ID: %-8s | donor: %-30s | " \
               "personnel: %-30s | date: %-30s | blood: %-4d " \
               "| valability: %-30s | in_bank: %s" % \
               (str(self.donation_id), self.donor, self.personnel, self.date.isoformat(),
                self.blood, self.expire_date.isoformat(), str(self.in_bank))

    def update_id(self, new_id):
        if self.donation_id is None:
            self.donation_id = new_id

    def __eq__(self, other):
        # noinspection PyBroadException
        try:
            if other.donation_id == self.donation_id and \
                    other.donor == self.donor and \
                    other.personnel == self.personnel and \
                    other.date == self.date and \
                    other.expire_date == self.expire_date and \
                    other.in_bank == self.in_bank:
                return True
            return False
        except Exception:
            return False
