CREATE TABLE Donors
(
    Name NVARCHAR(30) PRIMARY KEY NOT NULL,
    DOB DATE NOT NULL,
    Email NVARCHAR(30) NOT NULL,
    Address NVARCHAR(50) NOT NULL,
    Password VARCHAR(64) NOT NULL,
    Blood VARCHAR(4) NOT NULL
);


CREATE TABLE Doctors
(
    Name NVARCHAR(30) PRIMARY KEY NOT NULL,
    Email NVARCHAR(30) NOT NULL,
    Password VARCHAR(64) NOT NULL
);


CREATE TABLE Personnel
(
    Name NVARCHAR(30) PRIMARY KEY NOT NULL,
    Email NVARCHAR(30) NOT NULL,
    Password VARCHAR(64) NOT NULL
);


CREATE TABLE Donations
(
    ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Donor NVARCHAR(30) NOT NULL,
    Personnel NVARCHAR(30) NOT NULL,
    Date DATE NOT NULL,
    Blood VARCHAR(4) NOT NULL,
    Quantity FLOAT NOT NULL,
    CONSTRAINT Donations_Donors FOREIGN KEY (Donor) REFERENCES Donors (Name) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT Donations_Personnel FOREIGN KEY (Personnel) REFERENCES Personnel (Name) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE LabResults
(
    Donation INT NOT NULL,
    Syph BIT NOT NULL,
    HBV BIT NOT NULL,
    HIV BIT NOT NULL,
    HEV BIT NOT NULL,
    HTLV BIT NOT NULL,
    CONSTRAINT LabResults_Donations FOREIGN KEY (Donation) REFERENCES Donations (ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE Requests
(
    ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    Priority INT NOT NULL,
    Blood VARCHAR(4) NOT NULL,
    Doctor NVARCHAR(30) NOT NULL,
    Quantity FLOAT NOT NULL,
    Status INT NOT NULL,
    CONSTRAINT Requests_Doctors FOREIGN KEY (Doctor) REFERENCES Doctors (Name) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE RequestDonations
(
    Request INT NOT NULL,
    Donation INT NOT NULL,
    CONSTRAINT RequestDonations_PK PRIMARY KEY (Request, Donation),
    CONSTRAINT RequestDonations_Requests FOREIGN KEY (Request) REFERENCES Requests (ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT RequestDonations_Donations FOREIGN KEY (Donation) REFERENCES Donations (ID) ON DELETE CASCADE ON UPDATE CASCADE
);


CREATE TABLE StatusUpdates
(
    Date DATE NOT NULL,
    Request INT NOT NULL,
    Previous INT NOT NULL,
    Current INT NOT NULL,
    Personnel NVARCHAR(30) NOT NULL,
    CONSTRAINT StatusUpdates_Requests FOREIGN KEY (Request) REFERENCES Requests (ID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT StatusUpdates_Personnel FOREIGN KEY (Personnel) REFERENCES Personnel (Name) ON DELETE CASCADE ON UPDATE CASCADE
);