import datetime

from Utils.BloodType import BloodType


class Donation(object):
    def __init__(self, donation_id, donor, personnel, date, blood, quantity, valability):
        """

        :param donation_id:         int
        :param donor:               string, FOREIGN KEY
        :param personnel:           string, FOREIGN KEY
        :param date:                datetime.datetime object
        :param blood:               must be a code of BloodType
        :param quantity:            float
        :param valability:          datetime.timedelta object

        :type donation_id: int
        :type donor: str
        :type personnel: str
        :type date: datetime.datetime
        :type blood: str,int
        :type quantity: float
        :type valability: datetime.timedelta
        """
        self.donation_id = donation_id
        self.donor = donor
        self.personnel = personnel
        self.date = date
        self.quantity = quantity
        self.valability = valability

        # switching to code
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood

    def __str__(self):
        return "Donation ID: %-8d | donor: %-30s | " \
               "personnel: %-30s | date: %-30s | blood: %-4s " \
               "| quantity: %-4f | valability: %-30s" % (self.donation_id, self.donor, self.personnel, self.date,
                                                         self.blood, self.quantity, str(self.valability))


x = Donation(123, "muie", "laba", datetime.datetime(year=2000, month=1, day=1), 1, 1.234,
             datetime.timedelta(days=2))

print(x)
