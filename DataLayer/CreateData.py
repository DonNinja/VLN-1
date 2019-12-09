import csv

class CreateData():
    def __init__(self):
        self.__data = []

    def readCrew(self):
        self.__data.clear()
        with open(".\\STUDENTDATA\\Crew.csv", "w") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraft(self):
        self.__data.clear()
        with open("./STUDENTDATA/Aircraft.csv", "w") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraftType(self):
        self.__data.clear()
        with open("./STUDENTDATA/AircraftType.csv", "w") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readDestinations(self):
        with open("./STUDENTDATA/Destination.csv", "w") as crew_file:
            pass

    def readPastFlights(self):
        self.__data.clear()
        with open("./STUDENTDATA/PastFlights.csv", "w") as crew_file:
            pass
    
    def readUpcomingFlights(self):
        with open("./STUDENTDATA/UpcomingFlights.csv", "w") as crew_file:
            pass