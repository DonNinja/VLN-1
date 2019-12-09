class Flight:
    def __init__(self, flight_number, departing_from, arriving_at, departure, arrival, aircraft_ID, captain, copilot, fsm, fa1, fa2=""):
        self.__flight_number = flight_number
        self.__departing_from = departing_from
        self.__arriving_at = arriving_at
        self.__departure = departure
        self.__arrival = arrival
        self.__aircraft_ID = aircraft_ID
        self.__captain = captain
        self.__copilot = copilot
        self.__fsm = fsm
        self.__fa1 = fa1
        self.__fa2 = fa2

    def setFlightNumber(self,newflightnumber):
        self.__flight_number = newflightnumber

    def getFLightNumber(self):
        return self.__flight_number

    def setDepartingFrom(self,newdepartingfrom):
        self.__departing_from = newdepartingfrom

    def getDepartingFrom(self):
        return self.__departing_from

    def setArrivingAt(self,newarrivingat):
        self.__arriving_at = newarrivingat

    def getArrivingAt(self):
        return self.__arriving_at

    def setDeparture(self,newdeparture):
        self.__departure = newdeparture

    def getDeparture(self):
        return self.__departure

    def setArrival(self,newarrival):
        self.__arrival = newarrival

    def getArrival(self):
        return self.__arrival

    def setAircraftId(self,newaircraftid):
        self.__aircraft_ID = newaircraftid

    def getAircraftId(self):
        return self.__aircraft_ID

    def setCaptain(self,newcaptain):
        self.__captain = newcaptain

    def getCaptain(self):
        return self.__captain

    def setCopilot(self,newcopilot):
        self.__copilot = newcopilot

    def getCopilot(self):
        return self.__copilot

    def setfsm(self,newfsm):
        self.__fsm = newfsm

    def getfsm(self):
        return self.__fsm

    def setfa1(self,newfa1):
        self.__fa1 = newfa1

    def getfa1(self):
        return self.__fa1

    def setfa2(self,newfa2):
        self.__fa2 = newfa2

    def getfa2(self):
        return self.__fa2

    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.__flight_number,
                                                                self.__departing_from,
                                                                self.__arriving_at,self.__departure,
                                                                self.__arrival, self.__aircraft_ID, 
                                                                self.__captain,self.__copilot,
                                                                self.__fsm,self.__fa1,
                                                                self.__fa2)