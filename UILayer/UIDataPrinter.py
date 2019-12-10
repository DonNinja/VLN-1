from LogicLayer.Logic import LogicAPI

class UIDataPrinter:
    def __init__(self):
        self.__data_getter = LogicAPI()
    
    def printCrewTop(self):
        """ This Prints the top 2 lines of the crew prints, then returns the line so we can use len(line) later """
        line = '║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format('SSN', 'Name', 'Role', 'Rank', 'License', 'Address', 'Mobile phone number', 'Home phone number') # ^ center aligns the text
        self.printTopLine(len(line))
        print(line)
        return line

    def printBotLine(self, length):
        """ This prints the bottom line so it looks good """
        line = "╚"
        while len(line) < length-1:
            line += "═"
        line += "╝"
        print(line)
    
    def printTopLine(self, length):
        """ This prints the top line so it looks good """
        print()
        line = "╔"
        while len(line) < length-1:
            line += "═"
        line += "╗"
        print(line)

    def printAllEmps(self):
        """ This prints every employee and formats it nicely """
        all_emp_list = self.__data_getter.showAllEmps()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printAllPilots(self):
        """ This prints every pilot and formats it nicely """
        all_emp_list = self.__data_getter.showAllPilots()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printAllAttendants(self):
        """ This prints every flight attendant and formats it nicely """
        all_emp_list = self.__data_getter.showAllAttendants()
        line = self.printCrewTop()
        for emp in all_emp_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")

    def printAllPlanes(self):
        """ This prints every plane and formats it nicely """
        all_plane_list = self.__data_getter.showAllPlanes()
        line = '║ {:^12} │ {:^14} ║'.format('Plane Type', 'Plane Insignia')
        self.printTopLine(len(line))
        print(line)
        for plane in all_plane_list:
            print('║ {:^12} │ {:^14} ║'.format(plane['planeTypeId'], plane['planeInsignia']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printPilotSSN(self, ssn):
        """ This calls a function to find a pilot by their SSN then prints out their information, if the pilot is not found, then it prints out 'Invalid SSN!' """
        pilot = self.__data_getter.showPilotSSN(ssn)
        if pilot:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")
    
    def printAttendantSSN(self, ssn):
        """ This calls a function to find a flight attendant by their SSN then prints out their information, if the flight attendant is not found, then it prints out 'Invalid SSN!' """
        attendant = self.__data_getter.showAttendantSSN(ssn)
        if attendant:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(attendant['ssn'], attendant['name'], attendant['role'], attendant['rank'], attendant['licence'], attendant['address'], attendant['mobilephonenumber'], attendant['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")
    
    def printEmpSSN(self, ssn):
        """ This calls a function to find any employee by their SSN then prints out their information, if the employee does not exists, it prints out 'Invalid SSN' """
        employee = self.__data_getter.showEmpSSN(ssn)
        if employee:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(employee['ssn'], employee['name'], employee['role'], employee['rank'], employee['licence'], employee['address'], employee['mobilephonenumber'], employee['homephonenumber']))
            self.printBotLine(len(line))
        else:
            print("\nInvalid SSN!")
        input("\nPress enter to continue...")

    def printPilotForPlane(self, plane_type):
        """ This calls a function that searches employees by whether they fly a specific plane type """
        pilots = self.__data_getter.showPilotByPlane(plane_type)
        line = self.printCrewTop()
        for pilot in pilots:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")