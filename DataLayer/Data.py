from DataLayer.ReadData import ReadData
from ModelClasses.AirplaneModel import Airplane
from ModelClasses.EmployeeModel import Employee
from ModelClasses.FlightModel import Flight
from ModelClasses.LocationModel import Location
from ModelClasses.WorkTripModel import WorkTrip

class DataAPI:
    def __init__(self):
        self.file_stream = open(".\\STUDENTDATA\\Crew.csv", "r")
        self.file_stream_crew = open(".\\STUDENTDATA\\Crew.csv", "r")
        self.file_stream_airplanes = open(".\\STUDENTDATA\\Aircraft.csv", "r")


    def getEmps(self):
        all_emp_list = []
        for line in self.file_stream_crew:
            emp_data_list = line.split(",")
            all_emp_list.append(emp_data_list)
        return all_emp_list

    def getAirplanes(self):
        all_airplanes_list = []
        for line in self.file_stream_airplanes:
            airplane_data_list = line.split(",")
            all_airplanes_list.append(airplane_data_list)
        return all_airplanes_list
        
        self.__data = []
        self.__reader = ReadData()
        pass

    def getEmps(self):
        return self.__reader.readCrew()

