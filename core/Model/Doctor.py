from Model.Base import Base


class Doctor(Base):
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
        self.name = name
        self.email = email
        self.password = password
        self.hospital = hospital

    def __str__(self):
        return "Doctor: %-30s | email: %-30s | hospital: %-30s" % (self.name, self.email, self.hospital)

    def get_db_insert_string(self):
        return "INSERT INTO Doctors (Name, Email, Password, Hospital) VALUES (\'%s\',\'%s\',\'%s\',\'%s\')" % \
               (self.name, self.email, self.password, self.hospital)

    def update_id(self, new_id):
        pass
