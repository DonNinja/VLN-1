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

    def updateWorkTrip(self, data):
    ''' This writes every value of the data into the crew file again, updating it. '''
    with open("./STUDENTDATA/Flights.csv", 'w',newline='\n') as file_stream:
        newFileWriter = csv.writer(file_stream)
        newFileWriter.writerow(['flightNumber', 'departingFrom', 'arrivingAt', 'departure', 'arrivial', 'aircraftID', 'captain', 'copilot', 'fsm', 'fa1', 'fa2'])
        for item in data:
            self.flightNumber = item['flightNumber']
            self.departingFrom = item['departingFrom']
            self.arrivingAt = item['arrivingAt']
            self.departure = item['departure']
            self.arrival = item['arrival']
            self.aircraftID = item['aircraftID']
            self.captain = item['captain']
            self.copilot = item['copilot']
            self.fsm = item['fsm']
            self.fa1 = item['fa1']
            self.fa2 = item['fa2']
            
            newFileWriter.writerow([self.flightNumber,self.departingFrom,self.arrivingAt,self.departure,self.arrival,self.aircraftID,self.captain,self.copilot,self.fsm, self.fa1, self.fa2])
    file_stream.close()