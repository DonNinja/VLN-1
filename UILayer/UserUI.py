from UILayer.UIAPI import UIAPI
import sys

BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"

class UserUI:
    def __init__(self):
        self.__ui_api = UIAPI()

    def back(self): 
        '''Our back function displayed in every screen'''
        return

    def inputCheck(self, inp, choice_dict):
        ''' Checks choice_dict, which is given by the function call, if the inputted choice exists and returns True if so '''
        for i in choice_dict:
            if inp == i:
                return True
        return False

    def askForInput(self):
        return input("\nEnter a choice: ").upper()

    def startScreen(self):
        ''' Displays the choices of the starting screen and asks the user for an input '''
        while True:
            self.__ui_api.UIHeaderDisplay("Starting screen") # Displays the header with the appropriate screen name
            choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.employeeScreen, "2" : self.airplaneScreen, "3" : self.tripAndLocScreen, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
                # The screens are pretty repetetive, so I don't feel the need to comment on every single screen

    def employeeScreen(self):
        ''' Displays the choices of the employee screen and asks the user for an input '''
        inp = ""
        while inp != "B": # It loops until a user enters the 'B' key, by which time it will return None and return to the previous function
            self.__ui_api.UIHeaderDisplay("Employee screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Employee", "2 - Show Employee", "3 - Edit Employee", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.addEmployeeScreen, "2" : self.showEmpScreen, "3" : self.editEmpScreen, "B" : self.back, "Q" : sys.exit}
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def addEmployeeScreen(self):
        ''' Displays the choices of the add employee screen and asks the user for an input '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Add employee screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Pilot", "2 - Add Flight Attendant", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.addPilotScreen, "2" : self.addAttendantScreen, "B" : self.back,"Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def addPilotScreen(self):
        ''' Calls a function that asks the user to input values for a new pilot '''
        self.__ui_api.addEmp("Pilot")
        pass

    def addAttendantScreen(self):
        ''' Calls a function that asks the user to input values for a new Cabincrew '''
        self.__ui_api.addEmp("Cabincrew")
        pass

        
    def editEmpScreen(self):
        ''' Displays for the user the types of employees he can change, then asks the user for an input '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Edit employees screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Edit any employee", "2 - Edit pilot", "3 - Edit flight attendant", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.anyEmpSSN, "2" : self.pilotSSN, "3" : self.attendantSSN, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def anyEmpSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what employee we want to change '''
        is_emp, data = self.showEmployeeSSN()
        if is_emp: # If SSN is valid we enter editing screen
            self.whileEditingEmpScreen(data, data['role'])
        else: 
            pass

    def pilotSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what pilot we want to change '''
        is_pilot, data = self.showPilotSSN()
        if is_pilot: # If SSN is valid we enter editing screen
            self.whileEditingEmpScreen(data, data['role'])
        else:
            pass

    def attendantSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what flight attendant we want to change '''
        is_attendant, data = self.showAttendantSSN()
        if is_attendant: # If SSN is valid we enter editing screen
            self.whileEditingEmpScreen(data, data['role'])
        else:
            pass

    def whileEditingEmpScreen(self, data, role):
        ''' This asks the user what he would like to change '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Editing employee screen")  # Displays the header with the appropriate screen name
            if role == 'Cabincrew':
                choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", BACK_STR, QUIT_STR] # Lists choices available for Cabincrew
                choice_dict = {"1" : self.__ui_api.editAddress, "2" : self.phoneEditScreen, "3" : self.__ui_api.editEmail, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            else:
                choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane License", BACK_STR, QUIT_STR] # Lists choices available for Pilots
                choice_dict = {"1" : self.__ui_api.editAddress, "2" : self.phoneEditScreen, "3" : self.__ui_api.editEmail, "4" : self.__ui_api.editLicense, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp, choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                if inp != "B" and inp != "Q":
                    nextScreen(data) 
                else:
                    nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def phoneEditScreen(self, data):
        ''' This shows the user what phones he can change. '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Editing employee phone screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Change Home Phone Number", "2 - Change Mobile Number", BACK_STR, QUIT_STR]  # Lists choices available
            choice_dict = {"1" : self.__ui_api.editHomePhone, "2" : self.__ui_api.editMobilePhone, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                if inp != "B" and inp != "Q":
                    nextScreen(data)
                else:
                    nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def showEmpScreen(self):
        ''' This asks what kind of employee he would like to show '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Show employees screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", "4 - Show an employee's work trips for a week", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1": self.miscFilterScreen, "2" : self.pilotFilterScreen, "3" : self.attFilterScreen, "4" : self.__ui_api.showEmpWeekTrips, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def miscFilterScreen(self):
        ''' This is the any employee show screen, here a user can choose what he wants to display, whether it's every employee or a specific employee (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Display Employee Screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Show all employees", "2 - Show employees at work on day", "3 - Show employees not at work on day", "4 - Look for employee by SSN", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.showAllEmps , "2" : self.__ui_api.showEmpAtWork , "3" : self.__ui_api.showEmpNotAtWork, "4" : self.showEmployeeSSN, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def showEmployeeSSN(self):
        ssn = input("Enter an employee's SSN (kennitala): ")
        return self.__ui_api.showSpecificEmp(ssn)

    def attFilterScreen(self):
        ''' This is the flight attendant show screen, here a user can choose what he wants to display, whether it's every flight attendant or a specific flight attendant (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Display Flight Attendant Screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Show all attendants", "2 - Show attendants at work on day", "3 - Show attendants not at work on day", "4 - Look for attendant by SSN", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.showAllAttendants , "2" : self.__ui_api.showEmpAtWork, "3" : self.__ui_api.showEmpNotAtWork, "4" : self.showAttendantSSN, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def showAttendantSSN(self):
        ''' This asks for an input and checks if the SSN corresponds to a flight attendant '''
        ssn = input("Enter a flight attendant's SSN (kennitala): ")
        return self.__ui_api.showSpecificAttendant(ssn)
        
    def pilotFilterScreen(self):
        ''' This is the pilot show screen, here a user can choose what he wants to display, whether it's every pilot or a specific pilot (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Display Pilot Screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Show all pilots", "2 - Show pilots at work on day", "3 - Show pilots not at work on day", "4 - Look for pilot by SSN", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.showAllPilots , "2" : self.__ui_api.showEmpAtWork, "3" : self.__ui_api.showEmpNotAtWork, "4" : self.showPilotSSN, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def showPilotSSN(self):
        ''' This asks for an input and checks if the SSN corresponds to a pilot '''
        ssn = input("Enter a pilot's SSN (kennitala): ")
        return self.__ui_api.showSpecificPilot(ssn)
        
        
    def airplaneScreen(self):
        ''' This screen shows the user what he can do with airplanes, then asks for an input '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Airplane screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Show All Airplanes", "2 - Add Airplanes", "3 - Show Pilots Sorted by plane make", "4 - Show Pilots For Specific Plane Make", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.showAllAirplanes, "2" : self.addAirplane, "3" : self.showPilotsSortedByPlanes, "4" : self.specificPlaneScreen, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
        
    def specificPlaneScreen(self):
        ''' This is where the user inputs a plane make and receives a print of every pilot that's allowed to fly that type of plane '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Choose a plane make")  # Displays the header with the appropriate screen name
            choice_list = ["1 - BAE146", "2 - Fokker F28", "3 - Fokker F100", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : "NABAE146", "2" : "NAFokkerF28", "3" : "NAFokkerF100", "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                if inp == "B" or inp == "Q": # So that it doesn't display an empty box when enter back or quit
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen() # This calls the function the user asked for
                else:
                    plane_type = choice_dict.get(inp)
                    self.showPilotsForPlaneType(plane_type)
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def showAllAirplanes(self):
        # Show all airplanes
        self.__ui_api.showAllPlanes()
        
    def addAirplane(self):
        # Adding Airplane
        self.__ui_api.addPlane()

    def showPilotsSortedByPlanes(self):
        self.__ui_api.showSortPilotsByPlane()

    def showPilotsForPlaneType(self, plane_type):
        # ShowPilotsForSpecificPlane
        self.__ui_api.showPilotsForPlane(plane_type)

    def tripAndLocScreen(self):
        ''' This is a screen that allows the user to choose between showing work trips or locations screens '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Trips and locations screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Locations", "2 - Work Trips", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.locationScreen, "2" : self.workTripsScreen, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def workTripsScreen(self):
        ''' This shows the user the choices he can make with work trips '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Work trips screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Work Trip", "2 - Show Work Trips", "3 - Show An Employee's Work Trip", "4 - Edit Work Trip", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.addWorkTrip, "2" : self.filterWorkTripsScreen, "3" : self.showEmpsWorkTrips,"4" : self.enterFN , "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def showEmpsWorkTrips(self):
        ssn = input("Enter an employee's SSN (kennitala): ")
        self.__ui_api.showEmpsWorkTrips(ssn)

    def locationScreen(self):
        ''' This shows the user the choices he can make with locations '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Locations screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.addLocation, "2" : self.enterLocID, "3" : self.__ui_api.showAllLocations, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def enterLocID(self):
        is_loc, loc_id = self.__ui_api.checkLocID()
        if is_loc:
            self.__ui_api.showSpecificLocation(loc_id)
            self.whileEditingLocScreen(loc_id)
        else:
            print("That is not a location ID!")

    def whileEditingLocScreen(self, loc_id):
        ''' This screen shows what the user can change about locations '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Editing location screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Change emergency contact name", "2 - Change emergency contact phone number", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.editLocContName, "2" : self.__ui_api.editLocContPhone, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                if inp == "B" or inp == "Q":
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen() # This calls the function the user asked for
                else:
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen(loc_id)
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
        
    def filterWorkTripsScreen(self):
        ''' This screen shows the user what choices he has for displaying work trip '''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Filter work trips screen") # Displays the header with the appropriate screen name
            choice_list = ["1 - Show All Trips", "2 - Show For Day", "3 - Show For Week", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.showAllWorkTrips, "2" :self.__ui_api.showWorkTripsByDay, "3" : self.__ui_api.showWorkTripsByWeek, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def whileEditingWorkTripsScreen(self, flight_num):
        ''' This screen shows the user what choices he has for editing work trip'''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Edit work trips screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Aircraft ID", "2 - Add Pilot", "3 - Add Cabincrew", BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.editFlightAircraftID, "2" :self.addPilotToWorkTrip, "3" : self.addCCToWorkTrip,"B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                if inp == "B" or inp == "Q":
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen() # This calls the function the user asked for
                else:
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen(flight_num)
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def addPilotToWorkTrip(self, flight_num):
        ''' This screen shows the user what choices he has for adding pilot/s to work trip'''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Add pilot to work trip screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Captain", "2 - Add Copilot",BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.editFlightCaptain, "2" :self.__ui_api.editFlightCopilot,"B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                if inp == "B" or inp == "Q":
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen() # This calls the function the user asked for
                else:
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen(flight_num)
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def addCCToWorkTrip(self, flight_num):
        ''' This screen shows the user what choices he has for adding Cabincrew to work trip'''
        inp = ""
        while inp != "B":
            self.__ui_api.UIHeaderDisplay("Add cabincrew to work trip screen")  # Displays the header with the appropriate screen name
            choice_list = ["1 - Add Service Manager", "2 - Add Flight Attendant 1", "3 - Add Flight Attendant 2",BACK_STR, QUIT_STR] # Lists choices available
            choice_dict = {"1" : self.__ui_api.editFlightFSM, "2" : self.__ui_api.editFlightFA_1,"3" : self.__ui_api.editFlightFA_2, "B" : self.back, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_api.UIDisplay(choice_list) # Displays the choices
            inp = self.askForInput()
            #Check if input is valid
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                if inp == "B" or inp == "Q":
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen() # This calls the function the user asked for
                else:
                    nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                    nextScreen(flight_num)
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again
    
    def enterFN(self):
        flight_num = input("Enter a flight number (4 digits): ").zfill(4)
        if self.__ui_api.showSpecificTrip(flight_num):
            self.whileEditingWorkTripsScreen(flight_num)