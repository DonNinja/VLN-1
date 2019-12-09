from UILayer.UserInput import UserInput
from UILayer.UIPrinter import UIPrinter
from UILayer.UIDataPrinter import UIDataPrinter
import sys

BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"

class UserUI:
    def __init__(self):
        self.__inputter = UserInput()
        self.__ui_printer = UIPrinter()
        self.__data_printer = UIDataPrinter()

    def doNothing(self):
        pass

    def back(self):
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
            self.__ui_printer.headerDisplay("Starting screen") # Displays the header with the appropriate screen name
            choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR] # This needs to change with every screen
            choice_dict = {"1" : self.employeeScreen, "2" : self.airplaneScreen, "3" : self.tripAndLocScreen, "Q" : sys.exit} # The dictionary values are function names, which are then called when one of the keys is entered
            self.__ui_printer.display(choice_list) # Displays the rest of the choices
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict) # This finds whether the inputted choice is valid or not, that is if the input is in the choice_dict and returns True if so, else it returns False
            if checking:
                nextScreen = choice_dict.get(inp) # This assigns the next function's name to nextScreen
                nextScreen() # This calls the function the user asked for
            else:
                print("Input is invalid!") # Prints out an error message if the inputted choice isn't valid, then loops the function again

    def employeeScreen(self):
        ''' Displays the choices of the employee screen and asks the user for an input '''
        inp = ""
        while inp != "B": # It loops until a user enters the 'B' key, by which time it will return None and return to the previous function
            self.__ui_printer.headerDisplay("Employee screen")
            choice_list = ["1 - Add Employee", "2 - Show Employee", "3 - Edit Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.addEmployeeScreen, "2" : self.showEmpScreen, "3" : self.editEmpScreen, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def addEmployeeScreen(self):
        ''' Displays the choices of the add employee screen and asks the user for an input '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Add employee screen")
            choice_list = ["1 - Add Pilot", "2 - Add Flight Attendant", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.addPilotScreen, "2" : self.addAttendantScreen, "B" : self.back,"Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def addPilotScreen(self):
        ''' Calls a function that asks the user to input values for a new pilot '''
        pilot_data_list = self.__inputter.addEmp("pilot")
        pass

    def addAttendantScreen(self):
        ''' Calls a function that asks the user to input values for a new flight attendant '''
        att_data_list = self.__inputter.addEmp("flight attendant")
        pass

    def showHardestWorking(self):
        #This just displays the hardest working employee, will be a function call
        pass
        
    def editEmpScreen(self):
        ''' Displays for the user the types of employees he can change, then asks the user for an input '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Edit employees screen")
            choice_list = ["1 - Edit any employee", "2 - Edit pilot", "3 - Edit flight attendant", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.anyEmpSSN, "2" : self.pilotSSN, "3" : self.attendantSSN, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def anyEmpSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what employee we want to change '''
        ssn = self.__inputter.enterSSN("ny employee") # The string that's sent in is "ny employee" because the input command has "a" + the string that's sent in so we can reuse the same command for each of the employee types

    def pilotSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what pilot we want to change '''
        ssn = self.__inputter.enterSSN(" pilot")

    def attendantSSN(self):
        ''' Calls a function that asks the user to input a SSN (kennitala) so we can choose what flight attendant we want to change '''
        ssn = self.__inputter.enterSSN(" flight attendant")

    def whileEditingEmpScreen(self):
        ''' This asks the user what he would like to change '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Editing employee screen")
            choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane Type", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.phoneEditScreen, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def phoneEditScreen(self):
        ''' This shows the user what phones he can change. '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Editing employee phone screen")
            choice_list = ["1 - Change Home Phone Number", "2 - Change Mobile Number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def showEmpScreen(self):
        ''' This asks what kind of employee he would like to show '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Show employees screen")
            choice_list = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", "4 - Show Hardest Working Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1": self.miscFilterScreen, "2" : self.pilotFilterScreen, "3" : self.attFilterScreen, "4" : self.showHardestWorking, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def miscFilterScreen(self):
        ''' This is the any employee show screen, here a user can choose what he wants to display, whether it's every employee or a specific employee (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Filter employee screen")
            choice_list = ["1 - Show all employees", "2 - Show employees at work on day/week", "3 - Show employees not at work on day/week", "4 - Look for employee by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__data_printer.printAllEmps , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.showEmployeeSSN, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def showEmployeeSSN(self):
        ssn = input("Enter a pilot's SSN (kennitala): ")
        self.__data_printer.printEmpSSN(ssn)
        pass

    def attFilterScreen(self):
        ''' This is the flight attendant show screen, here a user can choose what he wants to display, whether it's every flight attendant or a specific flight attendant (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Filter flight attendant screen")
            choice_list = ["1 - Show all attendants", "2 - Show attendants at work on day/week", "3 - Show attendants not at work on day/week", "4 - Look for attendant by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__data_printer.printAllAttendants , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.showAttendantSSN, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def showAttendantSSN(self):
        ssn = input("Enter a pilot's SSN (kennitala): ")
        self.__data_printer.printAttendantSSN(ssn)
        pass
        
    def pilotFilterScreen(self):
        ''' This is the pilot show screen, here a user can choose what he wants to display, whether it's every pilot or a specific pilot (searched by SSN) '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Filter pilot screen")
            choice_list = ["1 - Show all pilots", "2 - Show pilots at work on day/week", "3 - Show pilots not at work on day/week", "4 - Look for pilot by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__data_printer.printAllPilots , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.showPilotSSN, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def showPilotSSN(self):
        ssn = input("Enter a pilot's SSN (kennitala): ")
        self.__data_printer.printAttendantSSN(ssn)
        pass
        
    def dayWeekScreen(self):
        ''' This asks the user if he wants to display employees working or not working for day or for week '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Day/Week screen")
            choice_list = ["1 - Show by day", "2 - Show by week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def atWorkScreen(self):
        ''' This is the screen that leads to displaying every employee/pilot/flight attendant that's at work on a chosen day or a chosen week '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("At work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing , "2" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def notAtWorkScreen(self):
        ''' This is the screen that leads to displaying every employee/pilot/flight attendant that's not at work on a chosen day or a chosen week '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Not at work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def airplaneScreen(self):
        ''' This screen shows the user what he can do with airplanes, then asks for an input '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Airplane screen")
            choice_list = ["1 - Show All Airplanes", "2 - Add Airplanes", "3 - Show Pilots Sorted by plane make", "4 - Show Pilots For Specific Plane Make", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.showAllAirplanes, "2" : self.addAirplane, "3" : self.showPilotsSortedByPlanes, "4" : self.specificPlaneScreen, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def specificPlaneScreen(self):
        ''' This is where the user inputs a plane make and receives a print of every pilot that's allowed to fly that type of plane '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Choose a plane make")
            choice_list = ["1 - BAE146", "2 - Fokker F28", "3 - Fokker F100", BACK_STR, QUIT_STR]
            choice_dict = {"1" : "NABAE146", "2" : "NAFokkerF28", "3" : "NAFokkerF100", "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                if inp == "B" or inp == "Q": # So that it doesn't display an empty box when enter back or quit
                    nextScreen = choice_dict.get(inp)
                    nextScreen()
                else:
                    plane_type = choice_dict.get(inp)
                    self.showPilotsForPlaneType(plane_type)
            else:
                print("Input is invalid!")

    def showAllAirplanes(self):
        # Show all airplanes
        self.__data_printer.printAllPlanes()
        
    def addAirplane(self):
        # Adding Airplane
        pass

    def showPilotsSortedByPlanes(self):
        pass

    def showPilotsForPlaneType(self, plane_type):
        # ShowPilotsForSpecificPlane
        self.__data_printer.printPilotForPlane(plane_type)
        
    def tripAndLocScreen(self):
        ''' This is a screen that allows the user to choose between showing work trips or locations screens '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Trips and locations screen")
            choice_list = ["1 - Locations", "2 - Work Trips", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.locationScreen, "2" : self.workTripsScreen, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def workTripsScreen(self):
        ''' This shows the user the choices he can make with work trips '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Work trips screen")
            choice_list = ["1 - Add Work Trip", "2 - Show Work Trips", "3 - Show An Employee's Work Trip", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__inputter.addWorkTrip, "2" : self.filterWorkTripsScreen, "3" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def locationScreen(self):
        ''' This shows the user the choices he can make with locations '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Locations screen")
            choice_list = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", "4 - Show Most Popular Location", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__inputter.addLocation, "2" : self.whileEditingLocScreen, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def whileEditingLocScreen(self):
        ''' This screen shows what the user can change about locations '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Editing location screen")
            choice_list = ["1 - Change emergency contact name", "2 - Change emergency contact phone number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def filterWorkTripsScreen(self):
        ''' This screen shows the user what choices he has for displaying work trip '''
        inp = ""
        while inp != "B":
            self.__ui_printer.headerDisplay("Filter work trips screen")
            choice_list = ["1 - Show All Trips", "2 - Show For Day", "3 - Show For Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" :self.doNothing, "3" : self.doNothing, "B" : self.back, "Q" : sys.exit}
            self.__ui_printer.display(choice_list)
            inp = self.askForInput()
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")