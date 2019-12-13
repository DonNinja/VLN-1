import dateutil
import datetime
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
    
    def sortCabincrew(self, data):
        ret_list = []
        for item in data:
            if item['role'] == "Cabincrew":
                ret_list.append(item)
        return ret_list
    
    def sortEmployeeSSN(self, data, ssn):
        """ This returns the employee with the inputted SSN, else None if the employee is not found """
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['ssn'] == ssn: # Checks if the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortPilotSSN(self, data, ssn):
        """ This returns the pilot with the inputted SSN, else None if the pilot is not found """
        for item in data: # Iterates through every item in the crew list
            if item['role'] == "Pilot" and item['ssn'] == ssn: # Checks if the role == Pilot and the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortAttendantSSN(self, data, ssn):
        """ This returns the flight attendant with the inputted SSN, else None if the flight attendant is not found """
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Flight Attendant" and item['ssn'] == ssn: # Checks if the rank == Flight Attendant and the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortPilotsByPlane(self, data, plane_type):
        """ This  """
        ret_list = []
        for item in data:
            if item['role'] == "Pilot" and item['licence'] == plane_type: # Checks if employee is pilot and if they have an active licence for the chosen plane
                ret_list.append(item)
        return ret_list

    def sortworkTripNumber(self):
        pass
    
    def sortEmpTrips(self, data_list, ssn):
        ret_list = []
        for item in data_list:
            if item['captain'] == ssn or item['copilot'] == ssn or item['fsm'] == ssn or item['fa1'] == ssn or item['fa2'] == ssn:
                ret_list.append(item)
        return ret_list

    def dateSorter(self, data, date):
        ret_list = []
        for item in data:
            parsed_item_date = dateutil.parser.parse(item['departure'])
            item_date = str(parsed_item_date.date())
            if item_date == date:
                ret_list.append(item)
        return ret_list

    def sortOrderByPlane(self, data):
        ret_list = []
        for item in data:
            if item['licence'] == 'NABAE146':
                ret_list.append(item)
        for item in data:
            if item['licence'] == 'NAFokkerF28':
                ret_list.append(item)
        for item in data:
            if item['licence'] == 'NAFokkerF100':
                ret_list.append(item)
        return ret_list

    def weekSorter(self, data , start_date):
        ret_list = []
        date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        for i in range(8):
            i = i
            for item in data:
                parsed_item_date = dateutil.parser.parse(item['departure'])
                item_date = str(parsed_item_date.date())
                if item_date == str(date_obj.date()):
                    ret_list.append(item)
            date_obj += datetime.timedelta(days=1)
        return ret_list

    def sortForTrip(self, flight_num_list, data):
        ret_list = []
        for item in data:
            if item['flightNumber'] == flight_num_list[0] or item['flightNumber'] == flight_num_list[1]:
                ret_list.append(item)
        return ret_list
    
    def sortForLocation(self, loc_id, data):
        ret_list = []
        if loc_id == "KEF":
            return None
        for item in data:
            if item['id'] == loc_id:
                return item
        return None
    
    def sortSpecificPlane(self, data, plane_id):
        for item in data:
            if item['planeInsignia'] == plane_id:
                return item
        return None
    
    def sortSpecificCaptain(self, data, ssn):
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Captain':
                return item
        return None
    
    def sortSpecificCopilot(self, data, ssn):
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Copilot':
                return item
        return None
    
    def sortSpecificFSM(self, data, ssn):
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Flight Service Manager':
                return item
        return None
    
    def sortSpecificAttendant(self, data, ssn):
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Flight Attendant':
                return item
        return None