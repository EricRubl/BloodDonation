import datetime

from Utils.BloodType import BloodType
from Model.Base import Base


class Donation(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertDonation'

    def to_insert_list(self):
        return [self.donor, self.personnel, self.date, self.blood, self.quantity, self.expire_date, self.in_bank]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Donation
        :type argument: tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            new_obj = Donation(argument[1], argument[2], argument[3], argument[4], argument[5], argument[6],
                               argument[7])
            new_obj.donation_id = argument[0]
            return new_obj
        elif isinstance(argument, dict):
            new_obj = Donation(argument['donor'], argument['personnel'], argument['date'], argument['blood'],
                               argument['quantity'], argument['expire_date'], argument['in_bank'])
            new_obj.donation_id = argument['donation_id']
            return new_obj
        raise TypeError

    def to_dict(self):
        return {
            'donation_id': self.donation_id,
            'donor': self.donor,
            'personnel': self.personnel,
            'date': self.date,
            'blood': self.blood,
            'quantity': self.quantity,
            'expire_date': self.expire_date,
            'in_bank': self.in_bank,
        }

    def __init__(self, donor, personnel, date, blood, quantity, expire_date, in_bank):
        """

        :param donor:               string, FOREIGN KEY
        :param personnel:           string, FOREIGN KEY
        :param date:                datetime.datetime object
        :param blood:               must be a code of BloodType
        :param quantity:            float
        :param expire_date:         datetime.datetime object
        :param in_bank              bool, if in back

        :type donor: str
        :type personnel: str
        :type date: datetime.datetime
        :type blood: str
        :type quantity: float
        :type expire_date: datetime.datetime
        :type in_bank: bool
        """
        super().__init__()
        self.donation_id = None
        self.donor = donor
        self.personnel = personnel
        self.date = date
        self.quantity = quantity
        self.expire_date = expire_date
        self.in_bank = in_bank

        self.blood = BloodType.to_code[blood]

    def __str__(self):
        return "Donation ID: %-8s | donor: %-30s | " \
               "personnel: %-30s | date: %-30s | blood: %-4d " \
               "| quantity: %-4f | valability: %-30s | in_bank: %s" % \
               (str(self.donation_id), self.donor, self.personnel, self.date,
                self.blood, self.quantity, str(self.expire_date), str(self.in_bank))

    def update_id(self, new_id):
        if self.donation_id is None:
            self.donation_id = new_id
