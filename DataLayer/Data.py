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

    def registerNewEmp(self, data_list):
        self.__register.registeremployee(data_list)

    def registerPlanes(self, data_list):
        self.__register.registerPlane(data_list)
    
    def updateEmp(self, data, new_data, field):
        ''' This replaces the old employee item with a new, updated item '''
        data[field] = new_data
        crew_list = self.__reader.readCrew()
        for item in crew_list:
            if item['ssn'] == data['ssn']:
                item.update(data)
                break
        self.__updater.updateEmployee(crew_list)
    
    def getLocations(self):
        """ Returns a list of items of every destination """
        return self.__reader.readDestinations()
    
    def getTrips(self):
        ''' Returns a list of every flight '''
        return self.__reader.readAllFlights()

    def registerWorkTrip(self,data_list):
        self.__register.registerWorkTrip(data_list)

    def registerLocation(self, data_list):
        self.__register.registerLocation(data_list)
    
    def updateLocation(self, data, new_data, field):
        data[field] = new_data
        loc_list = self.__reader.readDestinations()
        for item in loc_list:
            if item['id'] == data['id']:
                item.update(data)
                break
        self.__updater.updateLocation(loc_list)