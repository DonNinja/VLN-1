from DataLayer.ReadData import ReadData
from ModelClasses.AirplaneModel import Airplane
from ModelClasses.EmployeeModel import Employee
from ModelClasses.FlightModel import Flight
from ModelClasses.LocationModel import Location
from ModelClasses.WorkTripModel import WorkTrip

class DataAPI:
    def __init__(self):
        self.__data = []
        self.__reader = ReadData()
        pass

    def getEmps(self):
        return self.__reader.readCrew()