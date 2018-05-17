from Model.Doctor import *
from Model.Donation import *
from Model.Donor import *
from Model.Hospital import *
from Model.LabResult import *
from Model.Personnel import *
from Model.Request import *
from Model.RequestDonation import *
from Model.StatusUpdate import *


def run_ctor_str():
    doctor = Doctor("name", "email", "password", "str")
    print(doctor)

    donation = Donation("donor", "personnel", datetime.datetime.now(), "A+", datetime.datetime.now(), True)
    print(donation)

    donor = Donor("name", datetime.datetime.now().date(), "email", "address", "password", "AB+")
    print(donor)

    hospital = Hospital("name", "address")
    print(hospital)

    lab_result = LabResult(1, False, True, True, True, True)
    print(lab_result)
    lab_result = LabResult(1, True, False, True, True, True)
    print(lab_result)
    lab_result = LabResult(1, True, True, False, True, True)
    print(lab_result)
    lab_result = LabResult(1, True, True, True, False, True)
    print(lab_result)
    lab_result = LabResult(1, True, True, True, True, False)
    print(lab_result)

    personnel = Personnel("name", "email", "password")
    print(personnel)

    request = Request("normal", "O+", "doctor", 3, "open", datetime.datetime.now())
    print(request)

    request_donation = RequestDonation(12, 13)
    print(request_donation)

    status_update = StatusUpdate(datetime.datetime.now(), 1, 2, 3, "personnel")
    print(status_update)


if __name__ == '__main__':
    run_ctor_str()
