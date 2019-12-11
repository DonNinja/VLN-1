import csv

class ReadData():
    def __init__(self):
        self.__data = []

    def readCrew(self):
        """ This reads the Crew.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Crew.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readAircraft(self):
        """ This reads the Aircraft.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Aircraft.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readAircraftType(self):
        """ This reads the AircraftType.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/AircraftType.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readDestinations(self):
        """ This reads the Destinations file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Destinations.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data

    def readPastFlights(self):
        """ This reads the PastFlights.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/PastFlights.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readAllFlights(self):
        """ This reads the Flights.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/Flights.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readUpcomingFlights(self):
        """ This reads the UpcomingFlights.csv file and returns the ordered dictionary """
        self.__data.clear()
        with open("./STUDENTDATA/UpcomingFlights.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
    
    def readAddUpcomingFlights(self):
        """ This reads the UpcomingFlights.csv file and returns the ordered dictionary """
        with open("./STUDENTDATA/UpcomingFlights.csv", "r") as file_stream:
            file_reader = csv.DictReader(file_stream)
            for line in file_reader:
                self.__data.append(line)
        file_stream.close()
        return self.__data
        