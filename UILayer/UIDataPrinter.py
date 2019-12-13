import datetime
import dateutil.parser

class UIDataPrinter:
    def __init__(self):
        pass
    
    def printCrewTop(self):
        """ This Prints the top 2 lines of the crew prints, then returns the line so we can use len(line) later """
        line = '║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format('SSN', 'Name', 'Role', 'Rank', 'Email', 'License', 'Address', 'Mobile phone number', 'Home phone number') # ^ center aligns the text
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        return line

    def printBotLine(self, length):
        """ This prints the bottom line so it looks good """
        line = "╚" # Bottom left corner
        while len(line) < length-1: # Goes until it reaches the bottom right corner, but doesn't include it
            line += "═"
        line += "╝" # Bottom right corner
        print(line) # This prints the header line
    
    def printTopLine(self, length):
        """ This prints the top line so it looks good """
        print()
        line = "╔" # Top left corner
        while len(line) < length-1: # Goes until it reaches the top right corner, but doesn't include it
            line += "═"
        line += "╗" # Top right corner
        print(line) # This prints the header line
    
    def printSeparator(self, length):
        """ This prints a separator to make the display more readable """
        line = "╟" # Left wall
        while len(line) < length-1: # Goes until it reaches the right wall, but doesn't include it
            line += "─" # A separator line
        line += "╢" # Right wall
        print(line) # This prints the header line

    def printAllEmps(self, data_list):
        """ This prints every employee in the given data list and formats it nicely """
        line = self.printCrewTop()
        self.printSeparator(len(line)) # Prints the seperator
        for emp in data_list:
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['email'],emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber'])) # This prints every employee in the data_list
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way

    def printAllPlanes(self, data_list):
        """ This prints every plane and formats it nicely """
        line = '║{:^12}│{:^14}║'.format('Plane Type', 'Plane Insignia') # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        self.printSeparator(len(line)) # Prints the seperator
        for plane in data_list:
            print('║{:^12}│{:^14}║'.format(plane['planeTypeId'], plane['planeInsignia']))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way
    
    def printEmpSSN(self, employee):
        """ This calls a function to find any employee by their SSN then prints out their information, if the employee does not exists, it prints out 'Invalid SSN' """
        if employee:
            line = self.printCrewTop()
            self.printSeparator(len(line)) # Prints the seperator
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(employee['ssn'], employee['name'], employee['role'], employee['rank'], employee['email'], employee['licence'], employee['address'], employee['mobilephonenumber'], employee['homephonenumber']))
            self.printBotLine(len(line)) # Prints the bottom line
            ret_cond = True
        else:
            print("\nInvalid SSN!")
            ret_cond = False
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way
        return ret_cond

    def printPilotForPlane(self, data_list):
        """ This calls a function that searches employees by whether they fly a specific plane type """
        line = self.printCrewTop()
        self.printSeparator(len(line)) # Prints the seperator
        for pilot in data_list:
            print('║{:^10}│{:^20}│{:^9}│{:^22}│{:^19}│{:^12}│{:^20}│{:^19}│{:^17}║'.format(pilot['ssn'], pilot['name'], pilot['role'], pilot['rank'], pilot['email'], pilot['licence'], pilot['address'], pilot['mobilephonenumber'], pilot['homephonenumber']))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way
    
    def printLocations(self, location_list):
        """ This prints every location from the data list """
        line = '║{:^3}│{:^13}│{:^13}│{:^20}│{:^11}│{:^19}│{:^20}│{:^20}║'.format('ID', 'City', 'Country', 'Airport name', 'Flight time', 'Flight distance(km)', 'Contact name', 'Contact phone number') # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        self.printSeparator(len(line)) # Prints the seperator
        if location_list: # Checks if the location list is empty
            for location in location_list: # Goes through the whole list and gets every location dictionary
                loc_hour, loc_min = location['flightTime'].split(".") # So we can use the hour and minutes seperately
                print('║{:^3}│{:^13}│{:^13}│{:^20}│   {}h{:02d}m   │{:^19}│{:^20}│{:^20}║'.format(location['id'], location['destination'], location['country'], location['airport'], loc_hour, int(loc_min), location['distanceFromIceland'], location['contactName'], location['contactPhone']))
            self.printBotLine(len(line)) # Prints the bottom line
            input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way
            return True
        else:
            return False
    
    def printSingleLocation(self, location):
        """ This prints every location from the data list """
        line = '║{:^3}│{:^13}│{:^13}│{:^20}│{:^11}│{:^19}│{:^20}│{:^20}║'.format('ID', 'City', 'Country', 'Airport name', 'Flight time', 'Flight distance(km)', 'Contact name', 'Contact phone number') # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line 
        self.printSeparator(len(line)) # Prints the seperator
        if location: # Checks if the location is valid
            loc_hour, loc_min = location['flightTime'].split(".")
            print('║{:^3}│{:^13}│{:^13}│{:^20}│   {}h{:02d}m   │{:^19}│{:^20}│{:^20}║'.format(location['id'], location['destination'], location['country'], location['airport'], loc_hour, int(loc_min), location['distanceFromIceland'], location['contactName'], location['contactPhone']))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way

    def printAllWorkTrips(self, data_list):
        """ This receives a list of every flight and prints them out neatly """
        line = '║{:^13}│{:^14}│{:^11}│{:^19}│{:^19}│{:^11}│{:^11}│{:^11}│{:^13}│{:^16}│{:^16}│{:^12}║'.format('Flight number', 'Departing from', 'Arriving at', 'Departure time', 'Arrival time', 'Aircraft ID', 'Captain SSN', 'Copilot SSN', 'Flight SM SSN', 'Flight att 1 SSN', 'Flight att 2 SSN', 'Fully manned') # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        self.printSeparator(len(line)) # Prints the seperator
        for trip in data_list:
            dep_time = trip['departure']
            parsed_dep_time = dateutil.parser.parse(dep_time) # This parses the departure time so we can easily get the values
            dep_time_day = parsed_dep_time.day # This just gets the day from the parsed departure time
            dep_time_month = parsed_dep_time.month # This just gets the month from the parsed departure time
            dep_time_year = parsed_dep_time.year # This just gets the year form the parsed departure time
            dep_time_clock = parsed_dep_time.time() # This gets the time from the parsed departur time
            correct_dep_time = "{:02d}.{:02d}.{} {}".format(dep_time_day, dep_time_month, dep_time_year, dep_time_clock) # This set the departure time into the correct form for our print call
            arr_time = trip['arrival']
            parsed_arr_time = dateutil.parser.parse(arr_time) # This does the same but for arrival time
            arr_time_day = parsed_arr_time.day # This does the same but for arrival time
            arr_time_month = parsed_arr_time.month # This does the same but for arrival time
            arr_time_year = parsed_arr_time.year # This does the same but for arrival time
            arr_time_clock = parsed_arr_time.time() # This does the same but for arrival time
            correct_arr_time = "{:02d}.{:02d}.{} {}".format(arr_time_day, arr_time_month, arr_time_year, arr_time_clock) # This does the same but for arrival time
            
            print('║{:^13}│{:^14}│{:^11}│{:^14}│{:^12}│{:^11}│{:^11}│{:^11}│{:^13}│{:^16}│{:^16}│{:^12}║'.format(trip['flightNumber'], trip['departingFrom'], trip['arrivingAt'], correct_dep_time, correct_arr_time, trip['aircraftID'], trip['captain'], trip['copilot'], trip['fsm'], trip['fa1'], trip['fa2'], trip['fullyManned']))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way

    def printEmpsNotWorking(self, emp_list):
        """ Takes in a list of every employee who's not working and prints out their SSNs """
        print("\nThese employees are not working on the inputted date") # This is to show what we're displaying
        line = "║{:^14}║".format("Employee SSN") # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        self.printSeparator(len(line)) # Prints the seperator
        for val in emp_list: # This goes through the employee list and prints every SSN out
            print("║{:^14}║".format(val))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way

    def printEmpsWorking(self, emp_dict):
        """ Takes in a dictionary of every employee and their destinations who's working on a selected day prints them and their destinations out """
        print("\nThese employees are working on the inputted date") # This is to show what we're displaying
        line = "║{:^14}│{:^14}║".format("Employee SSN", "Destination ID") # This is the header line
        self.printTopLine(len(line)) # This prints the top of the display box
        print(line) # This prints the header line
        self.printSeparator(len(line)) # Prints the seperator
        for dest in emp_dict: # This goes through the destinations in the dictionary so we can show where the employees are going
            for emp_ssn in emp_dict[dest]: # This goes through the employees 
                print('║{:^14}│{:^14}║'.format(emp_ssn, dest))
        self.printBotLine(len(line)) # Prints the bottom line
        input("\nPress enter to continue...") # We wait until the user enters anything so he can see the display box without the choice form geting in the way