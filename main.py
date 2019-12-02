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

def open_file(file_name):
    try:
        file_stream = open(file_name, "r")
        return file_stream
    except FileNotFoundError:
        return None

file_name = "crew.csv"
file_stream = open_file(file_name)


choice_list = ["1 - Single Kek", "2 - Double kek",
               "3 - Triple kek", BACK_STR, QUIT_STR]

display(choice_list)
 #geggjað comment

#hello world
