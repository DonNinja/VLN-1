class UIDataPrinter:
    def __init__(self):
        pass
    
    def printCrewTop(self):
        """ This Prints the top 2 lines of the crew prints, then returns the line so we can use len(line) later """
        line = '║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^19} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format('SSN', 'Name', 'Role', 'Rank', 'Email', 'License', 'Address', 'Mobile phone number', 'Home phone number') # ^ center aligns the text
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

    def printAllEmps(self, data_list):
        """ This prints every employee in the given data list and formats it nicely """
        line = self.printCrewTop()
        for emp in data_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^19} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['email'],emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")

    def printAllPlanes(self, data_list):
        """ This prints every plane and formats it nicely """
        line = '║ {:^12} │ {:^14} ║'.format('Plane Type', 'Plane Insignia')
        self.printTopLine(len(line))
        print(line)
        for plane in data_list:
            print('║ {:^12} │ {:^14} ║'.format(plane['planeTypeId'], plane['planeInsignia']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printEmpSSN(self, employee):
        """ This calls a function to find any employee by their SSN then prints out their information, if the employee does not exists, it prints out 'Invalid SSN' """
        if employee:
            line = self.printCrewTop()
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^19} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(employee['ssn'], employee['name'], employee['role'], employee['rank'], employee['email'], employee['licence'], employee['address'], employee['mobilephonenumber'], employee['homephonenumber']))
            self.printBotLine(len(line))
            ret_cond = True
        else:
            print("\nInvalid SSN!")
            ret_cond = False
        input("\nPress enter to continue...")
        return ret_cond

    def printPilotForPlane(self, data_list):
        """ This calls a function that searches employees by whether they fly a specific plane type """
        line = self.printCrewTop()
        for pilot in data_list:
            print('║ {:^10} │ {:^20} │ {:^9} │ {:^22} │ {:^19} │ {:^12} │ {:^12} │ {:^19} │ {:^17} ║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")