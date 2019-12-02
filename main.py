SCREENLENGTH = 40
BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"

def askForInput():
    return input("Enter a choice: ")

def back():
    return

def printLine():
    line = ""
    while len(line) < SCREENLENGTH:
        line += "="
    print(line)

def choice(choice_dict, inp):
    return choice_dict.get()

def display(choice_list):
    printLine()
    for choice in choice_list:
        line = "|    " + choice
        while len(line) < SCREENLENGTH-1:
            line += " "
        line += "|"
        print(line)
    printLine()
    
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

def addEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass

def showEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def editEmpScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def miscFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def attFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def pilotFilterScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def atWorkScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def notAtWorkScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def airplaneScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def tripAndLocScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def workTripsScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def locationScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def whileEditingScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def phoneEditScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    pass
    
def filterWorkTripsScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)
    
def dayWeekScreen():
    choice_list = ["1 - Employees", "2 - Airplanes", "3 - Trips and locations", QUIT_STR]
    choice_dict = {}
    display(choice_list)
    inp = askForInput()
    choice(choice_dict, inp)

startScreen()