from LogicLayer.Logic import LogicAPI
from UILayer.UserInput import UserInput
from UILayer.UIDataPrinter import UIDataPrinter
from UILayer.UIPrinter import UIPrinter

class UIAPI:
    def __init__(self):
        self.logic = LogicAPI()
        self.inputter = UserInput()
        self.data_printer = UIDataPrinter()
        self.ui_printer = UIPrinter()

    def UIDisplay(self, choice_list):
        self.ui_printer.display(choice_list)
    
    def UIHeaderDisplay(self, title):
        self.ui_printer.headerDisplay(title)
    
    def addEmp(self, role):
        data_list = self.inputter.addEmp(role)
        self.logic.addEmpLL(data_list)
    
    def addPlane(self):
        data_list = self.inputter.addPlane()
        self.logic.addPlane(data_list)
    
    def addLocation(self):
        pass
    
    def showAllEmps(self):
        data_list = self.logic.showAllEmps()
        self.data_printer.printAllEmps(data_list)
    
    def showAllPilots(self):
        data_list = self.logic.showAllPilots()
        self.data_printer.printAllEmps(data_list)
    
    def showAllAttendants(self):
        data_list = self.logic.showAllAttendants()
        self.data_printer.printAllEmps(data_list)
    
    def showAllPlanes(self):
        data_list = self.logic.showAllPlanes()
        self.data_printer.printAllPlanes(data_list)
    
    def showPilotsForPlane(self, plane_type):
        data_list = self.logic.showPilotByPlane(plane_type)
        self.data_printer.printPilotForPlane(data_list)
    
    def showSpecificEmp(self, ssn):
        emp = self.logic.showEmpSSN(ssn)
        return self.data_printer.printEmpSSN(emp), emp
    
    def showSpecificPilot(self, ssn):
        emp = self.logic.showPilotSSN(ssn)
        return self.data_printer.printEmpSSN(emp), emp
    
    def showSpecificAttendant(self, ssn):
        emp = self.logic.showAttendantSSN(ssn)
        return self.data_printer.printEmpSSN(emp), emp

    def editEmail(self, data):
        new_var = self.inputter.enterVariable('email')
        self.logic.updateEmp(data, new_var, 'email')
        self.showSpecificEmp(data['ssn'])

    def editAddress(self, data):
        new_var = self.inputter.enterVariable('address')
        self.logic.updateEmp(data, new_var, 'address')
        self.showSpecificEmp(data['ssn'])
    
    def editHomePhone(self, data):
        new_var = self.inputter.enterVariable('home phone number')
        self.logic.updateEmp(data, new_var, 'homephonenumber')
        self.showSpecificEmp(data['ssn'])
    
    def editMobilePhone(self, data):
        new_var = self.inputter.enterVariable('mobile phone number')
        self.logic.updateEmp(data, new_var, 'mobilephonenumber')
        self.showSpecificEmp(data['ssn'])
    
    def editLicense(self, data):
        new_var = self.inputter.enterLicense()
        self.logic.updateEmp(data, new_var, 'licence')
        self.showSpecificEmp(data['ssn'])
    
    def showAllLocations(self):
        data_list = self.logic.showAllLocations()
        self.data_printer.printLocations(data_list)
