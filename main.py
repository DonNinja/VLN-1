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


choice_list = ["1 - Single Kek", "2 - Double kek",
               "3 - Triple kek", BACK_STR, QUIT_STR]

display(choice_list)

# Böddi löpp