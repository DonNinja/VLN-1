SCREENLENGTH = 40
BACK_STR = "B - Back"
QUIT_STR = "Q - Quit"


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

def display_employee_screen():



choice_list = ["1 - Single Kek", "2 - Double kek",
               "3 - Triple kek", BACK_STR, QUIT_STR]

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



display(choice_list)

# Böddi löpp