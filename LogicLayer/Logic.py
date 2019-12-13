from DataLayer.Data import DataAPI
from LogicLayer.SortData import SortData
from LogicLayer.UserInputCheck import UserInputCheck

class LogicAPI():
    def __init__(self):
        self.__data = DataAPI()
        self.__data_sorter = SortData()
        self.__user_check = UserInputCheck()

    def showAllEmps(self):
        """ This returns a collection of every employee to the UI so it can print them out """
        return self.__data.getEmps()
    
    def showAllPilots(self):
        """ This gets a collection of every employee, then calls a function to sort the collection into a collection of just pilots and returns that """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortPilots(all_emps) # Sorts through all_emps and returns only flight attendants
    
    def showAllAttendants(self):
        """ This gets a collection of every employee, then calls a function to sort the collection into a collection of just flight attendants and returns that """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortAttendants(all_emps) # Sorts through all_emps and returns only flight attendants
    
    def showAllPlanes(self):
        """ This returns a list of every plane so the UI can print them out """
        return self.__data.getAirplanes()
    
    def showPilotSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that is both a pilot and has the inputted SSN and returns him if it finds him, but returns None if he finds nothing """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortPilotSSN(all_emps, ssn)
    
    def showAttendantSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that is both a flight attendant and has the inputted SSN and returns him if it finds him, but returns None if he finds nothing """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortAttendantSSN(all_emps, ssn)
    
    def showEmpSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that has the inputted SSN and returns him, but returns None if he finds nothing """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortEmployeeSSN(all_emps, ssn)
    
    def showPilotByPlane(self, plane_type):
        """ This gets a list of every employee, then cuts it down so it's just pilots who can fly the chose plane type and returns it """
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortPilotsByPlane(all_emps, plane_type)
    
    def showAllLocations(self):
        """ This gets a list of every location and returns it """
        return self.__data.getLocations()

    def addEmpLL(self,data_list):
        """ This calls the dataAPI to add a new employee to the crew.csv file """
        self.__data.registerNewEmp(data_list)

    def addPlane(self,data_list):
        self.__data.registerPlanes(data_list)

    def editPilot(self,ssn):
        all_emps = self.__data.getEmps()
        return self.__data_sorter.sortPilotSSN(all_emps, ssn)

    def checkSSN(self, ssn, data):
        return self.__user_check.checkSSN(ssn, data)

    def checkName(self, name):
        return self.__user_check.checkName(name)
    
    def checkRank(self, rank, emp_type):
        return self.__user_check.checkRank(rank, emp_type)

    def checkEmail(self, email):
        return self.__user_check.checkEmail(email)

    def checkLicens(self, licens):
        return self.__user_check.checkLicens(licens)

    def checkAddress(self,adress):
        return self.__user_check.checkAddress(adress)

    def checkPhone(self, phonenum):
        return self.__user_check.checkPhone(phonenum)

    def updateEmp(self, data, new_data, field):
        """ This calls the dataAPI to update an employee with the new data """
        self.__data.updateEmp(data, new_data, field)

    def showAllWorkTrips(self):
        """ This gets a list of every work trip and returns it """
        return self.__data.getTrips()
    
    def showEmpsWorkTrips(self, ssn):
        ''' This gets a list of all work trips, then calls a function that only returns the flights including the SSN '''
        all_trips = self.__data.getTrips()
        return self.__data_sorter.sortEmpTrips(all_trips, ssn)
        
    def showWorkTripsByDay(self, date):
        '''Gets all trips and sends to get sorted by date input'''
        all_trips = self.__data.getTrips()
        return self.__data_sorter.dateSorter(all_trips, date)

    def addWorkTrip(self,data_list):
        self.__data.registerWorkTrip(data_list)
    
    def showWorkTripsByWeek(self, date):
        all_trips = self.__data.getTrips()
        return self.__data_sorter.weekSorter(all_trips, date)
        
    def sortPilotByPlane(self):
        data_list = self.__data.getEmps()
        return self.__data_sorter.sortOrderByPlane(data_list)
    
    def checkFlightNum(self, num):
        return self.__user_check.checkNum(num)
    
    def sortTrips(self, flight_num_list):
        data_list = self.__data.getTrips()
        return self.__data_sorter.sortForTrip(flight_num_list, data_list)
    
    def addLocation(self, data_list):
        self.__data.registerLocation(data_list)
    
    def checkLocID(self, loc_id):
        data_list = self.showAllLocations()
        return self.__data_sorter.sortForLocation(loc_id, data_list)
    
    def showLocationID(self, loc_id):
        all_locations = self.__data.getLocations()
        return self.__data_sorter.sortForLocation(loc_id, all_locations)
    
    def updateLocation(self, data, new_data, field):
        self.__data.updateLocation(data, new_data, field)