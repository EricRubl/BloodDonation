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


def run_ctor_new():
    doctor = Doctor("name", "email", "password", "str")
    doctor2 = Doctor.new(("name", "email", "password", "str"))
    print(doctor)
    print(doctor2)
    print(doctor == doctor2)

    datetime1 = datetime.datetime.now()
    datetime2 = datetime.datetime(year=2010, month=1, day=1)

    donation = Donation("donor", "personnel", datetime1, "A+", datetime2, True)
    donation2 = Donation.new((None, "donor", "personnel", datetime1, "A+", datetime2, True))
    print(donation)
    print(donation2)
    print(donation == donation2)

    donor = Donor("name", datetime.datetime.now().date(), "email", "address", "password", "AB+")
    donor2 = Donor.new(("name", datetime.datetime.now().date(), "email", "address", "password", "AB+"))
    print(donor)
    print(donor2)
    print(donor == donor2)

    hospital = Hospital("name", "address")
    hospital2 = Hospital.new(("name", "address"))
    print(hospital)
    print(hospital2)
    print(hospital == hospital2)

    lab_result = LabResult(1, False, True, True, True, True)
    lab_result2 = LabResult.new((1, False, True, True, True, True))
    print(lab_result)
    print(lab_result2)
    print(lab_result == lab_result2)

    personnel = Personnel("name", "email", "password")
    personnel2 = Personnel.new(("name", "email", "password"))
    print(personnel)
    print(personnel2)
    print(personnel == personnel2)

    request = Request("normal", "O+", "doctor", 3, "open", datetime1)
    request2 = Request.new((None, "normal", "O+", "doctor", 3, "open", datetime1))
    print(request)
    print(request2)
    print(request == request2)

    request_donation = RequestDonation(12, 13)
    request_donation2 = RequestDonation.new((12, 13))
    print(request_donation)
    print(request_donation2)
    print(request_donation == request_donation2)

    status_update = StatusUpdate(datetime1, 1, 2, 3, "personnel")
    status_update2 = StatusUpdate.new((datetime1, 1, 2, 3, "personnel"))
    print(status_update)
    print(status_update2)
    print(status_update == status_update2)


if __name__ == '__main__':
    run_ctor_str()
    run_ctor_new()
