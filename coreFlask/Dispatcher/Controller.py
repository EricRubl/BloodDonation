import datetime

from Dispatcher.DataBaseConnector import DataBaseConnector
from Model.Doctor import Doctor
from Model.Donation import Donation
from Model.Donor import Donor
from Model.Hospital import Hospital
from Model.Base import Base
from Model.LabResult import LabResult
from Model.Personnel import Personnel
from Model.Request import Request
from Model.RequestDonation import RequestDonation
from Model.StatusUpdate import StatusUpdate


class Controller:
    def __init__(self):
        """
        TODO documentation
        """
        self.db_connector = DataBaseConnector()

    def get_all_donors(self):
        query_result = self.db_connector.call_procedure("GetAllDonors")
        print(type(query_result))
        for i in query_result:
            i_donor = Donor.new(i)
            print(i_donor.to_dict())

    def get_all_doctor(self):
        query_result = self.db_connector.call_procedure("GetAllDoctors")
        print(type(query_result))
        for i in query_result:
            i_doctor = Doctor.new(i)
            print(i_doctor.to_dict())

    def get_all_donations(self):
        query_result = self.db_connector.call_procedure("GetAllDonations")
        print(type(query_result))
        for i in query_result:
            i_donation = Donation.new(i)
            print(i_donation.to_dict())

    def get_all_hospitals(self):
        query_result = self.db_connector.call_procedure("GetAllHospitals")
        print(type(query_result))
        for i in query_result:
            i_hospital = Hospital.new(i)
            print(i_hospital.to_dict())

    def insert(self, obj):
        """
        Inserts into the DB, using the procedures
        :param obj:     instantiated object subclassing Base
        :type obj:      Base

        :return:
        """
        y = self.db_connector.call_procedure(obj.to_insert_procedure(), obj.to_insert_list())
        if isinstance(y, list) and len(y) == 1:
            # new id received
            print(obj)
            print(y[0][0])
            # update id
            obj.update_id(y[0][0])
            print(obj)
        pass


if __name__ == '__main__':
    ctrl = Controller()
    # ctrl.get_all_donors()
    # ctrl.get_all_doctor()
    # ctrl.get_all_donations()
    # ctrl.get_all_hospitals()
    # x = Hospital("zxc", "qwe")
    # x = Donation("Vlad-Dionisie Potra", "Valera", datetime.datetime.now(), "A+", 0.342,
    #              datetime.datetime.now() + datetime.timedelta(days=3), True)
    # x = Donor('name', (datetime.datetime.now() - datetime.timedelta(days=4000)).date(),
    #           "email", "address", "pass", "A+")
    # x = LabResult(11, True, False, True, False, False)
    # ctrl.insert(x)
    # x = LabResult(11, False, True, False, False, False)
    # ctrl.insert(x)
    # x = LabResult(11, False, False, True, False, False)
    # ctrl.insert(x)
    # x = LabResult(11, False, False, False, True, False)
    # ctrl.insert(x)
    # x = LabResult(11, False, False, False, False, True)
    # x = Request(1, "A+", "Dana Bostana", 9.873, 2, datetime.datetime.now())
    # x = RequestDonation(18, 8)
    x = StatusUpdate(datetime.datetime.now(), 18, 0, 2, "Vitali")
    ctrl.insert(x)
