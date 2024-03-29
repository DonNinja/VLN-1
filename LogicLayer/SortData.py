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
    
    def sortCaptains(self, data):
        ''' This searches through every employee and returns a list of only captains '''
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Captain": # Checks if the rank == Captain and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortCopilots(self, data):
        ''' This searches through every employee and returns a list of only copilots '''
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Copilot": # Checks if the rank == Copilot and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortAttendants(self, data):
        """ Takes all crew and only keeps the flight attendants """
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['role'] == "Cabincrew": # Checks if the rank == Flight Attendant and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortFSM(self, data):
        ''' This searches through every employee and returns a list of only flight service managers '''
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['rank'] == "Flight Service Manager": # Checks if the rank == Flight Service Manager and adds it to the return list if so
                ret_list.append(item)
        return ret_list
    
    def sortCabincrew(self, data):
        ret_list = []
        for item in data: # Iterates through every item in the crew list
            if item['role'] == "Cabincrew": # Checks if the role == Cabincrew and adds it to the return list if so
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
            if item['role'] == "Cabincrew" and item['ssn'] == ssn: # Checks if the rank == Flight Attendant and the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortPilotsByPlane(self, data, plane_type):
        """ This checks if pilot has license for set plane """
        ret_list = []
        for item in data: # Iterates through every item in the aircraft list
            if item['role'] == "Pilot" and item['licence'] == plane_type: # Checks if employee is pilot and if they have an active licence for the chosen plane
                ret_list.append(item)
        return ret_list

    def sortworkTripNumber(self):
        pass
    
    def sortEmpTrips(self, data_list, ssn):
        ''' This sorts emps that are on flight trip '''
        ret_list = []
        for item in data_list: # Iterates through every item in the flight list
            if item['captain'] == ssn or item['copilot'] == ssn or item['fsm'] == ssn or item['fa1'] == ssn or item['fa2'] == ssn: # Checks if emp is on the trip
                ret_list.append(item)
        return ret_list

    def dateSorter(self, data, date):
        ''' This sorts by date '''
        ret_list = []
        for item in data: # Iterates through every item in the flight list 
            parsed_item_date = dateutil.parser.parse(item['departure'])
            item_date = str(parsed_item_date.date())
            if item_date == date:
                ret_list.append(item)
        return ret_list

    def sortOrderByPlane(self, data):
        ''' This sorts by plane '''
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


    def weekSorter(self, data, start_date):
        ''' This returns a week starting from starting date input '''
        ret_list = []
        date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d') # Turns start date into usable format
        for i in range(8): # 7 days so we go up to 8
            i = i # Bara svo það komi ekki upp error
            for item in data: # Iterates through every item in the flight list 
                parsed_item_date = dateutil.parser.parse(item['departure']) # Takes in the departure date and turns it into usable format
                item_date = str(parsed_item_date.date()) # Make the var above a str
                if item_date == str(date_obj.date()): # If our start date == item in flight list
                    ret_list.append(item) # Append item
            date_obj += datetime.timedelta(days=1) # Add one to our counter
        return ret_list


    def empsNotAtWork(self, all_emps, emps_at_work):
        ret_list = []
        for emp in all_emps:
            if emp['ssn'] not in emps_at_work:
                ret_list.append(emp['ssn'])
        return ret_list

    def empsAtWork(self, trips, date):
        emps_working_dict = {}
        
        for item in trips:
            dict_list = []
            dep_compare_date = item["departure"]
            dep_compare_date = dep_compare_date.split("T")
            arr_compare_date = item["arrival"]
            arr_compare_date = arr_compare_date.split("T")
            if dep_compare_date[0] == date or arr_compare_date[0] == date:
                if item["arrivingAt"] != "KEF":
                    if item["captain"] != "X":
                        dict_list.append(item['captain'])
                    if item["copilot"] != "X":
                        dict_list.append(item['copilot'])
                    if item["fsm"] != "X":
                        dict_list.append(item['fsm'])
                    if item["fa1"] != "X":
                        dict_list.append(item['fa1'])
                    if item["fa2"] != "X":
                        dict_list.append(item['fa2'])
                    emps_working_dict[item['arrivingAt']] = dict_list
        return emps_working_dict

    def sortForTrip(self, flight_num_list, data):
        ''' This returns a trip with the input flight number '''
        ret_list = []
        for item in data: # Iterates through every item in the flight list 
            if item['flightNumber'] == flight_num_list[0] or item['flightNumber'] == flight_num_list[1]:
                ret_list.append(item)
        return ret_list

    def tripNumberSorter(self, flight_num, all_trips):
        ''' This returns both flights to and from'''
        if flight_num[:2] == "NA": # All flightNumbers start with NA
            flight_num = flight_num[2:]
        flight_num = int(flight_num)
        ret_list = []
        for i in range(2):
            if i == 1:
                flight_num += 1
            for line in all_trips: # Iterates through every item in the flight list 
                if line['flightNumber'] == 'NA' + str(flight_num).zfill(4):
                        ret_list.append(line)
        return ret_list

    def sortForLocation(self, loc_id, data):
        ''' This takes in location id from user and checks if it is in the file '''
        ret_list = []
        if loc_id == "KEF":
            return None
        for item in data: # Iterates through every item in the location list
            if item['id'] == loc_id:
                return item
        return None

    def sortSpecificPlane(self, data, plane_insignia):
        ''' This checks if plane in signa is in the file '''
        for item in data:
            if item['planeInsignia'] == plane_insignia:  # Iterates through every item in the aircraft list
                return item
        return None
    
    def sortSpecificCaptain(self, data, ssn):
        ''' This checks if a specific captain is in the file '''
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Captain':  # Iterates through every item in the crew list
                return item
        return None
    
    def sortSpecificCopilot(self, data, ssn):
        ''' This checks if a specific copilot is in the file '''
        for item in data: # Iterates through every item in the crew list
            if item['ssn'] == ssn and item['rank'] == 'Copilot':  
                return item
        return None
    
    def sortSpecificFSM(self, data, ssn):
        ''' This checks if a specific flight service manager is in the file '''
        for item in data: # Iterates through every item in the crew list
            if item['ssn'] == ssn and item['rank'] == 'Flight Service Manager': 
                return item
        return None
    
    def sortSpecificAttendant(self, data, ssn):
        ''' This checks if a specific flight attendant is in the file '''
        for item in data: # Iterates through every item in the crew list
            if item['ssn'] == ssn and item['rank'] == 'Flight Attendant':
                return item
        return None
    
    def sortEmpTripsForWeek(self, data, start_date, ssn):
        ''' This checks if a certain employee is working that week '''
        ret_list = []
        all_week_trips = self.weekSorter(data, start_date)
        for item in all_week_trips: # Iterates through every item in the flight list
            if item['captain'] == ssn or item['copilot'] == ssn or item['fsm'] == ssn or item['fa1'] == ssn or item['fa2'] == ssn: # Returns every employee on that trip
                ret_list.append(item)
        return ret_list
