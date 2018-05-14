import datetime
import json

from Dispatcher.DataBaseConnector import DataBaseConnector
from Model.Base import Base
from Model.Doctor import Doctor
from Model.Donation import Donation
from Model.Donor import Donor
from Model.Hospital import Hospital
from Model.Personnel import Personnel
from Model.Request import Request
from Model.StatusUpdate import StatusUpdate


class Controller:
    def __init__(self):
        """
        TODO documentation
        """
        self.db_connector = DataBaseConnector()

    def get_all_donors(self):
        query_result = self.db_connector.call_procedure("GetAllDonors")
        json_object = []
        for i in query_result:
            i_donor = Donor.new(i)
            i_dict = i_donor.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_doctors(self):
        query_result = self.db_connector.call_procedure("GetAllDoctors")
        json_object = []
        for i in query_result:
            i_doctor = Doctor.new(i)
            i_dict = i_doctor.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_donations(self):
        query_result = self.db_connector.call_procedure("GetAllDonations")
        json_object = []
        for i in query_result:
            i_donation = Donation.new(i)
            i_dict = i_donation.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_hospitals(self):
        query_result = self.db_connector.call_procedure("GetAllHospitals")
        json_object = []
        for i in query_result:
            i_hospital = Hospital.new(i)
            i_dict = i_hospital.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_requests(self):
        query_result = self.db_connector.call_procedure("GetAllRequests")
        json_object = []
        for i in query_result:
            i_request = Request.new(i)
            i_dict = i_request.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_status_updates(self):
        query_result = self.db_connector.call_procedure("GetAllStatusUpdates")
        json_object = []
        for i in query_result:
            i_status_update = StatusUpdate.new(i)
            i_dict = i_status_update.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

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

    # LOGIN methods
    def get_user_password(self, username):
        query_result = self.db_connector.call_procedure("GetDonorByName", [username])
        if len(query_result) == 1:
            user = Donor.new(query_result[0]).to_dict()
            return user['password']
        query_result = self.db_connector.call_procedure("GetDoctorByName", [username])
        if len(query_result) == 1:
            user = Doctor.new(query_result[0]).to_dict()
            return user['password']
        query_result = self.db_connector.call_procedure("GetPersonnelByName", [username])
        if len(query_result) == 1:
            user = Personnel.new(query_result[0]).to_dict()
            return user['password']
        return None

    def get_user_type(self, username, password):
        query_result = self.db_connector.call_procedure("GetDonorByName", [username])
        if len(query_result) == 1:
            user = Donor.new(query_result[0]).to_dict()
            if user['password'] == password:
                return 'Donor'
        query_result = self.db_connector.call_procedure("GetDoctorByName", [username])
        if len(query_result) == 1:
            user = Doctor.new(query_result[0]).to_dict()
            if user['password'] == password:
                return 'Doctor'
        query_result = self.db_connector.call_procedure("GetPersonnelByName", [username])
        if len(query_result) == 1:
            user = Personnel.new(query_result[0]).to_dict()
            if user['password'] == password:
                return 'Personnel'
        return None


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
    # x = StatusUpdate(datetime.datetime.now(), 18, 0, 2, "Vitali")
    # ctrl.insert(x)
    ctrl.get_all_status_updates()
