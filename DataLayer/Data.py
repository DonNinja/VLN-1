from DataLayer.ReadData import ReadData
from ModelClasses.AirplaneModel import Airplane
from ModelClasses.EmployeeModel import Employee
from ModelClasses.FlightModel import Flight
from ModelClasses.LocationModel import Location
from ModelClasses.WorkTripModel import WorkTrip
from DataLayer.registerData import RegisterData
from DataLayer.UpdateData import UpdateData

class DataAPI:
    import csv
    
    def __init__(self, data_list=[]):
        self.__data = []
        self.__reader = ReadData()
        self.__register = RegisterData(data_list)
        self.__updater = UpdateData()
        pass

    def getEmps(self):
        """ Calls a function, which returns the complete list of Crew, then it returns that. """
        return self.__reader.readCrew()
    
    def getAirplanes(self):
        """ Calls a function, which returns the complete list of Airplanes, then it returns that. """
        return self.__reader.readAircraft()

    def registerNewData(self, data_list):
        self.__register.registeremployee(data_list)

    def registerPlanes(self, data_list):
        self.__register.registerPlane(data_list)
    
    def updateEmp(self, data, new_data, field):
        data[field] = new_data
        crew_list = self.__reader.readCrew()
        for item in crew_list:
            if item['ssn'] == data['ssn']:
                item.update(data)
                break
        self.__updater.updateEmployee(crew_list)