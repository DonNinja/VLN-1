import datetime
import dateutil.parser

class UIDataPrinter:
    def __init__(self):
        pass
    
    def printCrewTop(self):
        """ This Prints the top 2 lines of the crew prints, then returns the line so we can use len(line) later """
        line = '║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format('SSN', 'Name', 'Role', 'Rank', 'Email', 'License', 'Address', 'Mobile phone number', 'Home phone number') # ^ center aligns the text
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
    
    def printSeparator(self, length):
        line = "╟"
        while len(line) < length-1:
            line += "─"
        line += "╢"
        print(line)

    def printAllEmps(self, data_list):
        """ This prints every employee in the given data list and formats it nicely """
        line = self.printCrewTop()
        self.printSeparator(len(line))
        for emp in data_list:
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['email'],emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")

    def printAllPlanes(self, data_list):
        """ This prints every plane and formats it nicely """
        line = '║{:^12}│{:^14}║'.format('Plane Type', 'Plane Insignia')
        self.printTopLine(len(line))
        print(line)
        self.printSeparator(len(line))
        for plane in data_list:
            print('║{:^12}│{:^14}║'.format(plane['planeTypeId'], plane['planeInsignia']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printEmpSSN(self, employee):
        """ This calls a function to find any employee by their SSN then prints out their information, if the employee does not exists, it prints out 'Invalid SSN' """
        if employee:
            line = self.printCrewTop()
            self.printSeparator(len(line))
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(employee['ssn'], employee['name'], employee['role'], employee['rank'], employee['email'], employee['licence'], employee['address'], employee['mobilephonenumber'], employee['homephonenumber']))
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
        self.printSeparator(len(line))
        for pilot in data_list:
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['email'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printLocations(self, location):
        """ This prints every location from the data list """
        line = '║{:^3}│{:^13}│{:^13}│{:^20}│{:^11}│{:^19}│{:^20}│{:^20}║'.format('ID', 'City', 'Country', 'Airport name', 'Flight time', 'Flight distance(km)', 'Contact name', 'Contact phone number')
        self.printTopLine(len(line))
        print(line)
        self.printSeparator(len(line))
        if location:
            for loc in location:
                loc_hour, loc_min = loc['flightTime'].split(".")
                print('║{:^3}│{:^13}│{:^13}│{:^20}│   {}h{:02d}m   │{:^19}│{:^20}│{:^20}║'.format(loc['id'], loc['destination'], loc['country'], loc['airport'], loc_hour, int(loc_min), loc['distanceFromIceland'], loc['contactName'], loc['contactPhone']))
            self.printBotLine(len(line))
            return True
        else:
            return False
        self.printBotLine(len(line))
        input("\nPress enter to continue...")
    
    def printSingleLocation(self, location):
        """ This prints every location from the data list """
        line = '║{:^3}│{:^13}│{:^13}│{:^20}│{:^11}│{:^19}│{:^20}│{:^20}║'.format('ID', 'City', 'Country', 'Airport name', 'Flight time', 'Flight distance(km)', 'Contact name', 'Contact phone number')
        self.printTopLine(len(line))
        print(line)
        self.printSeparator(len(line))
        if location:
            loc_hour, loc_min = location['flightTime'].split(".")
            print('║{:^3}│{:^13}│{:^13}│{:^20}│   {}h{:02d}m   │{:^19}│{:^20}│{:^20}║'.format(location['id'], location['destination'], location['country'], location['airport'], loc_hour, int(loc_min), location['distanceFromIceland'], location['contactName'], location['contactPhone']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")

    def printAllWorkTrips(self, data_list):
        """ This receives a list of every flight and prints them out neatly """
        line = '║{:^13}│{:^14}│{:^11}│{:^19}│{:^19}│{:^11}│{:^11}│{:^11}│{:^13}│{:^16}│{:^16}│{:^12}║'.format('Flight number', 'Departing from', 'Arriving at', 'Departure time', 'Arrival time', 'Aircraft ID', 'Captain SSN', 'Copilot SSN', 'Flight SM SSN', 'Flight att 1 SSN', 'Flight att 2 SSN', 'Fully manned')
        self.printTopLine(len(line))
        print(line)
        self.printSeparator(len(line))
        for trip in data_list:
            dep_time = trip['departure']
            parsed_dep_time = dateutil.parser.parse(dep_time)
            dep_time_day = parsed_dep_time.day
            dep_time_month = parsed_dep_time.month
            dep_time_year = parsed_dep_time.year
            dep_time_clock = parsed_dep_time.time()
            correct_dep_time = "{:02d}.{:02d}.{} {}".format(dep_time_day, dep_time_month, dep_time_year, dep_time_clock)

            arr_time = trip['arrival']
            parsed_arr_time = dateutil.parser.parse(arr_time)
            arr_time_day = parsed_arr_time.day
            arr_time_month = parsed_arr_time.month
            arr_time_year = parsed_arr_time.year
            arr_time_clock = parsed_arr_time.time()
            correct_arr_time = "{:02d}.{:02d}.{} {}".format(arr_time_day, arr_time_month, arr_time_year, arr_time_clock)
            
            print('║{:^13}│{:^14}│{:^11}│{:^14}│{:^12}│{:^11}│{:^11}│{:^11}│{:^13}│{:^16}│{:^16}│{:^12}║'.format(trip['flightNumber'], trip['departingFrom'], trip['arrivingAt'], correct_dep_time, correct_arr_time, trip['aircraftID'], trip['captain'], trip['copilot'], trip['fsm'], trip['fa1'], trip['fa2'], trip['fullyManned']))
        self.printBotLine(len(line))
        input("\nPress enter to continue...")