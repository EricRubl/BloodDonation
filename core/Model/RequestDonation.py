from Model.Base import Base


class RequestDonation(Base):
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
