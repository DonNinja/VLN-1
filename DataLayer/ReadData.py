import csv

class ReadData():
    def __init__(self):
        self.__data = []

    def readCrew(self):
        """ This reads the Crew.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Crew.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraft(self):
        """ This reads the Aircraft.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Aircraft.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readAircraftType(self):
        """ This reads the AircraftType.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/AircraftType.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readDestinations(self):
        """ This reads the Destinations file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Destinations.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data

    def readPastFlights(self):
        """ This reads the PastFlights.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/PastFlights.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
    
    def readUpcomingFlights(self):
        """ This reads the UpcomingFlights.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/UpcomingFlights.csv", "r") as crew_file:
            crew_reader = csv.DictReader(crew_file)
            for line in crew_reader:
                self.__data.append(line)
        return self.__data
        