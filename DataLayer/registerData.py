import csv

class RegisterData:
    def __init__(self,data_list):
        self.data_list = data_list

    def registeremployee(self,data_list):
        self.ssn = data_list[0]
        self.name = data_list[1]
        self.role = data_list[2]
        self.rank = data_list[3]
        self.licence = data_list[4]
        self.address = data_list[5]
        self.mobile_phone_number = data_list[6]
        self.home_phone_number = data_list[7]

        with open("./STUDENTDATA/Crew.csv", 'a',newline='\n') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([self.ssn,self.name,self.role,self.rank,self.licence,self.address,self.mobile_phone_number,self.home_phone_number])

    def registerPlane(self,data_list):
        self.planeID = data_list[0]
        self.insignia = data_list[1]

        with open("./STUDENTDATA/Aircraft.csv", 'a',newline='\n') as newFile:
            newFileWriter = csv.writer(newFile)
            newFileWriter.writerow([self.planeID,self.insignia])


    def editemp(self,data_list):
        lines = []

        with open("./STUDENTDATA/Crew.csv", 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                lines.append(row)
                for field in row:
                    if field == data_list[1]:
                        lines.remove(row)

        with open('mycsv.csv', 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
            
        self.registeremployee(data_list)

   