import datetime
from Utils.BloodType import BloodType
from Utils.Priority import Priority
from Utils.RequestStatus import RequestStatus
from Model.Base import Base


class Request(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertRequest'

    def to_insert_list(self):
        return [self.priority, self.blood, self.doctor, self.quantity, self.status, self.date]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Request
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            # check blood
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
            'priority': Priority.to_string[self.priority],
            'blood': BloodType.to_string[self.blood],
            'doctor': self.doctor,
            'quantity': self.quantity,
            'status': RequestStatus.to_string[self.status],
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

        :type priority: int, str
        :type blood: str, int
        :type doctor: str
        :type quantity: float
        :type status: str, int
        :type date: datetime.datetime
        """
        super().__init__()

        if not isinstance(priority, str) and not isinstance(priority, int):
            raise TypeError
        if isinstance(priority, str) and priority not in Priority.to_code:
            raise TypeError
        if not isinstance(blood, str) and not isinstance(blood, int):
            raise TypeError
        if isinstance(blood, str) and blood not in BloodType.to_code:
            raise TypeError
        if not isinstance(doctor, str):
            raise TypeError
        if not isinstance(quantity, float):
            raise TypeError
        if not isinstance(status, str) and not isinstance(status, int):
            raise TypeError
        if isinstance(status, str) and status not in RequestStatus.to_code:
            raise TypeError

        self.request_id = None
        self.doctor = doctor
        self.quantity = quantity
        self.date = date

        blood = int(blood)
        self.priority = Priority.to_code[priority] if isinstance(priority, str) else priority
        self.blood = BloodType.to_code[blood] if isinstance(blood, str) else blood
        self.status = RequestStatus.to_code[status] if isinstance(status, str) else status

    def __str__(self):
        return "Request ID: %-8s | priority: %-8s | " \
               "blood: %-4d | doctor: %-30s | quantity: %-4s |" \
               "status: %-4d | date: %-30s" % (str(self.request_id), str(self.priority),
                                               self.blood, self.doctor, str(self.quantity),
                                               self.status, str(self.date))

    def update_id(self, new_id):
        if self.request_id is None:
            self.request_id = new_id
