import datetime

from Exception.OperationException import OperationException
from Utils.BloodType import BloodType
from Model.Base import Base


class Donation(Base):
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
        :type blood: str,int
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

        # switching to code
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood

    def __str__(self):
        return "Donation ID: %-8s | donor: %-30s | " \
               "personnel: %-30s | date: %-30s | blood: %-4s " \
               "| quantity: %-4f | valability: %-30s | in_bank: %s" % \
               (str(self.donation_id), self.donor, self.personnel, self.date,
                self.blood, self.quantity, str(self.expire_date), str(self.in_bank))

    def get_db_insert_string(self):
        return "INSERT INTO Donations (Donor, Personnel, Date, Blood, Quantity, ExpireDate, InBank) VALUES " \
               "(\'%s\', \'%s\', \'%s\', \'%s\', %f, \'%s\', %s)" % \
               (self.donor, self.personnel, self.date, BloodType.to_string[self.blood],
                self.quantity, self.expire_date, self.in_bank)

    def update_id(self, new_id):
        if self.donation_id is None:
            self.donation_id = new_id

    def get_db_update_string(self):
        raise OperationException('Operation not allowed!')
