import datetime
from Utils.BloodType import BloodType
from Utils.RequestStatus import RequestStatus


class Request(object):
    def __init__(self, request_id, priority, blood, doctor, quantity, status, date):
        """
        Constructor for Request class

        :param request_id:      int
        :param priority:        int
        :param blood:           must be a code of BloodType
        :param doctor:          string, FOREIGN KEY
        :param quantity:        float
        :param status:          must be a code of RequestStatus
        :param date:            datetime.datetime object

        :type request_id: int
        :type priority: int
        :type blood: str, int
        :type doctor: str
        :type quantity: float
        :type status: str, int
        :type date: datetime.datetime
        """
        self.request_id = request_id
        self.priority = priority
        self.doctor = doctor
        self.quantity = quantity
        self.date = date

        #  switching to codes
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood
        self.status = RequestStatus.to_code[status] if isinstance(status, str) else status

    def __str__(self):
        return "Request ID: %-8d | priority: %-8d | " \
               "blood: %-4s | doctor: %-s | quantity: %4f |" \
               "status: %-15s | date: %-30s" % (self.request_id, self.priority,
                                                BloodType.to_string[self.blood], self.doctor, self.quantity,
                                                RequestStatus.to_string[self.status], str(self.date))
