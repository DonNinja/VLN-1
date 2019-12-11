from LogicLayer.Logic import LogicAPI
from UILayer.UserInput import UserInput
from UILayer.UIDataPrinter import UIDataPrinter
from UILayer.UIPrinter import UIPrinter

class UIAPI:
    def __init__(self):
        self.__logic = LogicAPI()
        self.__inputter = UserInput()
        self.__data_printer = UIDataPrinter()
        self.__ui_printer = UIPrinter()

    def UIDisplay(self, choice_list):
        """ This calls the printer to print out the current screen for the user """
        self.__ui_printer.display(choice_list)
    
    def UIHeaderDisplay(self, title):
        """ This calls the printer to print out the header for the current screen """
        self.__ui_printer.headerDisplay(title)
    
    def addEmp(self, role):
        """ This calls the inputter so the user can input the employee's data, then calls logicAPI to add it to the file """
        data_list = self.__inputter.addEmp(role)
        self.__logic.addEmpLL(data_list)
    
    def addPlane(self):
        """ This calls the inputter so the user can input the plane's data, then calls logicAPI to add it to the file """
        data_list = self.__inputter.addPlane()
        self.__logic.addPlane(data_list)
    
    def addLocation(self):
        """ This calls the inputter so the user can input the location's data, then calls logicAPI to add it to the file """
        data_list = self.__inputter.addLocation()
        # self.__logic
    
    def showAllEmps(self):
        """ This gets a list of every employee from logicAPI, then calls the printer to print out every employee for the user """
        data_list = self.__logic.showAllEmps()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllPilots(self):
        """ This gets a list of every pilot from logicAPI, then calls the printer to print out every pilot for the user """
        data_list = self.__logic.showAllPilots()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllAttendants(self):
        """ This gets a list of every flight attendant from logicAPI, then calls the printer to print out every flight attendant for the user """
        data_list = self.__logic.showAllAttendants()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllPlanes(self):
        """ This gets a list of every plane from logicAPI, then calls the printer to print out every plane for the user """
        data_list = self.__logic.showAllPlanes()
        self.__data_printer.printAllPlanes(data_list)
    
    def showPilotsForPlane(self, plane_type):
        """ This gets a list of every pilot with a license for the plane type from logicAPI, then calls the printer to print them out """
        data_list = self.__logic.showPilotByPlane(plane_type)
        self.__data_printer.printPilotForPlane(data_list)
    
    def showSpecificEmp(self, ssn):
        """ This gets a single employee with the inputted SSN and calls the pirnter to print them out """
        emp = self.__logic.showEmpSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp
    
    def showSpecificPilot(self, ssn):
        """ This gets a single pilot and calls the printer to print them out """
        emp = self.__logic.showPilotSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp
    
    def showSpecificAttendant(self, ssn):
        """ This gets a single attendant and calls the printer to print them out """
        emp = self.__logic.showAttendantSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp

    def editEmail(self, data):
        """ This calls the inputter and calls logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('email')
        self.__logic.updateEmp(data, new_var, 'email')
        self.showSpecificEmp(data['ssn'])

    def editAddress(self, data):
        """ This calls the inputter and calls logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('address')
        self.__logic.updateEmp(data, new_var, 'address')
        self.showSpecificEmp(data['ssn'])
    
    def editHomePhone(self, data):
        """ This calls the inputter and calls logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('home phone number')
        self.__logic.updateEmp(data, new_var, 'homephonenumber')
        self.showSpecificEmp(data['ssn'])
    
    def editMobilePhone(self, data):
        """ This calls the inputter and calls logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('mobile phone number')
        self.__logic.updateEmp(data, new_var, 'mobilephonenumber')
        self.showSpecificEmp(data['ssn'])
    
    def editLicense(self, data):
        """ This calls the inputter and calls logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterLicense()
        self.__logic.updateEmp(data, new_var, 'licence')
        self.showSpecificEmp(data['ssn'])
    
    def showAllLocations(self):
        """ This gets a list of every location from logicAPI, then calls the printer to print out every location for the user """
        data_list = self.__logic.showAllLocations()
        self.__data_printer.printLocations(data_list)

    def showAllWorkTrips(self):
        """ This gets a list of every flight from logicAPI, then calls the printer to print it out for the user """
        data_list = self.__logic.showAllWorkTrips()
        self.__data_printer.printAllWorkTrips(data_list)
    
    def addWorkTrip(self):
        """ This calls the inputter so the user can input the work trips's data, then calls logicAPI to add both flights to the flight.csv file """
        data_list = self.__inputter.addWorkTrip()