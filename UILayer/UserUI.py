from UILayer.UserInput import UserInput
from UILayer.UIPrinter import UIPrinter

BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"

class UserUI:
    def __init__(self):
        self.__inputter = UserInput()
        self.__printer = UIPrinter()
        pass

    def doNothing(self):
        pass

    def back(self):
        return

    def inputCheck(self, inp, choice_dict):
        for i in choice_dict:
            if inp == i:
                return True

    def askForInput(self):
        return input("\nEnter a choice: ").upper()

    def startScreen(self):
        while True:
            self.__printer.headerDisplay("Starting screen")
            choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
            choice_dict = {"1" : self.employeeScreen, "2" : self.airplaneScreen, "3" : self.tripAndLocScreen, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            #Check if input is valid
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def employeeScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Employee screen")
            choice_list = ["1 - Add Employee", "2 - Show Employee", "3 - Edit Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.addEmployeeScreen, "2" : self.showEmpScreen, "3" : self.editEmpScreen, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def addEmployeeScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Add employee screen")
            choice_list = ["1 - Add Pilot", "2 - Add Flight Attendant", BACK_STR,QUIT_STR]
            choice_dict = {"1" : self.addPilotScreen, "2" : self.addAttendantScreen, "B" : self.back,"Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def addPilotScreen(self):
        pilot_data_list = self.__inputter.addEmp("pilot")
        pass

    def addAttendantScreen(self):
        att_data_list = self.__inputter.addEmp("flight attendant")
        pass

    def showHardestWorking(self):
        #This just displays the hardest working employee
        pass
        
    def editEmpScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Edit employees screen")
            choice_list = ["1 - Edit any employee", "2 - Edit pilot", "3 - Edit flight attendant", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.anyEmpSSN, "2" : self.pilotSSN, "3" : self.attendantSSN, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def anyEmpSSN(self):
        ssn = self.__inputter.enterSSN("ny employee")
        pass

    def pilotSSN(self):
        ssn = self.__inputter.enterSSN(" pilot")
        pass

    def attendantSSN(self):
        ssn = self.__inputter.enterSSN(" flight attendant")
        pass

    def whileEditingEmpScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Editing employee screen")
            choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane Type", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def showEmpScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Show employees screen")
            choice_list = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", "4 - Show Hardest Working Employee", BACK_STR, QUIT_STR]
            choice_dict = {"1": self.miscFilterScreen, "2" : self.pilotFilterScreen, "3" : self.attFilterScreen, "4" : self.showHardestWorking, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def miscFilterScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Filter employee screen")
            choice_list = ["1 - Show all employees", "2 - Show employees at work on day/week", "3 - Show employees not at work on day/week", "4 - Look for employee by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.atWorkScreen , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.atWorkScreen, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def attFilterScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Filter flight attendant screen")
            choice_list = ["1 - Show all attendants", "2 - Show attendants at work on day/week", "3 - Show attendants not at work on day/week", "4 - Look for attendant by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.atWorkScreen, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def pilotFilterScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Filter pilot screen")
            choice_list = ["1 - Show all pilots", "2 - Show pilots at work on day/week", "3 - Show pilots not at work on day/week", "4 - Look for pilot by SSN", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing , "2" : self.atWorkScreen, "3" : self.notAtWorkScreen, "4" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def atWorkScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("At work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing , "2" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def notAtWorkScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Not at work screen")
            choice_list = ["1 - Show By Day", "2 - Show By Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def airplaneScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Airplane screen")
            choice_list = ["1 - Show All Airplanes", "2 - Add Airplanes", "3 - Show Pilots Sorted by plane make", "4 - Show Pilots For Specific Plane Make", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.showAllAirplanes, "2" : self.addAirplane, "3" : self.showPilotsSortedByPlanes, "4" : self.showPilotForSpecificPlane, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def showAllAirplanes(self):
        # Showing all airplanes
        pass
        
    def addAirplane(self):
        # Adding Airplane
        pass

    def showPilotsSortedByPlanes(self):
        # Show pilots sorted by plane make
        pass

    def showPilotForSpecificPlane(self):
        # ShowPilotsForSpecificPlane
        pass
        
    def tripAndLocScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Trips and locations screen")
            choice_list = ["1 - Locations", "2 - Work Trips", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.locationScreen, "2" : self.workTripsScreen, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
    
    def workTripsScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Work trips screen")
            choice_list = ["1 - Add Work Trip", "2 - Show Work Trips", "3 - Show An Employee's Work Trip", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.filterWorkTripsScreen, "3" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def locationScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Locations screen")
            choice_list = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", "4 - Show Most Popular Location", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.__inputter.addLocation, "2" : self.whileEditingLocScreen, "3" : self.doNothing, "4" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def whileEditingLocScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Editing employee screen")
            choice_list = ["1 - Change emergency contact name", "2 - Change emergency contact phone number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")

    def phoneEditScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Editing employee phone screen")
            choice_list = ["1 - Change Home Phone Number", "2 - Change Mobile Number", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def filterWorkTripsScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Filter work trips screen")
            choice_list = ["1 - Show All Trips", "2 - Show For Day", "3 - Show For Week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" :self.doNothing, "3" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            choice_dict.get(inp)
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")
        
    def dayWeekScreen(self):
        inp = ""
        while inp != "B":
            self.__printer.headerDisplay("Day/Week screen")
            choice_list = ["1 - Show by day", "2 - Show by week", BACK_STR, QUIT_STR]
            choice_dict = {"1" : self.doNothing, "2" : self.doNothing, "B" : self.back, "Q" : exit}
            self.__printer.display(choice_list)
            inp = self.askForInput()
            checking = self.inputCheck(inp,choice_dict)
            if checking:
                nextScreen = choice_dict.get(inp)
                nextScreen()
            else:
                print("Input is invalid!")