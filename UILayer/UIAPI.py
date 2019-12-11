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
    
    def addEmp(self, role):
        data_list = []
        data_list.append(self.checkSSN(role))
        data_list.append(self.checkName(role))
        data_list.append(self.checkRole(role))
        data_list.append(self.checkRank(role))
        data_list.append(self.checkLicens(role))
        data_list.append(self.checkAddress(role))
        data_list.append(self.checkMobile(role))
        data_list.append(self.checkHomenum(role))
        #
        #
        #
        self.logic.addEmpLL(data_list)

    def checkSSN(self, emp_type): #Virkar
        ssn = self.inputter.addEmpSSN(emp_type)
        while not(self.logic.checkSSN(ssn)):
            ssn = self.inputter.addEmpSSN(emp_type)
        else:
            return ssn

    def checkName(self, emp_type): #Virkar ekki
        first_name, last_name = self.inputter.addEmpName(emp_type)
        while not(self.logic.checkName(first_name, last_name)):
            first_name, last_name = self.inputter.addEmpName(emp_type)
        else:
            return first_name.capitalize(), last_name.capitalize()

    def checkRole(self, emp_type): #Virkar
        return emp_type

    def checkRank(self, emp_type): #Virkar
        rank_input = self.inputter.addEmpRank(emp_type)
        rank = self.logic.checkRank(rank_input, emp_type)
        while not (rank):
            rank_input = self.inputter.addEmpRank(emp_type)
            rank = self.logic.checkRank(rank_input, emp_type)
        else:
            print(rank)
            return rank

    def checkLicens(self,emp_type): #Virkar
        licens_input = self.inputter.addEmpLicens(emp_type)
        licens = self.logic.checkLicens(licens_input)
        while not(licens):
            licens_input = self.inputter.addEmpLicens
            licens = self.logic.checkLicens(licens_input)
        else:
            print(licens)
            return licens

    def checkAddress(self, emp_type): #Virkar ekki
        address = self.inputter.addEmpAddress(emp_type)
        while not(self.logic.checkAddress(address)):
            address = self.inputter.addEmpAddress
        else:
            print(address)
            return address

    def checkMobile(self, emp_type): # Virkar ekki
        mobile = self.inputter.addEmpMobile(emp_type)
        while not(self.logic.checkPhone(mobile)):
            mobile = self.inputter.addEmpMobile
        else:
            print(mobile)
            return mobile

    def checkHomenum(self,emp_type): # Virkar ekki
        home_phone_num = self.inputter.addHomePhone(emp_type)
        while not(self.logic.checkPhone(home_phone_num)):
            mobile = self.inputter.addEmpHomePhone

        else:
            print(home_phone_num)
            return home_phone_num

