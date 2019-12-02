SCREENLENGTH = 40
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
    
<<<<<<< HEAD
def startScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {1 : employeeScreen(), 2 : airplaneScreen(), 3 : airplaneScreen(), "Q" : exit()}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)


def employeeScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {1 : employeeScreen(), 2 : airplaneScreen(), 3 : airplaneScreen(), "Q" : exit()}
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass

def create_crew_list(file_stream):
    crew_list = []
    for line in file_stream:
        crew_list.append() = line.split(",")
    return crew_list
=======
# def create_crew_list(file_stream):
#     crew_list = []
#     for line in file_stream:
#         to_add_to_crew_list = line.split(",")
#         crew_list.append(to_add_to_crew_list)
#         return crew_list
>>>>>>> b04d5f2f74302d809d2869745125f28707c0e970

        
def open_file(file_name):
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

file_name = "crew.csv"
file_stream = open_file(file_name)
<<<<<<< HEAD
display_crew = create_crew_list(file_stream)
=======
# display_crew = create_crew_list(file_stream)
    
def startScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {"1" : employeeScreen, "2" : airplaneScreen, "3" : airplaneScreen, "Q" : exit}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)()

def employeeScreen():
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
>>>>>>> b04d5f2f74302d809d2869745125f28707c0e970

def addAttendantScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass

def showEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def editEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def miscFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def attFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def pilotFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def atWorkScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def notAtWorkScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def airplaneScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def tripAndLocScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def workTripsScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def locationScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def whileEditingScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def phoneEditScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    pass
    
def filterWorkTripsScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice_dict.get(inp)
    
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