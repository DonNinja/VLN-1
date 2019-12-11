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
<<<<<<< HEAD
        self.data_printer.printAttendantSSN(emp)

    def editemp(self,ssn,emp_type):
        emp = self.logic.showPilotSSN(ssn)
        pilot_data = list(emp.values())
        updated_emp = self.inputter.editemp(pilot_data,emp_type)
        self.logic.editemp(updated_emp)

=======
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
        new_var = self.inputter.enterVariable('plane license')
        self.logic.updateEmp(data, new_var, 'licence')
        self.showSpecificEmp(data['ssn'])
>>>>>>> 94327e09f99e8a282e4a4fb9edac9bcea9d77b21
