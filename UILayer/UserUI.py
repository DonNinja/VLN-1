class UserUI:
    SCREENLENGTH = 60
    BACK_STR = "B - Back"
    QUIT_STR = "Q - Quit"
    
    def __init__(self):
        pass

    def doNothing(self):
        pass
        
    def back(self):
        return

    def input_check(self, inp, choice_dict):
        for i in choice_dict:
            if inp == i:
                return True

    def printLine(self):
        line = ""
        while len(line) < SCREENLENGTH:
            line += "="
        print(line)

    def askForInput(self):
        return input("Enter a choice: ").upper()

    def printHeaderUpperLine(self):
        line = ""
        while len(line) < SCREENLENGTH:
            line += "_"
        print(line)
        
    def printHeaderUnderLine(self):
        line = ""
        while len(line) < SCREENLENGTH:
            line += "‾"
        print(line)

    def headerDisplay(self, screen_name):
        printHeaderUpperLine()
        half_screen_length = round(SCREENLENGTH/2, 0)
        half_screen_name_length = round(len(screen_name)/2, 0)
        screen_length_center = half_screen_length - half_screen_name_length
        line = "|"
        while len(line) < screen_length_center:
            line += " "
        line += screen_name
        while len(line) < SCREENLENGTH-1:
            line += " "
        line += "|"
        print(line)
        printHeaderUnderLine()

    def display(self, choice_list):
        printLine()
        for choice in choice_list:
            line = "|    " + choice
            while len(line) < SCREENLENGTH-1:
                line += " "
            line += "|"
            print(line)
        printLine()

    def startScreen(self):
        while True:
            path_list = []
            headerDisplay("Starting screen")
            #valid_inputs = 123 q
            choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
            choice_dict = {"1" : employeeScreen, "2" : airplaneScreen, "3" : tripAndLocScreen, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            #Check if input is valid
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def employeeScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Employee screen")
            choice_list = ["1 - Add Employee", "2 - Show Employee", "3 - Edit Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1" : addEmployeeScreen, "2" : showEmpScreen, "3" : editEmpScreen, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                choice_dict.get(inp)()
            else:
                print("Input is invalid!")

    def addEmployeeScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Add employee screen")
            choice_list = ["1 - Add Misc Employee", "2 - Add Pilot", "3 - Add Flight Attendant", BACK_STR,QUIT_STR]
            choice_dict = {"1": addMiscEmpScreen, "2" : addPilotScreen, "3" : addAttendantScreen, "B" : back,"Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def addMiscEmpScreen(self):
        #This is a function call to add an employee to the roster, not a screen to navigate to/from
        pass

    def addPilotScreen(self):
        #This is a function call to add an employee to the roster, not a screen to navigate to/from
        pass

    def addAttendantScreen(self):
        #This is a function call to add an employee to the roster, not a screen to navigate to/from
        pass

    def showHardestWorking(self):
        #This just displays the hardest working employee
        pass
        
    def editEmpScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Edit employees screen")
            choice_list = ["1 - Edit Any Employee", "2 - Edit Pilot", "3 - Edit Attendant", BACK_STR, QUIT_STR]
            choice_dict = {"1" :whileEditingEmpScreen, "2" :whileEditingEmpScreen, "3" :whileEditingEmpScreen, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
                
    def enterEmpSSN(self):
        ssn = input("Enter employee's Social Security Number (Kennitala): ")
        editEmpScreen(ssn)
        
    def whileEditingEmpScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Editing employee screen")
            choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane Type", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "3" : doNothing, "4" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def showEmpScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Show employees screen")
            choice_list = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", "4 - Show Hardest Working Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1": miscFilterScreen, "2" : pilotFilterScreen, "3" : attFilterScreen, "4" : showHardestWorking, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def miscFilterScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Filter employee screen")
            choice_list = ["1 - Show All Employees", "2 - Show Employees at work on day/week", "3 - Show Employees not at work on day/week", "4 - Look for Employee bt SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : atWorkScreen , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : atWorkScreen, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def attFilterScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Filter flight attendant screen")
            choice_list = ["1 - Show All Attendants", "2 - Show Attendants at work on day/week", "3 - Show Attendants not at work on day/week", "4 - Look for Attendant bt SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : atWorkScreen, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def pilotFilterScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Filter pilot screen")
            choice_list = ["1 - Show All Pilots", "2 - Show pilots at work on day/week", "3 - Show pilots not at work on day/week", "4 - Look for pilot bt SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def atWorkScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("At work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing , "2" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def notAtWorkScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Not at work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "3" : doNothing, "4" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def airplaneScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Airplane screen")
            choice_list = ["1 - Show All Airplanes", "2 - Add Airplanes", "3 - Show Pilots Sorted by plane make", "4 - Show Pilots For Specific Plane Make", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "3" : doNothing, "4" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def tripAndLocScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Trips and locations screen")
            choice_list = ["1 - Locations", "2 - Work Trips", BACK_STR, QUIT_STR]
            choice_dict = {"1" : locationScreen, "2" : workTripsScreen, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def workTripsScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Work trips screen")
            choice_list = ["1 - Add Work Trip", "2 - Show Work Trips", "3 - Show An Employee's Work Trip", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : filterWorkTripsScreen, "3" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def locationScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Locations screen")
            choice_list = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", "4 - Show Most Popular Location", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : whileEditingLocScreen, "3" : doNothing, "4" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def whileEditingLocScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Editing employee screen")
            choice_list = ["1 - Change emergency contact name", "2 - Change emergency contact phone number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

    def phoneEditScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Editing employee phone screen")
            choice_list = ["1 - Change Home Phone Number", "2 - Change Mobile Number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def filterWorkTripsScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Filter work trips screen")
            choice_list = ["1 - Show All Trips", "2 - Show For Day", "3 - Show For Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "3" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            choice_dict.get(inp)
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")
        
    def dayWeekScreen(self):
        inp = ""
        while inp != "B":
            headerDisplay("Day/Week screen")
            choice_list = ["1 - Show by day", "2 - Show by week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : doNothing, "2" : doNothing, "B" : back, "Q" : exit}
            display(choice_list)
            inp = askForInput()
            checking = input_check(inp,choice_dict)
            if checking:
                next_screen = choice_dict.get(inp)
                next_screen()
            else:
                print("Input is invalid!")

# run_ui = UserUI()

# run_ui.startScreen()