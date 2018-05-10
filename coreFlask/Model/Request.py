import datetime
from Utils.BloodType import BloodType
from Utils.RequestStatus import RequestStatus
from Model.Base import Base


class Request(Base):
    def to_insert_list(self):
        return [self.request_id, self.priority, self.blood, self.doctor, self.quantity, self.status, self.date]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Request
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            new_obj = Request(argument[1], argument[2], argument[3], argument[4], argument[5], argument[6])
            new_obj.request_id = argument[0]
            return new_obj
        elif isinstance(argument, dict):
            new_obj = Request(argument['priority'], argument['blood'], argument['doctor'], argument['quantity'],
                              argument['status'], argument['date'])
            new_obj.request_id = argument['request_id']
            return new_obj
        raise TypeError

    def to_dict(self):
        return {
            'request_id': self.request_id,
            'priority': self.priority,
            'blood': self.blood,
            'doctor': self.doctor,
            'quantity': self.quantity,
            'status': self.status,
            'date': self.date,
        }

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
        return "Request ID: %-8s | priority: %-8d | " \
               "blood: %-4s | doctor: %-s | quantity: %4f |" \
               "status: %-15s | date: %-30s" % (str(self.request_id), self.priority,
                                                BloodType.to_string[self.blood], self.doctor, self.quantity,
                                                RequestStatus.to_string[self.status], str(self.date))

    def get_db_insert_string(self):
        return "INSERT INTO Requests (Priority, Blood, Doctor, Quantity, Status, Date) VALUES " \
               "(%d, \'%s\', \'%s\', %f, %d, \'%s\')" % \
               (self.priority, self.blood, self.doctor, self.quantity, self.status, self.date)

    def update_id(self, new_id):
        if self.request_id is None:
            self.request_id = new_id

    def get_db_update_string(self, **kwargs):
        res = "UPDATE Requests SET Status=%d WHERE ID=%d" % (kwargs.get('status'), kwargs.get('id'))
        self.status = kwargs.get('status')
        print(res)
        return res
