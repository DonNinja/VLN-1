from DataLayer.ReadData import ReadData
from ModelClasses.AirplaneModel import Airplane
from ModelClasses.EmployeeModel import Employee
from ModelClasses.FlightModel import Flight
from ModelClasses.LocationModel import Location
from ModelClasses.WorkTripModel import WorkTrip

class DataAPI:
    def __init__(self):
<<<<<<< HEAD
        self.file_stream = open("VLN-1/STUDENTDATA/Crew.csv", "r")

    def getEmps(self):
        all_emp_list = []
        for line in self.file_stream:
            emp_data_list = line.split(",")
            all_emp_list.append(emp_data_list)
        return all_emp_list

def data_check(data,num):
    filename = "Crew.csv"
  
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
        self.__data = []
        self.__reader = ReadData()
        pass

    def getEmps(self):
        return self.__reader.readCrew()
>>>>>>> 6604364486827ab38cbe5d674908060f39b38ae8
