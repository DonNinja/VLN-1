from DataLayer.ReadData import ReadData
from ModelClasses.AirplaneModel import Airplane
from ModelClasses.EmployeeModel import Employee
from ModelClasses.FlightModel import Flight
from ModelClasses.LocationModel import Location
from ModelClasses.WorkTripModel import WorkTrip

class DataAPI:
    def __init__(self):
<<<<<<< HEAD
        self.file_stream = open(".\\STUDENTDATA\\Crew.csv", "r")

    def getEmps(self):
        all_emp_list = []
        for line in self.file_stream:
=======
<<<<<<< HEAD
        self.file_stream_crew = open("STUDENTDATA\\Crew.csv", "r")
        self.file_stream_airplanes = open("STUDENTDATA\\Aircraft.csv", "r")
    def getEmps(self):
        all_emp_list = []
        for line in self.file_stream_crew:
>>>>>>> 65a3c4f0d4ebbd0aa462180a6cb56171adfc89f3
            emp_data_list = line.split(",")
            all_emp_list.append(emp_data_list)
        return all_emp_list

<<<<<<< HEAD
def data_check(data,num):
    self.file_stream = filename
  
    fields = [] 
    rows = [] 
  
    with open(filename, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        fields = next(csvreader)
        for row in csvreader: 
            rows.append(row) 

        for row in rows:
            if row[num] == data:
                return True
=======
    def getAirplanes(self):
        all_airplanes_list = []
        for line in self.file_stream_airplanes:
            airplane_data_list = line.split(",")
            all_airplanes_list.append(airplane_data_list)
        return all_airplanes_list
        
=======
>>>>>>> 65a3c4f0d4ebbd0aa462180a6cb56171adfc89f3
        self.__data = []
        self.__reader = ReadData()
        pass

    def getEmps(self):
        return self.__reader.readCrew()
<<<<<<< HEAD
=======
>>>>>>> 6604364486827ab38cbe5d674908060f39b38ae8
>>>>>>> 65a3c4f0d4ebbd0aa462180a6cb56171adfc89f3
