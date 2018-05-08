import datetime
from Utils.BloodType import BloodType
from Utils.RequestStatus import RequestStatus
from Model.Base import Base


class Request(Base):
    def __init__(self, priority, blood, doctor, quantity, status, date):
        """
        Constructor for Request class

        :param priority:        int
        :param blood:           must be a code of BloodType
        :param doctor:          string, FOREIGN KEY
        :param quantity:        float
        :param status:          must be a code of RequestStatus
        :param date:            datetime.datetime object

        :type priority: int
        :type blood: str, int
        :type doctor: str
        :type quantity: float
        :type status: str, int
        :type date: datetime.datetime
        """
        super().__init__()
        self.request_id = None
        self.priority = priority
        self.doctor = doctor
        self.quantity = quantity
        self.date = date

        #  switching to codes
        #  todo blood conflict
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood
        self.status = RequestStatus.to_code[status] if isinstance(status, str) else status

    def __str__(self):
        return "Request ID: %-8d | priority: %-8d | " \
               "blood: %-4s | doctor: %-s | quantity: %4f |" \
               "status: %-15s | date: %-30s" % (self.request_id, self.priority,
                                                BloodType.to_string[self.blood], self.doctor, self.quantity,
                                                RequestStatus.to_string[self.status], str(self.date))

    def get_db_insert_string(self):
        return "INSERT INTO Requests (Priority, Blood, Doctor, Quantity, Status, Date) VALUES " \
               "(%d, \'%s\', \'%s\', %f, %d, \'%s\')" % \
               (self.priority, self.blood, self.doctor, self.quantity, self.status, self.date)


r = Request(2, 2, "Dana Bostana", 999999.32, 2, datetime.datetime.now())
print(r.get_db_insert_string())