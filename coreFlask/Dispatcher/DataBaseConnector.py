import mysql.connector
from mysql.connector import errorcode

from Exception.OperationException import OperationException
from config import DataBaseConfig


class DataBaseConnector:
    def __init__(self):
        self.db_config = {
            'user': DataBaseConfig.user,
            'password': DataBaseConfig.password,
            'host': DataBaseConfig.host,
            'database': DataBaseConfig.database
        }

    def call_procedure(self, procedure_name, arguments=None):
        """ Calls a procedure on the DB

        :param procedure_name:      the name of the procedure
        :param arguments:           the arguments for the procedure

        Handle with care, please check to call the correct arguments

        :type procedure_name: str
        :type arguments: list

        :return:    result of the
        :rtype:     list
        """
        return_obj = []
        try:
            cnx = mysql.connector.connect(**self.db_config)
            cursor = cnx.cursor()
            if arguments is None:
                cursor.callproc(procedure_name)
            else:
                cursor.callproc(procedure_name, arguments)
            for first_table in cursor.stored_results():
                fetched_results = first_table.fetchall()
                for result_row in fetched_results:
                    return_obj.append(result_row)
                break
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                raise err
        except OperationException as err:
            raise err
        else:
            # Successfully executed the insert
            cnx.close()
        return return_obj

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
        # res = self.call_procedure("GetAllDoctors")
        # final_res = []
        # for i in res:
        #     final_res.append(Doctor(i[0], i[1], i[2], i[3]))
        # for i in final_res:
        #     print(i)

        # print(x)
        # self.insert(x)
        # print(x)
        pass


# x123 = DataBaseConnector()
# x123.test()
