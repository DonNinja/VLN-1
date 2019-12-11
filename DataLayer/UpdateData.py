import csv

class UpdateData:
    def __init__(self):
        self.__data = []

    def updateEmployee(self, data):
        ''' This writes every value of the data into the crew file again, updating it. '''
        with open("./STUDENTDATA/Crew.csv", 'w',newline='\n') as file_stream:
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow(['ssn', 'name', 'role', 'rank', 'email', 'licence', 'address', 'mobilephonenumber', 'homephonenumber'])
            for item in data:
                self.ssn = item['ssn']
                self.name = item['name']
                self.role = item['role']
                self.rank = item['rank']
                self.email = item['email']
                self.licence = item['licence']
                self.address = item['address']
                self.mobile_phone_number = item['mobilephonenumber']
                self.home_phone_number = item['homephonenumber']
                
                newFileWriter.writerow([self.ssn,self.name,self.role,self.rank,self.email,self.licence,self.address,self.mobile_phone_number,self.home_phone_number])
        file_stream.close()