class LabResult(object):
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
