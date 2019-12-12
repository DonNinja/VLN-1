from LogicLayer.Logic import LogicAPI
from UILayer.UserInput import UserInput
from UILayer.UIDataPrinter import UIDataPrinter
from UILayer.UIPrinter import UIPrinter

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
    
    def showAllAttendants(self):
        """ This gets a list of every flight attendant from logicAPI, then calls the printer to print out every flight attendant for the user """
        data_list = self.__logic.showAllAttendants()
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
        new_var = self.__inputter.enterVariable('email')
        email = self.__logic.checkEmail(new_var)
        while not(email):
            new_var = self.__inputter.enterVariable('email')
            email = self.__logic.checkEmail(new_var)
        else:
            self.__logic.updateEmp(data, new_var, 'email')
            self.showSpecificEmp(data['ssn'])

    def editAddress(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('address')
        address = self.__logic.checkAddress(new_var)
        while not(address):
            new_var = self.__inputter.enterVariable('address')
            address = self.__logic.checkAddress(new_var)
        else:
            self.__logic.updateEmp(data, address, 'address')
            self.showSpecificEmp(data['ssn'])
    
    def editHomePhone(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('home phone number')
        phone_check = self.__logic.checkPhone(new_var)
        while not(phone_check):
            new_var = self.__inputter.enterVariable('home phone number')
            phone_check = self.__logic.checkPhone(new_var)
        else:
            self.__logic.updateEmp(data, new_var, 'homephonenumber')
            self.showSpecificEmp(data['ssn'])
    
    def editMobilePhone(self, data):
        """ This calls the __inputter and calls __logic to update the file, then calls a function to show the updated employee """
        new_var = self.__inputter.enterVariable('mobile phone number')
        phone_check = self.__logic.checkPhone(new_var)
        while not(phone_check):
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
        while not (rank):
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
            return email

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
        """ This calls the inputter so the user can input the work trips's data, then calls logicAPI to add both flights to the flight.csv file """
        data_list = self.__inputter.addWorkTrip()
        self.__logic.addWorkTrip(data_list)

        

    def addLocation(self):
        pass

    
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


    def editFlightAircraftID(self, data):
        new_var = self.__inputter.enterVariable('Flight Aircraft ID')
        self.__logic.updateFlightAircraftID(data, new_var, 'aircraftID')
        self.showSpecificWorktrip(data['flight number'])
        

    def editFlightCaptain(self, data):
        new_var = self.__inputter.enterVariable('Flight Captain')
        blabla = self.__logic.updateFlightCaptain(data, new_var, 'captain')
        self.showSpecificWorktrip(data['flight number'])

    def editFlightCopilot():
        pass

    def editFlightFSM():
        pass

    def editFlightFA():
        pass

    def showSpecificWorktrip(self, flight_num):
        flight_list = self.__logic.showSpecificWorktrip(flightnumber)
        self.__data_printer.printWorkTrip(flight_list)
        