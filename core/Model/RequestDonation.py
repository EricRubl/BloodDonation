class RequestDonation(object):
    def __init__(self, request_id, donation_id):
        """
        Constructor for RequestDonation class

        :param request_id:      int, FOREIGN KEY
        :param donation_id:     int, FOREIGN KEY

        :type request_id int
        :type donation_id int
        """
        self.request_id = request_id
        self.donation_id = donation_id

    def __str__(self):
        return "Request ID: %-8d | Donation ID: %-8d" % (self.request_id, self.donation_id)
