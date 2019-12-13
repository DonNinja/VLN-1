import csv

def readAllFlights():
    """ This reads the Flights.csv file and returns the ordered dictionary """
    data = []
    with open("./STUDENTDATA/Flights.csv", "r") as file_stream:
        file_reader = csv.DictReader(file_stream)
        for line in file_reader:
            data.append(line)
    file_stream.close()
    return data

def flight_number():
    flight_number = input("Enter flightnumber: ")
    return flight_number

def checking_for_flight(flight_list, flight_info):
    for line in flight_list:
        if line['flightNumber'] == flight_info:
            print(line)


def main():
    flight_list = readAllFlights()
    flight_info = flight_number()
    checking_for_flight(flight_list, flight_info)


main()