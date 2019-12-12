import csv
import datetime
class RegisterData:
    def __init__(self,data_list):
        self.data_list = data_list

    def registeremployee(self,data_list):
        """ This gets a data list from the user and writes a new employee into the Crew.csv file with the data in the list """
        self.ssn = data_list[0]
        self.name = data_list[1]
        self.role = data_list[2]
        self.rank = data_list[3]
        self.email = data_list[4]
        self.licence = data_list[5]
        self.address = data_list[6]
        self.mobile_phone_number = data_list[7]
        self.home_phone_number = data_list[8]

        with open("./STUDENTDATA/Crew.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow([self.ssn,self.name,self.role,self.rank,self.email,self.licence,self.address,self.mobile_phone_number,self.home_phone_number])
        file_stream.close()

    def registerPlane(self, data_list):
        """ This gets a data list from the user and writes a new plane into the Aircraft.csv file with the data in the list """
        self.insignia = data_list[0]
        self.planeID = data_list[1]
        with open("./STUDENTDATA/Aircraft.csv", 'a',newline='\n') as file_stream:
            # This opens the file and inserts the plane into it
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow([self.planeID,self.insignia])
        file_stream.close()

    def registerWorkTrip(self, data_list):
        ''' this function registers worktrip with data list and gives new flights a new flight number'''
        counter = 0
        with open("./STUDENTDATA/Flights.csv", 'r') as file_stream: 
            newFileWriter = csv.writer(file_stream)

            for line in file_stream:
                counter = counter + 1
        file_stream.close()
        if counter < 100:
            flightnr = "NA00"+str(counter)
        elif counter < 1000:
            flightnr = "NA0"+str(counter)
        else:
            flightnr = "NA" + str(counter)

        self.flight_num = flightnr
        self.Depfrom = data_list[0]
        self.Arrat = data_list[1]
        self.deptime = data_list[2]
        self.arrtime = data_list[3]
        self.aircID = data_list[4]
        self.capssn = data_list[5]
        self.copssn = data_list[6]
        self.flightsmssn = data_list[7]

        with open("./STUDENTDATA/Flights.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow([self.flight_num,self.Depfrom,self.Arrat,self.deptime,self.arrtime,self.aircID,self.capssn,self.copssn,self.flightsmssn])
        file_stream.close()
        counter = counter+1
        if counter < 100:
            self.flight_num = "NA00"+str(counter)
        elif counter < 1000:
            self.flight_num = "NA0"+str(counter)
        else:
            self.flight_num = "NA" + str(counter)

        self.deptime = self.arrtime + datetime.timedelta(hours=1)
        self.arrtime = self.deptime + data_list[8]
        self.Depfrom = data_list[1]
        self.Arrat = data_list[0]
        
        with open("./STUDENTDATA/Flights.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow([self.flight_num,self.Depfrom,self.Arrat,self.deptime,self.arrtime,self.aircID,self.capssn,self.copssn,self.flightsmssn])
        file_stream.close()

    def registerLocation(self, data_list):
        with open('./STUDENTDATA/Destinations.csv', 'a', newline='\n') as file_stream:
            newFileWriter = csv.writer(file_stream)
            newFileWriter.writerow(data_list)