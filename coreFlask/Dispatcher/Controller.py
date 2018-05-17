import datetime
import json

import mysql.connector

from Dispatcher.DataBaseConnector import DataBaseConnector
from Model.Base import Base
from Model.Doctor import Doctor
from Model.Donation import Donation
from Model.Donor import Donor
from Model.Hospital import Hospital
from Model.LabResult import LabResult
from Model.Personnel import Personnel
from Model.Request import Request
from Model.StatusUpdate import StatusUpdate
from Utils.RequestStatus import RequestStatus


class Controller:
    def __init__(self):
        """
        TODO documentation
        """
        self.db_connector = DataBaseConnector()

    def move_donation_to_bank(self, donation_id):
        try:
            query_result = self.db_connector.call_procedure("GetDonationByID", [donation_id])
            if len(query_result) is not 0:
                query_result = self.db_connector.call_procedure("GetLabResultByDonation", [donation_id])
                if len(query_result) is not 0:
                    lab_result = LabResult.new(query_result[0])
                    if lab_result.syph or lab_result.HBV or lab_result.HIV or lab_result.HEV or lab_result.HTLV:
                        return 'Bad LabResult'
                else:
                    return 'No LabResult'
            else:
                return 'Invalid DonationID'
            self.db_connector.call_procedure("InsertLabResult", [donation_id])
        except mysql.connector.Error:
            return 'Error!'

    def insert_lab_result(self, donation_id, syph, hbv, hiv, hev, htlv):
        try:
            self.db_connector.call_procedure("InsertLabResult", [donation_id, bool(int(syph)), bool(int(hbv)),
                                                                 bool(int(hiv)), bool(int(hev)), bool(int(htlv))])
        except mysql.connector.Error:
            return 'Error!'

    def get_requests_by_id(self, request_id):
        query_result = self.db_connector.call_procedure("GetRequestByID", [request_id])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_request = Request.new(i)
            i_dict = i_request.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def update_request_status(self, request_id=None, previous=None, current=None, personnel=None, date=None):
        try:
            self.db_connector.call_procedure("UpdateRequestStatus", [request_id, RequestStatus.to_code[previous],
                                                                     current, personnel, date])
        except mysql.connector.Error:
            return 'Error!'

    def get_donations_in_bank(self):
        query_result = self.db_connector.call_procedure("GetDonationsInBank")
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_donation = Donation.new(i)
            i_dict = i_donation.to_dict()
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
            print("debug:", i, type(i))
            i_donation = Donation.new(i)
            i_dict = i_donation.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_personnel_by_name(self, personnel_name):
        query_result = self.db_connector.call_procedure("GetPersonnelByName", [personnel_name])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_personnel = Personnel.new(i)
            i_dict = i_personnel.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def update_request_priority(self, request_id=None, new_priority=None):
        try:
            self.db_connector.call_procedure("UpdateRequestPriority", [int(request_id), int(new_priority)])
        except mysql.connector.Error:
            return 'Error!'

    # TODO date parsing
    def insert_new_request(self, doctor_name, priority=None, blood=None, quantity=None, status=None, date=None):
        # print(blood, type(blood))
        # blood = BloodType.to_string[int(blood)]
        new_request = Request(priority, blood, doctor_name, quantity, status, date)
        self.insert(new_request)
        # self.db_connector.call_procedure("InsertRequest",
        #                             [int(priority), blood, doctor_name, float(quantity), int(status), date])
        # json_object = []
        # for i in query_result:
        #     i_request = Request.new(i)
        #     i_dict = i_status_update.to_dict()
        #     for key in i_dict:
        #         if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
        #             i_dict[key] = i_dict[key].isoformat()
        #     json_object.append(i_dict)
        # json_object = json.dumps(json_object, ensure_ascii=False)
        # return json_object

    def get_status_updates_by_request(self, request_id=None):
        query_result = self.db_connector.call_procedure("GetStatusUpdateByReqID", [int(request_id)])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_status_update = StatusUpdate.new(i)
            i_dict = i_status_update.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_requests_by_doctor(self, doctor_name):
        query_result = self.db_connector.call_procedure("GetRequestsByDoctor", [doctor_name])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_request = Request.new(i)
            i_dict = i_request.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_doctor_by_name(self, doctor_name):
        query_result = self.db_connector.call_procedure("GetDoctorByName", [doctor_name])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_doctor = Doctor.new(i)
            i_dict = i_doctor.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_lab_results_by_donation(self, donation_id):
        query_result = self.db_connector.call_procedure("GetLabResultByDonation", [donation_id])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_lab_result = LabResult.new(i)
            i_dict = i_lab_result.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_donations_by_donor(self, donor_name):
        query_result = self.db_connector.call_procedure("GetDonationsByDonor", [donor_name])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_donation = Donation.new(i)
            i_dict = i_donation.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_donor_by_name(self, donor_name):
        query_result = self.db_connector.call_procedure("GetDonorByName", [donor_name])
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
            i_donor = Donor.new(i)
            i_dict = i_donor.to_dict()
            for key in i_dict:
                if isinstance(i_dict[key], datetime.datetime) or isinstance(i_dict[key], datetime.date):
                    i_dict[key] = i_dict[key].isoformat()
            json_object.append(i_dict)
        json_object = json.dumps(json_object, ensure_ascii=False)
        return json_object

    def get_all_donors(self):
        query_result = self.db_connector.call_procedure("GetAllDonors")
        json_object = []
        for i in query_result:
            print("debug:", i, type(i))
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
            print("debug:", i, type(i))
            i_doctor = Doctor.new(i)
            i_dict = i_doctor.to_dict()
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
            print("debug:", i, type(i))
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
            print("debug:", i, type(i))
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
            print("debug:", i, type(i))
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
            # update id
            obj.update_id(y[0][0])
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
