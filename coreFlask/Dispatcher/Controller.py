from Dispatcher.DataBaseConnector import DataBaseConnector
from Model.Doctor import Doctor
from Model.Donation import Donation
from Model.Donor import Donor
from Model.Hospital import Hospital


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

    def insert_hospital(self, obj):
        self.db_connector.call_procedure("InsertHospital")
        pass


if __name__ == '__main__':
    ctrl = Controller()
    # ctrl.get_all_donors()
    # ctrl.get_all_doctor()
    # ctrl.get_all_donations()
    # ctrl.get_all_hospitals()
    ctrl.insert_hospital("asd")
