import csv
import datetime
class RegisterData:
    def __init__(self,data_list):
        self.data_list = data_list

    def registeremployee(self,data_list):
        """ This gets a data list from the user and writes a new employee into the Crew.csv file with the data in the list """
        with open("./STUDENTDATA/Crew.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it, then insert a newline so we don't write into the same line every time
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            newFileWriter.writerow(data_list) # This writes a new line into the file with the header as keys in a dictionary so it knows what the appropriate data is
        file_stream.close() # We close the file so it isn't taking up our precious resources

    def registerPlane(self, data_list):
        """ This gets a data list from the user and writes a new plane into the Aircraft.csv file with the data in the list """
        with open("./STUDENTDATA/Aircraft.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the plane into it, then insert a newline so we don't write into the same line every time
            # This opens the file and inserts the plane into it
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            newFileWriter.writerow(data_list) # This writes a new line into the file with the header as keys in a dictionary so it knows what the appropriate data is
        file_stream.close() # We close the file so it isn't taking up our precious resources

    def registerWorkTrip(self, data_list):
        ''' this function registers worktrip with data list and gives new flights a new flight number'''
        counter = 0
        with open("./STUDENTDATA/Flights.csv", 'r') as file_stream:  # This opens the file and counts the line amount
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            for line in file_stream:
                counter += 1 # So we have the flight number as well
        file_stream.close() # We close the file so it isn't taking up our precious resources
        if counter < 100:
            flightnr = "NA00"+str(counter)
        elif counter < 1000:
            flightnr = "NA0"+str(counter)
        else:
            flightnr = "NA" + str(counter) # This is just to set the correct format for the flight number

        self.flight_num = flightnr # This sets the flight number
        self.Depfrom = data_list[0] # This sets the departure location ID
        self.Arrat = data_list[1] # This sets the arrival location ID
        self.deptime = data_list[2] # This sets the departure time
        self.arrtime = data_list[3] # This sets the arrival time
        self.aircID = data_list[4] # This sets the plane insignia
        self.capssn = data_list[5] # This sets the captain's SSN
        self.copssn = data_list[6] # This sets the copilot's SSN
        self.flightsmssn = data_list[7] # This sets the flight service manager's SSN
        self.flight_fa1 = data_list[8] # This sets the first flight attendant's SSN
        self.flight_fa2 = data_list[9] # This sets the second flight attendant's SSN
        self.ret_dep_time = data_list[10] # This sets the return departure time
        self.ret_arr_time = data_list[11] # This sets the return arrival time
        self.fully_manned = data_list[12] # This set if the flight is fully manned or not (Y/N)

        with open("./STUDENTDATA/Flights.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            newFileWriter.writerow([self.flight_num, self.Depfrom, self.Arrat, self.deptime, self.arrtime, self.aircID, self.capssn, self.copssn, self.flightsmssn, self.flight_fa1, self.flight_fa2, self.fully_manned]) # This writes a new line into the file with the header as keys in a dictionary so it knows what the appropriate data is
        file_stream.close() # We close the file so it isn't taking up our precious resources
        counter = counter+1
        if counter < 100:
            self.flight_num = "NA00"+str(counter)
        elif counter < 1000:
            self.flight_num = "NA0"+str(counter)
        else:
            self.flight_num = "NA" + str(counter) # This is just to set the correct format for the returning flight number

        self.Depfrom = data_list[1] # This switches the departure and arrival locations for the return trip
        self.Arrat = data_list[0] # This switches the departure and arrival locations for the return trip

        with open("./STUDENTDATA/Flights.csv", 'a',newline='\n') as file_stream: # This opens the file and inserts the user into it
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            newFileWriter.writerow([self.flight_num, self.Depfrom, self.Arrat, self.ret_dep_time, self.ret_arr_time, self.aircID, self.capssn, self.copssn, self.flightsmssn, self.flight_fa1, self.flight_fa2, self.fully_manned]) # This writes a new line into the file with the header as keys in a dictionary so it knows what the appropriate data is
        file_stream.close() # We close the file so it isn't taking up our precious resources

    def registerLocation(self, data_list):
        with open('./STUDENTDATA/Destinations.csv', 'a', newline='\n') as file_stream:
            newFileWriter = csv.writer(file_stream) # This is a writer that is able to write into the file
            newFileWriter.writerow(data_list) # This writes a new line into the file with the header as keys in a dictionary so it knows what the appropriate data is