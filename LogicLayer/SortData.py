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
        for item in data:
            if item['rank'] == "Captain":
                ret_list.append(item)
        return ret_list
    
    def sortCopilots(self, data):
        ''' This searches through every employee and returns a list of only copilots '''
        ret_list = []
        for item in data:
            if item['rank'] == "Copilot":
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
        for item in data:
            if item['rank'] == "Flight Service Manager":
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
            if item['role'] == "Cabincrew" and item['ssn'] == ssn: # Checks if the rank == Flight Attendant and the SSN is correct and returns it if so, else returns none
                return item
        return None
    
    def sortPilotsByPlane(self, data, plane_type):
        """ This checks if pilot has license for set plane """
        ret_list = []
        for item in data:
            if item['role'] == "Pilot" and item['licence'] == plane_type: # Checks if employee is pilot and if they have an active licence for the chosen plane
                ret_list.append(item)
        return ret_list

    def sortworkTripNumber(self):
        pass
    
    def sortEmpTrips(self, data_list, ssn):
        ''' This sorts emps that are on flight trip '''
        ret_list = []
        for item in data_list:
            if item['captain'] == ssn or item['copilot'] == ssn or item['fsm'] == ssn or item['fa1'] == ssn or item['fa2'] == ssn: # Checks if emp is on the trip
                ret_list.append(item)
        return ret_list

    def dateSorter(self, data, date):
        ''' This sorts by date '''
        ret_list = []
        for item in data:
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
        date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d')
        for i in range(8):
            i = i # Bara svo það komi ekki upp error
            for item in data:
                parsed_item_date = dateutil.parser.parse(item['departure'])
                item_date = str(parsed_item_date.date())
                if item_date == str(date_obj.date()):
                    ret_list.append(item)
            date_obj += datetime.timedelta(days=1)
        return ret_list


    def empsnotatwork(self,trips,data):
        emps_notworking = []

        for line in trips:
            comparedate = line["departure"]
            comparedate = comparedate.split("T")
            comparedate1 = line["arrival"]
            comparedate1 = comparedate1.split("T")
            if comparedate[0] != data or comparedate1[0] != data:
                if line["captain"] != "X":
                    emps_notworking.append(line["captain"])
                elif line["copilot"] != "X":
                    emps_notworking.append(line["copilot"])
                elif line["fsm"] != "X":
                    emps_notworking.append(line["fsm"])
                elif line["fa1"] != "X":
                    emps_notworking.append(line["fa1"])
                elif line["fa2"] != "X":
                    emps_notworking.append(line["fa2"])

        return emps_notworking



    def empsatwork(self,trips,data):
        emps_working = []
        
        
        for line in trips:
            comparedate = line["departure"]
            comparedate = comparedate.split("T")
            comparedate1 = line["arrival"]
            comparedate1 = comparedate1.split("T")
            if comparedate[0] == data or comparedate1[0] == data:
                if line["arrivingAt"] != "KEF":
                    emps_working.append(line["arrivingAt"])
                    if line["captain"] != "X":
                        emps_working.append(line["captain"])
                        if line["copilot"] != "X":
                            emps_working.append(line["copilot"])
                            if line["fsm"] != "X":
                                emps_working.append(line["fsm"])
                                if line["fa1"] != "X":
                                    emps_working.append(line["fa1"])
                                    if line["fa2"] != "X":
                                        emps_working.append(line["fa2"])
            

        return emps_working

    def sortForTrip(self, flight_num_list, data):
        ''' This returns a trip with the input flight number '''
        ret_list = []
        for item in data:
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
            for line in all_trips:
                if line['flightNumber'] == 'NA' + str(flight_num).zfill(4):
                        ret_list.append(line)
        return ret_list
    
    def sortForLocation(self, loc_id, data):
        ''' This takes in location id from user and checks if it is in the file '''
        ret_list = []
        if loc_id == "KEF":
            return None
        for item in data:
            if item['id'] == loc_id:
                return item
        return None
    
    def sortSpecificPlane(self, data, plane_insignia):
        ''' This checks if plane in signa is in the file '''
        for item in data:
            if item['planeInsignia'] == plane_insignia:
                return item
        return None
    
    def sortSpecificCaptain(self, data, ssn):
        ''' This checks if a specific captain is in the file '''
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Captain':
                return item
        return None
    
    def sortSpecificCopilot(self, data, ssn):
        ''' This checks if a specific copilot is in the file '''
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Copilot':
                return item
        return None
    
    def sortSpecificFSM(self, data, ssn):
        ''' This checks if a specific flight service manager is in the file '''
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Flight Service Manager':
                return item
        return None
    
    def sortSpecificAttendant(self, data, ssn):
        ''' This checks if a specific flight attendant is in the file '''
        for item in data:
            if item['ssn'] == ssn and item['rank'] == 'Flight Attendant':
                return item
        return None
    
    def sortEmpTripsForWeek(self, data, start_date, ssn):
        ''' This checks if a certain employee is working that week '''
        ret_list = []
        all_week_trips = self.weekSorter(data, start_date)
        for item in all_week_trips:
            if item['captain'] == ssn or item['copilot'] == ssn or item['fsm'] == ssn or item['fa1'] == ssn or item['fa2'] == ssn:
                ret_list.append(item)
        return ret_list
