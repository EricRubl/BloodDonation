from Exception.OperationException import OperationException
from Model.Base import Base


class LabResult(Base):
    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class LabResult
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return LabResult(argument[0], argument[1], argument[2], argument[3], argument[4], argument[5])
        elif isinstance(argument, dict):
            return LabResult(argument['donation_id'], argument['syph'], argument['hbv'],
                             argument['hiv'], argument['hev'], argument['htlv'])
        raise TypeError

    def to_dict(self):
        return {
            'donation_id': self.donation_id,
            'syph': self.syph,
            'hbv': self.HBV,
            'hiv': self.HIV,
            'hev': self.HEV,
            'htlv': self.HTLV,
        }

    def __init__(self, donation_id, syph, hbv, hiv, hev, htlv):
        """
        Constructor for LabResult class

        :param donation_id:     int, FOREIGN KEY
        :param syph:            bool
        :param hbv:             bool
        :param hiv:             bool
        :param hev:             bool
        :param htlv:            bool

        :type donation_id: int
        :type syph: bool
        :type hbv: bool
        :type hiv: bool
        :type hev: bool
        :type htlv: bool
        """
        super().__init__()
        self.donation_id = donation_id
        self.syph = syph
        self.HBV = hbv
        self.HIV = hiv
        self.HEV = hev
        self.HTLV = htlv

    def get_positive(self):
        """
        Returns all the positive results
        :return: list
        """
        result = []
        if self.syph:
            result.append("SYPH")
        if self.HBV:
            result.append("HBV")
        if self.HIV:
            result.append("HIV")
        if self.HEV:
            result.append("HEV")
        if self.HTLV:
            result.append("HTLV")
        return result

    def get_negative(self):
        """
        Returns all the negative results
        :return: list
        """
        result = []
        if not self.syph:
            result.append("SYPH")
        if not self.HBV:
            result.append("HBV")
        if not self.HIV:
            result.append("HIV")
        if not self.HEV:
            result.append("HEV")
        if not self.HTLV:
            result.append("HTLV")
        return result

    def __str__(self):
        positive = str(self.get_positive())
        negative = str(self.get_negative())
        return "Donation ID: %-8d | positive: %-50s | negative: %s" % \
               (self.donation_id, positive, negative)

    def get_db_update_string(self):
        raise OperationException('Operation not allowed!')

    def get_db_insert_string(self):
        return "INSERT INTO LabResults (Donation, Syph, HBV, HIV, HEV, HTLV) " \
               "VALUES (%d, %s, %s, %s, %s, %s)" % \
               (self.donation_id, self.syph, self.HBV, self.HIV, self.HEV, self.HTLV)

    def update_id(self, new_id):
        pass
