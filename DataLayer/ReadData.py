import csv

class ReadData():
    def __init__(self):
        self.__data = []

    def readCrew(self):
        self.__data.clear()
        with open(".\\STUDENTDATA\\Crew.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraft(self):
        self.__data.clear()
        with open("./STUDENTDATA/Aircraft.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraftType(self):
        self.__data.clear()
        with open("./STUDENTDATA/AircraftType.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readDestinations(self):
        self.__data.clear()
        with open("./STUDENTDATA/Destination.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data

    def readPastFlights(self):
        self.__data.clear()
        with open("./STUDENTDATA/PastFlights.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readUpcomingFlights(self):
        self.__data.clear()
        with open("./STUDENTDATA/UpcomingFlights.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data