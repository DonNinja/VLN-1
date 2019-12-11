import csv

class RegisterData:
    def __init__(self,data_list):
        self.data_list = data_list

    def registeremployee(self,data_list):
        self.ssn = data_list[0]
        self.name = data_list[1]
        self.role = data_list[2]
        self.rank = data_list[3]
        self.email = data_list[4]
        self.licence = data_list[5]
        self.address = data_list[6]
        self.mobile_phone_number = data_list[7]
        self.home_phone_number = data_list[8]

        with open("./STUDENTDATA/Crew.csv", 'a',newline='\n') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([self.ssn,self.name,self.role,self.rank,self.email,self.licence,self.address,self.mobile_phone_number,self.home_phone_number])

    def registerPlane(self, data_list):
        self.insignia = data_list[0]
        self.planeID = data_list[1]

        with open("./STUDENTDATA/Aircraft.csv", 'a',newline='\n') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([self.planeID,self.insignia])
