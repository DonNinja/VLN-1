from LogicLayer.Logic import LogicAPI
from UILayer.UserInput import UserInput
from UILayer.UIDataPrinter import UIDataPrinter
from UILayer.UIPrinter import UIPrinter
import dateutil

class UIAPI:
    def __init__(self):
        self.__logic = LogicAPI()
        self.__inputter = UserInput()
        self.__data_printer = UIDataPrinter()
        self.__ui_printer = UIPrinter()

    def UIDisplay(self, choice_list):
        """ This calls the printer to print out the current screen for the user """
        self.__ui_printer.display(choice_list)
    
    def UIHeaderDisplay(self, title):
        """ This calls the printer to print out the header for the current screen """
        self.__ui_printer.headerDisplay(title)
    
    def addPlane(self):
        """ This calls the __inputter so the user can input the plane's data, then calls logicAPI to add it to the file """
        data_list = self.__inputter.addPlane()
        self.__logic.addPlane(data_list)
    
    def showAllEmps(self):
        """ This gets a list of every employee from logicAPI, then calls the printer to print out every employee for the user """
        data_list = self.__logic.showAllEmps()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllPilots(self):
        """ This gets a list of every pilot from logicAPI, then calls the printer to print out every pilot for the user """
        data_list = self.__logic.showAllPilots()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllCaptains(self):
        ''' This gets a list of every captain from logicAPI, then calls the printer to print them out for the user '''
        data_list = self.__logic.showAllCaptains()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllCopilots(self):
        ''' This gets a list of every copilot from logicAPI, then calls the printer to print them out for the user '''
        data_list = self.__logic.showAllCopilots()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllAttendants(self):
        """ This gets a list of every flight attendant from logicAPI, then calls the printer to print out every flight attendant for the user """
        data_list = self.__logic.showAllAttendants()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllFSM(self):
        ''' This gets a list of every flight service manager from logicAPI, then calls the printer to print them out for the user '''
        data_list = self.__logic.showAllFSM()
        self.__data_printer.printAllEmps(data_list)
    
    def showAllPlanes(self):
        """ This gets a list of every plane from logicAPI, then calls the printer to print out every plane for the user """
        data_list = self.__logic.showAllPlanes()
        self.__data_printer.printAllPlanes(data_list)
    
    def showPilotsForPlane(self, plane_type):
        """ This gets a list of every pilot with a license for the plane type from logicAPI, then calls the printer to print them out """
        data_list = self.__logic.showPilotByPlane(plane_type)
        self.__data_printer.printPilotForPlane(data_list)
    
    def showSpecificEmp(self, ssn):
        """ This gets a single employee with the inputted SSN and calls the pirnter to print them out """
        emp = self.__logic.showEmpSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp
    
    def showSpecificTrip(self, flight_num):
        flight_num_check = self.__logic.checkFlightNum(flight_num)
        while not(flight_num_check):
            print("Flight number must be 4 digits")
            flight_num = input("Enter a flight number (4 digits): ")
            flight_num_check = self.__logic.checkFlightNum(flight_num)
        dep_flight_num = "NA" + flight_num
        ret_flight_num = "NA" + str(int(flight_num) + 1).zfill(4)
        flight_num_list = [dep_flight_num, ret_flight_num]
        trip_list = self.__logic.sortTrips(flight_num_list)
        if len(trip_list) > 0:
            self.__data_printer.printAllWorkTrips(trip_list)
            return True
        else:
            print("There are no trips with that Flight number.")
            return False

    def showSpecificPilot(self, ssn):
        """ This gets a single pilot and calls the printer to print them out """
        emp = self.__logic.showPilotSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp

    def showSpecificAttendant(self, ssn):
        """ This gets a single attendant and calls the printer to print them out """
        emp = self.__logic.showAttendantSSN(ssn)
        return self.__data_printer.printEmpSSN(emp), emp
    
    def showAllLocations(self):
        data_list = self.__logic.showAllLocations()
        self.__data_printer.printLocations(data_list)

    def editEmail(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_email = self.__inputter.enterEmail()
        email_check, error_msg = self.__logic.checkEmail(new_email)
        while not(email_check):
            print(error_msg)
            new_email = self.__inputter.enterEmail()
            email_check, error_msg = self.__logic.checkEmail(new_email)
        else:
            new_email += "@NaNAir.is"
            self.__logic.updateEmp(data, new_email, 'email')
            self.showSpecificEmp(data['ssn'])

    def editAddress(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('address')
        address, error_msg = self.__logic.checkAddress(new_var)
        while not(address):
            print(error_msg)
            new_var = self.__inputter.enterVariable('address')
            address = self.__logic.checkAddress(new_var)
        else:
            self.__logic.updateEmp(data, address, 'address')
            self.showSpecificEmp(data['ssn'])
    
    def editHomePhone(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('home phone number')
        phone_check, error_msg = self.__logic.checkPhone(new_var)
        while not(phone_check):
            print(error_msg)
            new_var = self.__inputter.enterVariable('home phone number')
            phone_check = self.__logic.checkPhone(new_var)
        else:
            self.__logic.updateEmp(data, new_var, 'homephonenumber')
            self.showSpecificEmp(data['ssn'])
    
    def editMobilePhone(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('mobile phone number')
        phone_check, error_msg = self.__logic.checkPhone(new_var)
        while not(phone_check):
            print(error_msg)
            new_var = self.__inputter.enterVariable('mobile phone number')
            phone_check = self.__logic.checkPhone(new_var)
        else:
            self.__logic.updateEmp(data, new_var, 'mobilephonenumber')
            self.showSpecificEmp(data['ssn'])
    
    def editLicense(self, data):
        new_var = self.__inputter.addEmpLicens('plane license')
        licens = self.__logic.checkLicens(new_var)
        while not(licens):
            new_var = self.__inputter.addEmpLicens('plane license')
            licens = self.__logic.checkLicens(new_var)
        else:
            self.__logic.updateEmp(data, licens, 'licence')
            self.showSpecificEmp(data['ssn'])
    
    def addEmp(self, role):
        """ This add all items to list after they pass checks """
        data_list = []
        data_list.append(self.checkSSN(role))
        data_list.append(self.checkName(role))
        data_list.append(self.checkRole(role))
        data_list.append(self.checkRank(role))
        data_list.append(self.checkEmail(role))
        data_list.append(self.checkLicens(role))
        data_list.append(self.checkAddress(role))
        data_list.append(self.checkMobile(role))
        data_list.append(self.checkHomenum(role))
        self.__logic.addEmpLL(data_list) #List with all of the employee info

    def checkSSN(self, emp_type): #Virkar
        """ This checks if SSN is in valid format """
        data = self.__logic.showAllEmps()
        ssn = self.__inputter.addEmpSSN(emp_type)
        ssn_check, error_list = self.__logic.checkSSN(ssn, data)
        while not(ssn_check):
            for error in error_list:
                print(error)
            ssn = self.__inputter.addEmpSSN(emp_type)
            ssn_check, error_list = self.__logic.checkSSN(ssn, data)
        else:
            return ssn

    def checkName(self, emp_type): #Virkar semi
        """ This checks if name is in valid format (first and last name), also capitilizes first letters in seperate names """
        name_input = self.__inputter.addEmpName(emp_type)
        name, error_msg = self.__logic.checkName(name_input)
        while not (name):
            print(error_msg)
            name_input = self.__inputter.addEmpName(emp_type)
            name, error_msg = self.__logic.checkName(name_input)
        else:
            return name

    def checkRole(self, emp_type):
        """ This adds employ type to the list cabincrew/pilot (already been selcted through employee screen) """
        return emp_type

    def checkRank(self, emp_type): #Virkar
        """ This checks if employee rank is valid and returs valid rank """
        rank_input = self.__inputter.addEmpRank(emp_type)
        rank = self.__logic.checkRank(rank_input, emp_type)
        while not(rank):
            print("Invalid choice")
            rank_input = self.__inputter.addEmpRank(emp_type)
            rank = self.__logic.checkRank(rank_input, emp_type)
        else:
            return rank

    def checkEmail(self, emp_type):
        """ This checks if email is in valid format """
        email_input = self.__inputter.addEmpEmail(emp_type)
        email, error_msg = self.__logic.checkEmail(email_input)
        while not(email):
            print(error_msg)
            email_input = self.__inputter.addEmpEmail(emp_type)
            email, error_msg = self.__logic.checkEmail(email_input)
        else:
            return email_input

    def checkLicens(self,emp_type): #Virkar
        """ This checks if licens is valid and returns right licens"""
        licens_input = self.__inputter.addEmpLicens(emp_type)
        licens = self.__logic.checkLicens(licens_input)
        while not(licens):
            print("Invalid choice")
            licens_input = self.__inputter.addEmpLicens(emp_type)
            licens = self.__logic.checkLicens(licens_input)
        else:
            return licens

    def checkAddress(self, emp_type): #Virkar 
        """ This checks if address is valid and returns it in the right format if street name is not capitalized """
        address_input = self.__inputter.addEmpAddress(emp_type)
        address, error_msg = self.__logic.checkAddress(address_input)
        while not(address):
            print(error_msg)
            address_input = self.__inputter.addEmpAddress(emp_type)
            address, error_msg = self.__logic.checkAddress(address_input)
        else:
            return address

    def checkMobile(self, emp_type): # Virkar
        """ This checks if number is only digit and length of 7 """
        mobile = self.__inputter.addEmpMobile(emp_type)
        phone_check, error_msg = self.__logic.checkPhone(mobile)
        while not(phone_check):
            print(error_msg)
            mobile = self.__inputter.addEmpMobile(emp_type)
            phone_check, error_msg = self.__logic.checkPhone(mobile)
        else:
            return mobile

    def checkHomenum(self,emp_type): # Virkar
        """ This checks if number is only digit and length of 7 """
        home_phone_num = self.__inputter.addHomePhone(emp_type)
        phone_check, error_msg = self.__logic.checkPhone(home_phone_num)
        while not(phone_check):
            print(error_msg)
            home_phone_num = self.__inputter.addHomePhone(emp_type)
            phone_check, error_msg = self.__logic.checkPhone(home_phone_num)
        else:
            return home_phone_num

    def showAllWorkTrips(self):
        """ This gets a list of every flight from logicAPI, then calls the printer to print it out for the user """
        data_list = self.__logic.showAllWorkTrips()
        self.__data_printer.printAllWorkTrips(data_list)
    
    def addWorkTrip(self):
        """ This calls the inputter so the user can input the work trip's data, then calls logicAPI to add both flights to the flight.csv file """
        data_list = []
        trip_dep_loc = "KEF" # The departure flight is always from KEF

        while True:
            trip_arr_loc = self.__inputter.addTripDest() # calls the inputter for the destination
            if trip_arr_loc.upper() == "HELP":
                self.showAllLocations()
            else:
                if self.__logic.checkLocID(trip_arr_loc):
                    break
                else:
                    print("\nLocation does not exist or is written incorrectly, also can't be KEF")

        trip_dep_time = self.__inputter.addTripDepTime()
        trip_dep_date = trip_dep_time.date()
        trip_arr_time = self.__logic.calcFlightTime(trip_dep_time, trip_arr_loc)

        while True:
            trip_plane_id = self.__inputter.addTripPlaneID() # Can be empty
            if trip_plane_id.upper() == "HELP":
                self.showAllPlanes()
            else:
                if self.__logic.checkIfEmpty(trip_plane_id):
                    trip_plane_id = "X"
                    break
                else:
                    trip_plane_id = "TF-" + trip_plane_id
                    if self.__logic.checkIfPlane(trip_plane_id):
                        if not(self.__logic.checkIfIsWorking(trip_plane_id, trip_dep_date)):
                            break
                        else:
                            print("Plane is being used on that day")
                    else:
                        print("That is not a correct plane insignia")

        while True:
            trip_captain = self.__inputter.addTripCaptain() # Can be empty
            if trip_captain.upper() == "HELP":
                self.showAllCaptains()
            else:
                if self.__logic.checkIfEmpty(trip_captain):
                    trip_captain = "X"
                    break
                if self.__logic.checkIfCaptain(trip_captain):
                    if self.__logic.checkIfMayFly(trip_captain, trip_plane_id):
                        if not(self.__logic.checkIfIsWorking(trip_captain, trip_dep_date)):
                            break
                        else:
                            print("Employee is working on that day")
                    else:
                        print("This pilot may not fly a {}".format(trip_plane_id))
                else:
                    print("That is not a correct captain's ssn")

        while True:
            trip_copilot = self.__inputter.addTripCopilot() # Can be empty
            if trip_copilot.upper() == "HELP":
                self.showAllCopilots()
            else:
                if self.__logic.checkIfEmpty(trip_copilot):
                    trip_copilot = "X"
                    break
                if self.__logic.checkIfCopilot(trip_copilot):
                    if self.__logic.checkIfMayFly(trip_copilot, trip_plane_id):
                        if not(self.__logic.checkIfIsWorking(trip_copilot, trip_dep_date)):
                            break
                        else:
                            print("Employee is working on that day")
                    else:
                        print("This pilot may not fly a {}".format(trip_plane_id))
                else:
                    print("That is not a correct copilot's ssn")
            


        while True:
            trip_fsm = self.__inputter.addTripFSM() # Can be empty
            if trip_fsm.upper() == "HELP":
                self.showAllFSM()
            else:
                if self.__logic.checkIfEmpty(trip_fsm):
                    trip_fsm = "X"
                    break
                if self.__logic.checkIfFSM(trip_fsm):
                    if not(self.__logic.checkIfIsWorking(trip_fsm, trip_dep_date)):
                        break
                    else:
                        print("Employee is working on that day")
                else:
                    print("That is not a correct flight service manager's ssn")
            
        data_list = [trip_dep_loc, trip_arr_loc, trip_dep_time, trip_arr_time, trip_plane_id, trip_captain, trip_copilot, trip_fsm] # 0 - 7
        for i in range(2):
            add_more = input("\nWould you like to enter more flight attendants ('Y' if yes): ").upper()
            if add_more == "Y":
                while True:
                    trip_fa = self.__inputter.addTripFA()
                    if trip_fa.upper() == "HELP":
                        self.showAllAttendants()
                    else:
                        if self.__logic.checkIfEmpty(trip_fa):
                            trip_fa = "X"
                            break
                        if self.__logic.checkIfFA(trip_fa):
                            if not(self.__logic.checkIfIsWorking(trip_fa, trip_dep_date)):
                                break
                            else:
                                print("Employee is working on that day")
                        else:
                            print("That is not a correct flight attendant's ssn")
                data_list.append(trip_fa) # 8 & 9
            else:
                trip_fa = "X"
                if i == 0:
                    data_list.append(trip_fa) # Can be empty 8
                    data_list.append(trip_fa) # Can be empty 9
                    break
                else:
                    data_list.append(trip_fa) # Can be empty 9
                    break
        
        ret_trip = self.__logic.calcTurnAroundTime(trip_arr_time) # This just adds 1 hour to the return trip after landing
        data_list.append(ret_trip) # 10
        ret_flight_time = self.__logic.calcFlightTime(ret_trip, trip_arr_loc) # This calculates the time it takes to fly from A to B by looking at the csv file
        data_list.append(ret_flight_time) # 11
        flight_fully_manned = self.__logic.checkAddIfFullyManned(trip_plane_id, trip_captain, trip_copilot, trip_fsm) # This does a check and sees if it's fully manned
        data_list.append(flight_fully_manned) # 12
        self.__logic.addWorkTrip(data_list)

    def addLocation(self):
        loc_name = self.__inputter.addLocName()
        country = self.__inputter.addLocCountry()
        loc_id = self.__inputter.addLocCountryAbbrev()
        airport = self.__inputter.addLocAirport()
        flight_time_hours = self.__inputter.addLocFlightTimeHour()
        flight_time_mins = self.__inputter.addLocFlightTimeMin()
        flight_time = '.'.join([flight_time_hours, flight_time_mins])
        distance = self.__inputter.addLocDist()
        contact_name = self.__inputter.addLocContactName()
        contact_phone = self.__inputter.addLocContactNum()
        data_list = [loc_id, loc_name, country, airport, flight_time, distance, contact_name, contact_phone]
        self.__logic.addLocation(data_list)
    
    def checkLocID(self):
        loc_id = self.__inputter.askForLocID()
        loc_data = self.__logic.showLocationID(loc_id)
        return self.__logic.checkLocID(loc_id), loc_id
    
    def showSpecificLocation(self, loc_id):
        data = self.__logic.showLocationID(loc_id)
        self.__data_printer.printSingleLocation(data)

    def editLocContPhone(self, loc_id):
        cont_phone = self.__inputter.enterVariable('contact phone')
        data = self.__logic.showLocationID(loc_id)
        phone_check, error_msg = self.__logic.checkPhone(cont_phone)
        while not(phone_check):
            print(error_msg)
            cont_phone = self.__inputter.enterVariable('contact phone')
            phone_check, error_msg = self.__logic.checkPhone(cont_phone)
        else:
            self.__logic.updateLocation(data, cont_phone, 'contactPhone')
            self.__data_printer.printSingleLocation(data) #show location by ID

    def editLocContName(self, loc_id):
        cont_name = self.__inputter.enterVariable('contact name')
        data = self.__logic.showLocationID(loc_id)
        name_check, error_msg = self.__logic.checkName(cont_name)
        while not(name_check):
            print(error_msg)
            cont_name = self.__inputter.enterVariable('contact name')
            name_check, error_msg = self.__logic.checkName(cont_name)
        else:
            self.__logic.updateLocation(data, cont_name, 'contactName')
            self.__data_printer.printSingleLocation(data) #show location by ID
    
    def showEmpsWorkTrips(self, ssn):
        ''' This calls a function print out work trips that are included in the data list '''
        data_list = self.__logic.showEmpsWorkTrips(ssn)
        self.__data_printer.printAllWorkTrips(data_list)

    def showWorkTripsByDay(self):
        '''Getting work trips by day '''
        date = self.__inputter.askForDate()
        data_list = self.__logic.showWorkTripsByDay(date)
        self.__data_printer.printAllWorkTrips(data_list)

    def showWorkTripsLastWeek(self):
        '''Getting work trips for last 7 days'''
        pass

    def checktripinp(self,data):
        # data = self.__logic.checktripinp(data)
        return data

    def showWorkTripsByWeek(self):
        date = self.__inputter.askForDate()
        data_list = self.__logic.showWorkTripsByWeek(date)
        self.__data_printer.printAllWorkTrips(data_list)

    def showSortPilotsByPlane(self):
        data_list = self.__logic.sortPilotByPlane()
        self.__data_printer.printAllEmps(data_list)


    def showempnotatwork(self):
        date = self.__inputter.askForDate()
        emp = self.__logic.showempnotworking(date)

        self.__data_printer.printempsnotworking(emp)


    def showempatwork(self):
        date = self.__inputter.askForDate()
        emp = self.__logic.showempatwork(date)
        self.__data_printer.printempsworking(emp)


    def editFlightAircraftID(self, data):
        aircraft_id = self.__inputter.enterVariable('Flight Aircraft ID')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, aircraft_id, 'aircraftID')
        self.showSpecificWorktrip(dep_flight['flightNumber'])

    def editFlightCaptain(self, data):
        flight_capt = self.__inputter.enterVariable('Flight Captain SSN')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, flight_capt, 'captain')
        self.showSpecificWorktrip(dep_flight['flightNumber'])

    def editFlightCopilot(self, data):
        flight_copilot = self.__inputter.enterVariable('Flight Copilot SSN')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, flight_copilot, 'copilot')
        self.showSpecificWorktrip(dep_flight['flightNumber'])

    def editFlightFSM(self, data):
        flight_fsm = self.__inputter.enterVariable('Flight Service Manager SSN')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, flight_fsm, 'fsm')
        self.showSpecificWorktrip(dep_flight['flightNumber'])
        
    def editFlightFA_1(self, data):
        flight_fa = self.__inputter.enterVariable('Flight Attendant SSN')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, flight_fa, 'fa1')
        self.showSpecificWorktrip(dep_flight['flightNumber'])

    def editFlightFA_2(self, data):
        flight_fa = self.__inputter.enterVariable('Flight Attendant SSN')
        flight_list = self.__logic.showSpecificWorktrip(data)
        dep_flight = flight_list[0]
        self.__logic.updateWorkTrip(flight_list, flight_fa, 'fa2')
        self.showSpecificWorktrip(dep_flight['flightNumber'])

    def showSpecificWorktrip(self, flight_num):
        flight_list = self.__logic.showSpecificWorktrip(flight_num)
        self.__data_printer.printAllWorkTrips(flight_list)
        
        # self.__data_printer.printAllEmps(data_list)
    
    def showEmpWeekTrips(self):
        ssn = self.__inputter.enterVariable('SSN')
        date = self.__inputter.askForDate()
        data_list = self.__logic.showEmpWeekTrips(ssn, date)
        self.__data_printer.printAllWorkTrips(data_list)
