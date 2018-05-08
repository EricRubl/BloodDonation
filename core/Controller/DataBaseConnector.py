import datetime
from time import sleep

import mysql.connector
from mysql.connector import errorcode

from Model.RequestDonation import RequestDonation
from Model.Donation import Donation
from Model.LabResult import LabResult
from Model.Personnel import Personnel
from Model.Doctor import Doctor
from Model.Donor import Donor
from Model.Hospital import Hospital
from Model.Request import Request
from Model.StatusUpdate import StatusUpdate
from config import DataBaseConfig
from Model.Base import Base


class DataBaseConnector:
    def __init__(self):
        self.db_config = {
            'user': DataBaseConfig.user,
            'password': DataBaseConfig.password,
            'host': DataBaseConfig.host,
            'database': DataBaseConfig.database
        }

    def insert(self, obj):
        """
        Inserts any object into the database

            obj will be modified, assigning automatically the id set by the db (helps if the id is auto increment,
        and not set by the user), useless if the PK is set by the user.

        :param obj: must be a subclassed object from Base class, meaning one from Model package
        :type obj:  Base
        :return:
        """
        try:
            cnx = mysql.connector.connect(**self.db_config)
            cursor = cnx.cursor()
            query = obj.get_db_insert_string()
            cursor.execute(query)

            cursor.execute('SELECT LAST_INSERT_ID()')
            result_set = cursor.fetchall()
            new_id = result_set[0][0]

            obj.update_id(new_id)
            cursor.close()
            cnx.commit()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                raise err
        else:
            # Successfully executed the insert
            cnx.close()

    def test(self):
        # h = Hospital("asdasdasd", "zxczxczxc")
        # d = Donor("zxcasd", datetime.date(year=2010, month=2, day=15), "eee", "address", "asdasdasdasd", 1)
        # d = Doctor("name", "email", "password", "SJU Cluj")
        # l = Personnel("Valera", "asdasdzxc", "vyvghhbuihyutvgyh")
        # d = Donation("Vlad-Dionisie Potra", "Valera", datetime.datetime.now(), "A+", 12.23,
        #              datetime.datetime.now() + datetime.timedelta(days=365))
        # l = LabResult(8, True, True, False, True, False)

        # r = Request(2, 2, "Dana Bostana", 11.32, 2, datetime.datetime.now())
        # x = RequestDonation(17, 8)
        # x = StatusUpdate(datetime.datetime.now(), 17, 0, 3, "Valera")
        # self.insert(r)
        # print(r)
        try:
            cnx = mysql.connector.connect(**self.db_config)
            cursor = cnx.cursor()
            obj = Request(2, 2, "Dana Bostana", 11.32, 2, datetime.datetime.now())
            obj.request_id = 17

            query = obj.get_db_update_string(id=17, status=3)
            cursor.execute(query)

            # cursor.execute('SELECT LAST_INSERT_ID()')
            # result_set = cursor.fetchall()
            # new_id = result_set[0][0]

            # obj.update_id(new_id)
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                raise err
        else:
            # Successfully executed the insert
            cnx.close()

        # print(x)
        # self.insert(x)
        # print(x)


x123 = DataBaseConnector()
x123.test()
