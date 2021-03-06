from Model.Base import Base


class Doctor(Base):
    @staticmethod
    def to_insert_procedure():
        return 'InsertDoctor'

    def to_insert_list(self):
        return [self.name, self.email, self.password, self.hospital]

    @staticmethod
    def new(argument):
        """
        :param argument:    new instance of class Doctor
        :type argument tuple,dict
        :return:
        """
        if isinstance(argument, tuple):
            # must be called only with the tuple returned from the database
            return Doctor(argument[0], argument[1], argument[2], argument[3])
        elif isinstance(argument, dict):
            return Doctor(argument['name'], argument['email'], argument['password'], argument['hospital'])
        raise TypeError

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'hospital': self.hospital,
        }

    def __init__(self, name, email, password, hospital):
        """
        Constructor for Doctor class

        Hospital must exist!

        :param name:        string
        :param email:       string
        :param password:    must be a sha-256 (string of len 64)
        :param hospital     string, FOREIGN KEY

        :type name: str
        :type email: str
        :type password: str
        :type hospital: str
        """
        super().__init__()

        if not isinstance(name, str):
            raise TypeError
        if not isinstance(email, str):
            raise TypeError
        if not isinstance(password, str):
            raise TypeError
        if not isinstance(hospital, str):
            raise TypeError

        self.name = name
        self.email = email
        self.password = password
        self.hospital = hospital

    def __str__(self):
        return "Doctor: %-30s | email: %-30s | password: %-64s | hospital: %-30s" % \
               (self.name, self.email, self.password, self.hospital)

    def update_id(self, new_id):
        pass

    def __eq__(self, other):
        # noinspection PyBroadException
        try:
            if other.name == self.name and \
                    other.email == self.email and \
                    other.password == self.password and \
                    other.hospital == self.hospital:
                return True
            return False
        except Exception:
            return False
