import csv
class crew():
    def __init__(self,ssn,name,role,rank,licens,address,phonenumber):
        self.ssn = ssn
        self.name = name
        self.role = role
        self.rank = rank
        self.licens = licens
        self.address = address
        self.phonenumber = phonenumber

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.ssn,self.name,self.role,self.rank,self.licens,self.address,self.phonenumber) 


class pilot(crew):
    pass

class flightattendant(crew):
    pass

class planeType():
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

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.planeInsignia,self.planeTypeId,self.planeType,self.model,self.capacity,self.emptyWeight,self.maxTakeOffWeight,self.unitThrust,self.serviceCeiling,self.length,self.wingspan) 



class plane():
    def __init__(self,planeInsignia,planeTypeId):
        self.planeInsignia = planeInsignia
        self.planeTypeId = planeTypeId

    def __str__(self):
        return "{}\n{}".format(self.planeInsignia,self.planeTypeId)


class UpcomingFlights():
    def __init__(self,flightNumber,DepartingFrom,arrivingAt,Departure,arrival):
        self.flightNumber = flightNumber
        self.DepartingFrom = DepartingFrom
        self.arrivingAt = arrivingAt
        self.Departure = Departure
        self.arrival = arrival

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}".format(self.flightNumber,self.DepartingFrom,self.arrivingAt,self.Departure,self.arrival)
        


class PastFlight():
    def __init__(self,flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2):
        self.flightNumber = flightNumber
        self.departingFrom = departingFrom
        self.arrivingAt = arrivingAt
        self.departure = departure
        self.arrival = arrival
        self.aircraftID = aircraftID
        self.captain = captain
        self.copilot = copilot
        self.fsm = fsm
        self.fa1 = fa1
        self.fa2 = fa2


    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.flightNumber,self.departingFrom,self.arrivingAt,self.departure,self.arrival,self.aircraftID,self.captain,self.copilot,self.fsm,self.fa1,self.fa2)



#function that takes csv files and converts the information to 
#instances of a class stored in a dictionary, for example ssn 
#gives an employee

def getupcomingflights():
    filename = "UpcomingFlights.csv"
    
    lis = []
    UpcomingFlightsdict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            flightNumber,DepartingFrom,arrivingAt,Departure,arrival = row
            lis.append("upcomingflights"+str(counter))
            lis[counter] = UpcomingFlights(flightNumber,DepartingFrom,arrivingAt,Departure,arrival)
            UpcomingFlightsdict[flightNumber] = lis[counter]
            counter = counter + 1
        return UpcomingFlightsdict

def getcrew():
    filename = "Crew.csv"
  
    lis = []
    crewdict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            lis.append("crewmember"+str(counter))
            ssn,name,role,rank,licenc,address,mobile_phone_num,home_phone_num = row

            lis[counter] = crew(ssn,name,role,rank,licenc,address,mobile_phone_num,home_phone_num)
            crewdict[ssn] = lis[counter]
            counter = counter + 1 
        return crewdict



def getplanetype():
    filename = "AircraftType.csv"
    
    lis = []
    planeTypedict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            lis.append("planetype"+str(counter))
            planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan = row
            lis[counter] = planeType(planeTypeId,planeType,model,capacity,emptyWeight,maxTakeoffWeight,unitThrust,serviceCeiling,length,height,wingspan)
            planeTypedict[planeTypeId] = lis[counter]
            counter = counter + 1 
        return planeTypedict

def getplane():
    filename = "Aircraft.csv"
    
    lis = []
    planedict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            lis.append("plane"+str(counter))
            planeInsignia,planeTypeId = row

            lis[counter] = plane(planeInsignia,planeTypeId)
            planedict[planeInsignia] = lis[counter]
            counter = counter + 1 
        return planedict



def getpastflights():
    filename = "PastFlights.csv"
    lis = []
    past_flight_dict = {}
    with open(filename, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        counter = 0
        for row in csvreader:
            lis.append("pastflight"+ str(counter))
            flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2 = row

            lis[counter] = PastFlight(flightNumber,departingFrom,arrivingAt,departure,arrival,aircraftID,captain,copilot,fsm,fa1,fa2)
            past_flight_dict[flightNumber] = lis[counter]
            counter = counter + 1 
        return past_flight_dict


def newEmployee(crewdict, ssn, name, role, rank, licens, address, mobile, home_phone):
    with open('crew.csv', 'a',newline='') as newFile:
        newFileWriter = csv.writer(newFile)
        newFileWriter.writerow([ssn,name,role,rank,licens,address, mobile, home_phone])
        crewdict[ssn] = crew(ssn,name,role,rank,licens,address, mobile, home_phone)
        return crewdict


dict1 = getcrew()
inp = input("type in ssn to get employee")   
print(dict1[inp])


        