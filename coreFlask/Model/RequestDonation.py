from Exception.OperationException import OperationException
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
        self.request_id = request_id
        self.donation_id = donation_id

    def __str__(self):
        return "Request ID: %-8d | Donation ID: %-8d" % (self.request_id, self.donation_id)

    def get_db_insert_string(self):
        return "INSERT INTO RequestDonations (Request, Donation) VALUES " \
               "(%d, %d)" % (self.request_id, self.donation_id)

    def update_id(self, new_id):
        pass

    def get_db_update_string(self, **kwargs):
        raise OperationException('Operation not allowed!')
