SCREENLENGTH = 60

class UIPrinter:
    def __init__(self):
        pass

    def printHeaderSeparator(self): 
        ''' Prints the vertical line for the ui '''
        line = "╟"
        while len(line) < SCREENLENGTH-1:
            line += "─"
        line += "╢"
        print(line)
    
    def printLowerLine(self):
        ''' Prints the turn line on the lower left corner '''
        line = "╚"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╝"
        print(line)

    def printUpperLine(self):
        ''' Prints the turn line on the upper left corner '''
        print()
        line = "╔"
        while len(line) < SCREENLENGTH-1:
            line += "═"
        line += "╗"
        print(line)

    def headerDisplay(self, screen_name):
        ''' Displays the header '''
        self.printUpperLine()
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

    def display(self, choice_list):
        ''' Dsiplays the lines '''
        self.printHeaderSeparator()
        for choice in choice_list:
            line = "║    " + choice
            while len(line) < SCREENLENGTH-1:
                line += " "
            line += "║"
            print(line)
        self.printLowerLine()