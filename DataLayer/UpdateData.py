import csv

class UpdateData:
    def __init__(self):
        self.__data = []

    def readCrew(self):
        with open(".\\STUDENTDATA\\Crew.csv", "r") as crew_file:
            pass
    
    def readAircraft(self):
        with open("./STUDENTDATA/Aircraft.csv", "r") as crew_file:
            pass
    
    def readAircraftType(self):
        with open("./STUDENTDATA/AircraftType.csv", "r") as crew_file:
            pass
    
    def readDestinations(self):
        with open("./STUDENTDATA/Destination.csv", "r") as crew_file:
            pass

    def readPastFlights(self):
        with open("./STUDENTDATA/PastFlights.csv", "r") as crew_file:
            pass
    
    def readUpcomingFlights(self):
        with open("./STUDENTDATA/UpcomingFlights.csv", "r") as crew_file:
            pass