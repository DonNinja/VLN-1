from LogicLayer.Logic import LogicAPI

class UIDataPrinter:
    def __init__(self):
        self.__data_getter = LogicAPI()
    
    def printCrewTop(self):
        line = '║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format('SSN', 'Name', 'Role', 'Rank', 'License', 'Address', 'Mobile phone number', 'Home phone number')
        self.printTopLine(len(line))
        print(line)
        return line

    def printBotLine(self, length):
        line = "╚"
        while len(line) < length-1:
            line += "═"
        line += "╝"
        print(line)
    
    def printTopLine(self, length):
        print()
        line = "╔"
        while len(line) < length-1:
            line += "═"
        line += "╗"
        print(line)

    def printAllEmps(self):
        all_emp_list = self.__data_getter.showAllEmps()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printAllPilots(self):
        all_emp_list = self.__data_getter.showAllPilots()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printAllAttendants(self):
        all_emp_list = self.__data_getter.showAllAttendants()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")

    def printAllPlanes(self):
        all_plane_list = self.__data_getter.showAllPlanes()
        line = '║ {:^12} │ {:^14} ║'.format('Plane ID', 'Plane Insignia')
        self.printTopLine(len(line))
        print(line)
        for plane in all_plane_list:
            print('║ {:^12} │ {:^14} ║'.format(plane['planeTypeId'], plane['planeInsignia']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printPilotSSN(self, ssn):
        pilot = self.__data_getter.showPilotSSN(ssn)
        if pilot:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")
    
    def printAttendantSSN(self, ssn):
        attendant = self.__data_getter.showAttendantSSN(ssn)
        if attendant:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(attendant['ssn'], attendant['name'], attendant['role'], attendant['rank'], attendant['licence'], attendant['address'], attendant['mobilephonenumber'], attendant['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")
    
    def printEmpSSN(self, ssn):
        employee = self.__data_getter.showEmpSSN(ssn)
        if employee:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(employee['ssn'], employee['name'], employee['role'], employee['rank'], employee['licence'], employee['address'], employee['mobilephonenumber'], employee['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")