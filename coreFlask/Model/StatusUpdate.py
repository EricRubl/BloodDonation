from Exception.OperationException import OperationException
from Model.Base import Base


class StatusUpdate(Base):
    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class StatusUpdate
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            return StatusUpdate(argument[0], argument[1], argument[2], argument[3], argument[4])
        elif isinstance(argument, dict):
            return StatusUpdate(argument['date'], argument['request_id'], argument['previous'],
                                argument['current'], argument['personnel_id'])
        raise TypeError

    def to_dict(self):
        return {
            'date': self.date,
            'request_id': self.request_id,
            'previous': self.previous,
            'current': self.current,
            'personnel_id': self.personnel_id,
        }

    def __init__(self, date, request_id, previous, current, personnel_id):
        """
        Constructor for StatusUpdate class

        * for logs

        :param date:            when the update happened
        :param request_id:      int
        :param previous:        int
        :param current:         int
        :param personnel_id:

        :type date: datetime.datetime
        :type request_id: int
        :type previous: int
        :type current: int
        :type personnel_id: str
        """
        super().__init__()
        self.date = date
        self.request_id = request_id
        self.previous = previous
        self.current = current
        self.personnel_id = personnel_id

    def __str__(self):
        return "Status update at: %-30s | previous: %-10s | current: %-10s | Request: %-8d | Personnel: %-30s" % \
               (str(self.date), self.previous, self.current, self.request_id, self.personnel_id)

    def get_db_insert_string(self):
        return "INSERT INTO StatusUpdates (Date, Request, Previous, Current, Personnel) VALUES " \
               "(\'%s\', %d, %d, %d, \'%s\')" % \
               (str(self.date), self.request_id, self.previous, self.current, self.personnel_id)

    def update_id(self, new_id):
        pass

    def get_db_update_string(self, **kwargs):
        raise OperationException('Operation not allowed!')
