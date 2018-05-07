class Hospital(object):
    def __init__(self, name, address):
        """
        Constructor for Hospital class

        :param name:        string
        :param address:     string

        :type name str
        :type address str
        """
        self.name = name
        self.address = address

    def __str__(self):
        return "Hospital: %-30s | address: %-30s" % (self.name, self.address)
