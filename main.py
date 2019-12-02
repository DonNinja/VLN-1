SCREENLENGTH = 60
BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"

def askForInput():
    return input("Enter a choice: ").upper()

def back():
    return ""

def printLine():
    line = ""
    while len(line) < SCREENLENGTH:
        line += "="
    print(line)

def display(choice_list):
    printLine()
    for choice in choice_list:
        line = "|    " + choice
        while len(line) < SCREENLENGTH-1:
            line += " "
        line += "|"
        print(line)
    printLine()
    
# def create_crew_list(file_stream):
#     crew_list = []
#     for line in file_stream:
#         to_add_to_crew_list = line.split(",")
#         crew_list.append(to_add_to_crew_list)
#         return crew_list

        
def open_file(file_name):
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

file_name = "crew.csv"
file_stream = open_file(file_name)
# display_crew = create_crew_list(file_stream)
    
def input_check(inp,choice_dict):
    for i in choice_dict:
        if inp == i:
            return True

def startScreen():
    #valid_inputs = 123 q b
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {"1" : employeeScreen, "2" : airplaneScreen, "3" : tripAndLocScreen, "Q" : exit}
    display(choice_list)
    inp = askForInput()
    #Check if input is valid
    checking = input_check(inp,choice_dict)
    if checking == True:
        choice_dict.get(inp)()
    else:
        print("Input is invalid!")
        startScreen()

def employeeScreen():
    choice_list = ["1 - Add Employee", "2 - Show Employee", "3 - Edit Employee", QUIT_STR]
    choice_dict = {"1" : addEmployeeScreen, "2" : showEmpScreen, "3" : editEmpScreen, "Q" : exit}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()

def addEmployeeScreen():
    while True:
        choice_list = ["1 - Add Misc Employee", "2 - Add Pilot", "3 - Add Flight Attendant", BACK_STR, QUIT_STR]
        choice_dict = {"1": addMiscEmpScreen, "2" : addPilotScreen, "3" : addAttendantScreen, "B" : back, "Q" : exit}
        choice_dict = {}
        display(choice_list)
        inp = askForInput()
        choice_dict.get(inp)()

def addMiscEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)

def addPilotScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass

def addAttendantScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass

def showEmpScreen():
    choice_list = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", QUIT_STR]
    choice_dict = {"1": miscFilterScreen, "2" : pilotFilterScreen, "3" : attFilterScreen, "B" : back, "Q" : exit}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def editEmpScreen():
    choice_list = ["1 - Edit Any Employee", "2 - Edit Pilot", "3 - Edit Attendant", QUIT_STR]
    choice_dict = {"1" : whileEditingScreen, "2" : whileEditingScreen, "3" : whileEditingScreen}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def miscFilterScreen():
    choice_list = ["1 - Show All Employees", "2 - Show Employees at work on day/week", "3 - Show Employees not at work on day/week", "4 - Look for Employee bt SSN", QUIT_STR]
    choice_dict = {"1" : atWorkScreen , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : atWorkScreen }
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def attFilterScreen():
    choice_list = ["1 - Show All Attendants", "2 - Show Attendants at work on day/week", "3 - Show Attendants not at work on day/week", "4 - Look for Attendant bt SSN", QUIT_STR]
    choice_dict = {"1" : atWorkScreen , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : atWorkScreen }
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def pilotFilterScreen():
    choice_list = ["1 - Show All Pilots", "2 - Show pilots at work on day/week", "3 - Show pilots not at work on day/week", "4 - Look for pilot bt SSN", QUIT_STR]
    choice_dict = {"1" : atWorkScreen , "2" : atWorkScreen, "3" : notAtWorkScreen, "4" : atWorkScreen }
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def atWorkScreen():
    choice_list = ["1 - Show By Day", "2 - Show By Week", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    
    
def notAtWorkScreen():
    choice_list = ["1 - Show By Day", "2 - Show By Week", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    
    
def airplaneScreen():
    choice_list = ["1 - Show All Airplanes", "2 - Add Airplanes", "3 - Show Pilots Sorted by plane make", "4 - Show Pilots For Specific Plane Make", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    
    
def tripAndLocScreen():
    choice_list = ["1 - Locations", "2 - Work Trips", QUIT_STR]
    choice_dict = {"1" : locationScreen, "2" : workTripsScreen}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def workTripsScreen():
    choice_list = ["1 - Add Work Trip", "2 - Show Work Trips", "3 - Show An Employee's Work Trip", QUIT_STR]
    choice_dict = {"2" : filterWorkTripsScreen}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def locationScreen():
    choice_list = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", "4 - Show Most Popular Location", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    
    
def whileEditingScreen():
    choice_list = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane Type", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()
    
    
def phoneEditScreen():
    choice_list = ["1 - Change Home Phone Number", "2 - Change Mobile Number", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)

    
def filterWorkTripsScreen():
    choice_list = ["1 - Show All Trips", "2 - Show For Day", "3 - Show For Week", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def dayWeekScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)

startScreen()

employee_screen = ["1 - Add Employees", "2 - Show Employees", "3 - Edit Employee", BACK_STR, QUIT_STR]
add_employee_screen = ["1 - Add Misc Employee", "2 - Add Pilot", "3 - Add Flight Attendant", BACK_STR, QUIT_STR]
show_employee_screen = ["1 - Employees", "2 - Pilots", "3 - Flight Attendants", "4 - Show Hardest Working Employee", BACK_STR, QUIT_STR]
filter_employee_screen = ["1 - Show All X", "2 - Show x At Work On Day/Week", "3 - Show x Not At Work On Day/Week", "4 - Look For x By SSN", BACK_STR, QUIT_STR]
employee_at_work_screen = ["1 - Show By Day", "2 - Show By Week" , BACK_STR, QUIT_STR]
employee_not_at_work_screen = ["1 - Show By Day,", "2 - Show By Week", BACK_STR, QUIT_STR]
edit_employee_screen = ["1 - Edit Any Employee", "2 - Edit Pilot", "3 - Edit Attendant", BACK_STR, QUIT_STR]
while_editing_employee = ["1 - Change Home Address", "2 - Change Phone Number", "3 - Change Email", "4 - Change Plane Type Rights", BACK_STR, QUIT_STR]
while_editing_phone_number = ["1 - Change Home Phone Number", "2 - Change Mobile Number", BACK_STR, QUIT_STR]

airplane_screen = ["1 - Show All Airplanes", "2 - Add Airplane", "3 - Show Pilots Sorted By Plane Make", "4 - Show Pilots For Specific Plane Make", BACK_STR, QUIT_STR]

trips_and_location_screen = ["1 - Locations", "2 - Work Trips", BACK_STR, QUIT_STR]
location_screen = ["1 - Add Location", "2 - Edit Location", "3 - Show All Locations", "4 - Show Most Popular Location", BACK_STR, QUIT_STR]
work_trips_screen = ["1 - Add Work Trip", "2 - Show Work Trip" , "3 - Show Employee's Work Trip", BACK_STR, QUIT_STR]
filter_work_trips_screen = ["1- Show All Work Trips", "2 - Show For Day", "3 - Show For Week", BACK_STR, QUIT_STR]