class SortData:
    def __init__(self):
        pass
    
    def sortPilots(self, data):
        """ Takes all crew and only keeps the pilots """
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['role'] == "Pilot": # Checks if the role == Pilot and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortAttendants(self, data):
        """ Takes all crew and only keeps the flight attendants """
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Flight Attendant": # Checks if the rank == Flight Attendant and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortEmployeeSSN(self, data, ssn):
        for item in data: # Iterates through every item in the crew list
            if item['ssn'] == ssn: # Checks if the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortPilotSSN(self, data, ssn):
        for item in data: # Iterates through every item in the crew list
            if item['role'] == "Pilot" and item['ssn'] == ssn: # Checks if the role == Pilot and the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortAttendantSSN(self, data, ssn):
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Flight Attendant" and item['ssn'] == ssn: # Checks if the rank == Flight Attendant and the SSN is correct and returns it if so, else returns none
                return item
        return None