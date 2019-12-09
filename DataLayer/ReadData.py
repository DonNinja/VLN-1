import csv

class ReadData():
    def __init__(self):
        self.__data = []

    def readCrew(self):
        self.__data.clear()
        with open("./STUDENTDATA/Crew.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def read(parameter_list):
        pass