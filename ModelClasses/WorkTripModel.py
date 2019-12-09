class WorkTrip:
    def __init__(self, dep_flight_id, ret_flight_id):
        self.__dep_flight_id = dep_flight_id
        self.__ret_flight_id = ret_flight_id

    def setdepFlightId(self,newdepflightid):
        self.__dep_flight_id = newdepflightid

    def getdepFlightId(self):
        return self.__dep_flight_id

    def setRetFlightId(self,newretflightid):
        self.__ret_flight_id = newretflightid

    def getRetFlightId(self):
        return self.__ret_flight_id

    def __str__(self):
        return "{}\n{}".format(self.__dep_flight_id,self.__ret_flight_id)
