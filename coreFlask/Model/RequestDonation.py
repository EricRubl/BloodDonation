from Model.Base import Base


class RequestDonation(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertRequestDonation'

    def to_insert_list(self):
        return [self.request_id, self.donation_id]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class RequestDonation
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return RequestDonation(argument[0], argument[1])
        elif isinstance(argument, dict):
            return RequestDonation(argument['request_id'], argument['donation_id'])
        raise TypeError

    def to_dict(self):
        return {
            'request_id': self.request_id,
            'donation_id': self.donation_id
        }

    def __init__(self, request_id, donation_id):
        """
        Constructor for RequestDonation class

        :param request_id:      int, FOREIGN KEY
        :param donation_id:     int, FOREIGN KEY

        :type request_id int
        :type donation_id int
        """
        super().__init__()

        if not isinstance(request_id, int):
            raise TypeError
        if not isinstance(donation_id, int):
            raise TypeError

        self.request_id = request_id
        self.donation_id = donation_id

    def __str__(self):
        return "Request ID: %-8d | Donation ID: %-8d" % (self.request_id, self.donation_id)

    def update_id(self, new_id):
        pass

    def __eq__(self, other):
        # noinspection PyBroadException
        try:
            if other.request_id == self.request_id and \
                    other.donation_id == self.donation_id:
                return True
            return False
        except Exception:
            return False
