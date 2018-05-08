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
#
#
# class A(ABC):
#     def __init__(self):
#         self.act1 = 234
#
#     @abstractmethod
#     def down(self):
#         pass
#
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.act1 = 99999
#         self.act2 = 123
#
#     def down(self):
#         print(self.act1, self.act2)
#
#
# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.act2 = {'act3': 123983}
#
#     def down(self):
#         print(self.act1, self.act2)
#
#
# def zxc(param1):
#     """
#
#     :param param1:
#     :type param1: A
#     :return:
#     """
#     pass
#
#
# a = B()
# a.down()
# zxc(a)
#
#
