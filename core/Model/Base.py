from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self):
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
