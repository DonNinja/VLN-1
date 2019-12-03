
class crew():
    def __init__(self,ssn,name,role,rank,license1):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.license1 = license1


class plane():
    def __init__(self,planeInsignia,planeTypeId,planeType,model,capacity,emptyWeight,maxTakeOffWeight,unitThrust,serviceCeiling,length,height,wingspan):
        self.planeInsignia = planeInsignia
        self.planeTypeId = planeTypeId
        self.planeType = planeType
        self.model = model
        self.capacity = capacity
        self.emptyWeight = emptyWeight
        self.maxTakeOffWeight = maxTakeOffWeight
        self.unitThrust = unitThrust
        self.serviceCeiling = serviceCeiling
        self.length = length
        self.height = height
        self.wingspan = wingspan


class UpcomingFlights():
    def __init__(self,flightNumber,DepartingFrom,arrivingAt,Departure,arrival):
        self.flightNumber = flightNumber
        self.DepartingFrom = DepartingFrom
        self.arrivingAt = arrivingAt
        self.Departure = Departure
        self.arrival = arrival
        


class PastFlight(UpcomingFlights):
    def __init__(self,aircraftID,captain,copilot,fsm,fa1,fa2):
        self.aircraftID = aircraftID
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2


import csv
COPILOT = 'Copilot'
 
# csv file name
filename = "UpcomingFlights.csv"
 
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    counter = 1
    for row in csvreader:
        flightNumber,DepartingFrom,arrivingAt,Departure,arrival = row
        flightnr = flightNumber
        locals()["flight"+str(counter)] = UpcomingFlights(flightNumber,DepartingFrom,arrivingAt,Departure,arrival)
        counter = counter + 1


        


