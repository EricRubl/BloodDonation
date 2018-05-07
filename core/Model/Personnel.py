class Personnel(object):
    def __init__(self, name, email, password):
        """
        Constructor for Personnel class

        :param name:        string
        :param email:       string
        :param password:    must be a sha-256 (string of len 64)
        :type name str
        :type name str
        :type name str
        """
        self.name = name
        self.email = email
        self.password = password

    def __str__(self):
        return "Personnel: %-30s | email: %-30s" % (self.name, self.email)
