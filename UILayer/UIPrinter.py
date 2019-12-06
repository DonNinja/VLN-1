SCREENLENGTH = 60

class UIPrinter:
    def __init__(self):
        pass

<<<<<<< HEAD
    def printUpperLine(self):
        line = "╔"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╗"
=======
    def printHeaderSeparator(self):
        line = "╟"
        while len(line) < SCREENLENGTH-1:
            line += "─"
        line += "╢"
>>>>>>> 41a3b8be5f5d4982726b233e349d0d9fa9f472f3
        print(line)
    
    def printLowerLine(self):
        line = "╚"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╝"
        print(line)

    def printHeaderUpperLine(self):
<<<<<<< HEAD
        line = "┌"
        while len(line) < SCREENLENGTH-1:
            line += "─"
        line += "┐"
        print(line)
        
    def printHeaderUnderLine(self):
        line = "└"
        while len(line) < SCREENLENGTH-1:
            line += "─"
        line += "┘"
=======
        print()
        line = "╔"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╗"
>>>>>>> 41a3b8be5f5d4982726b233e349d0d9fa9f472f3
        print(line)

    def headerDisplay(self, screen_name):
        self.printHeaderUpperLine()
        half_screen_length = round(SCREENLENGTH/2, 0)
        half_screen_name_length = round(len(screen_name)/2, 0)
        screen_length_center = half_screen_length - half_screen_name_length
<<<<<<< HEAD
        line = "|"
=======
        line = "║"
>>>>>>> 41a3b8be5f5d4982726b233e349d0d9fa9f472f3
        while len(line) < screen_length_center:
            line += " "
        line += screen_name
        while len(line) < SCREENLENGTH-1:
            line += " "
<<<<<<< HEAD
        line += "|"
        print(line)
        self.printHeaderUnderLine()

    def display(self, choice_list):
        self.printUpperLine()
=======
        line += "║"
        print(line)

    def display(self, choice_list):
        self.printHeaderSeparator()
>>>>>>> 41a3b8be5f5d4982726b233e349d0d9fa9f472f3
        for choice in choice_list:
            line = "║    " + choice
            while len(line) < SCREENLENGTH-1:
                line += " "
            line += "║"
            print(line)
        self.printLowerLine()