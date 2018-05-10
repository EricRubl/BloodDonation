from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def to_insert_list(self):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        :return: necessary arguments for insert procedures in DB
        """
        pass

    @staticmethod
    @abstractmethod
    def new(argument):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        if argument is tuple, it MUST respect the order from the DB (check the tables)
        if argument is dict, it MUST have all the fields available for the required object
        :type argument dict,tuple
        :return: a new object from
        """
        pass

    @abstractmethod
    def to_dict(self):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        :return subclassed object at dictionary
        :rtype  dict
        """
        pass

    @abstractmethod
    def get_db_insert_string(self):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        :return: query string for cursor
            example: 'INSERT INTO ...'
        """
        pass

    @abstractmethod
    def get_db_update_string(self, **kwargs):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        :return: query string for cursor
            example: 'UPDATE `Table` SET ...'
        """
        pass

    @abstractmethod
    def update_id(self, new_id):
        """
        Abstract method
        Must be implemented in all the classes that have a table in the DB
        :return: None
        """
        pass

    @staticmethod
    @abstractmethod
    def to_insert_procedure():
        """

        :return:
        """
        pass
