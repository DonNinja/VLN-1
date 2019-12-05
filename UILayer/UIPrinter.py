SCREENLENGTH = 60

class UIPrinter:
    def __init__(self):
        pass

    def printUpperLine(self):
        line = "╟"
        while len(line) < SCREENLENGTH-1:
            line += "─"
        line += "╢"
        print(line)
    
    def printLowerLine(self):
        line = "╚"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╝"
        print(line)

    def printHeaderUpperLine(self):
        print()
        line = "╔"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╗"
        print(line)
        
    def printHeaderUnderLine(self):
        # line = "╚"
        # while len(line) < SCREENLENGTH-1:
        #     line += "═"
        # line += "╝"
        # print(line)
        pass

    def headerDisplay(self, screen_name):
        self.printHeaderUpperLine()
        half_screen_length = round(SCREENLENGTH/2, 0)
        half_screen_name_length = round(len(screen_name)/2, 0)
        screen_length_center = half_screen_length - half_screen_name_length
        line = "║"
        while len(line) < screen_length_center:
            line += " "
        line += screen_name
        while len(line) < SCREENLENGTH-1:
            line += " "
        line += "║"
        print(line)
        self.printHeaderUnderLine()

    def display(self, choice_list):
        self.printUpperLine()
        for choice in choice_list:
            line = "║    " + choice
            while len(line) < SCREENLENGTH-1:
                line += " "
            line += "║"
            print(line)
        self.printLowerLine()