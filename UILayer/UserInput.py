import datetime

class UserInput:
    def __init__(self):
        pass
    
    def addEmpSSN(self, emp_type):
        print()
        return input("\nEnter the new {}'s ssn: ".format(emp_type)).capitalize()

    def addEmpName(self, emp_type):
        return input("\nEnter {} first and last name (Non-Icelandic characters): ".format(emp_type))

    def addEmpRank(self, emp_type):
        if emp_type == "Pilot":
            print("\n1: Captain\n2: Copilot")
            return input("\nChoose a rank: ")
        else:
            print("\n1: Flight Service Manager\n2: Flight Attendant")
            return input("\nChoose a rank: ")
                

    def addEmpEmail(self, emp_type):
        return input("\nEnter {}'s email address (@NaNAir.com will be added to it): ".format(emp_type))

    def addEmpLicens(self, emp_type):          
        if emp_type != "Cabincrew":
            print("\n1: FokkerF100\n2: FokkerF28\n3: BAE146")
            choice = input("\nChoose a plane type: ")
            return choice
        else:
            return "N/A"

    def addEmpAddress(self, emp_type):
        return input("\nEnter the new {}'s address (Non-Icelandic characters): ".format(emp_type)).capitalize()

    def addEmpMobile(self, emp_type):
        return input("\nEnter the new {}'s mobile number (7 digits): ".format(emp_type)).capitalize()
    
    def addHomePhone(self, emp_type):
        return input("\nEnter the new {}'s home phone number (7 digits): ".format(emp_type)).capitalize()
    
    def addLocCountry(self):
        return input("\nEnter the new location's country (Non-Icelandic characters): ").capitalize()
    
    def addLocCountryAbbrev(self):
        return input("\nEnter the new location's country's abbreviation (ex.: Iceland = ICE): ").upper()

    def addLocName(self):
        return input("\nEnter the new location's internal name (Non-Icelandic characters): ").capitalize()

    def addLocAirport(self):
        return input("\nEnter the new location's aiport's name (Non-Icelandic characters): ").capitalize()
        
    def addLocFlightTimeHour(self):
        return input("\nEnter the new location's flight time (Hours): ")
    
    def addLocFlightTimeMin(self):
        return input("\nEnter the new location's flight time (Minutes): ")

    def addLocDist(self):
        return input("\nEnter the distance from Iceland (est. kilometers): ")

    def addLocContactName(self):
        return input("\nEnter the new location's contact's name (Non-Icelandic characters): ")
    
    def addLocContactNum(self):
        return input("\nEnter the new location's emergency phone number (Non-Icelandic characters): ")

    def enterSSN(self, emp_type):
        print("hæ")
        ssn = input("\nEnter a{}'s SSN: ".format(emp_type))
        #Check hvort að kennitalan tilheyri einhverjum starfsmanni
        return ssn

    
    def addWorkTrip(self):
        work_trip_data_list = []
        work_destination = input("\nDeparting from: ")
        work_trip_data_list.append(work_destination)
        work_departure_date = input("\nArriving at: ")
        if work_departure_date == "LYR":
            flight_time = datetime.timedelta(hours=2,minutes=53)
        elif work_departure_date == "GOH":
            flight_time = datetime.timedelta(hours=2,minutes=9)
        elif work_departure_date == "KUS":
            flight_time = datetime.timedelta(hours=1,minutes=20)
        elif work_departure_date == "FAE":
            flight_time = datetime.timedelta(hours=1,minutes=26)
        elif work_departure_date == "LWK":
            flight_time = datetime.timedelta(hours=1,minutes=53)
        else:
            print("invalid")

        work_trip_data_list.append(work_departure_date)
        work_departure_time = input("\nEnter a departure time (YYYY-MM-DD HH:MM:SS): ")
        dep_time_obj = datetime.datetime.strptime(work_departure_time, '%Y-%m-%d %H:%M:%S')
        work_trip_data_list.append(dep_time_obj)
        

        work_arrival_time = dep_time_obj
        arr_time_obj = work_arrival_time + flight_time
        work_trip_data_list.append(arr_time_obj)

        planeID = input("\nEnter planeID: ")
        work_trip_data_list.append(planeID)

        work_pilot_ssn = input("\nEnter the Pilot's SSN: ")
        work_trip_data_list.append(work_pilot_ssn)
        work_copilot_ssn = input("\nEnter the Co-Pilot's SSN: ")
        work_trip_data_list.append(work_copilot_ssn)

        work_attendant = input("\nEnter a flight attendant's SSN: ")
        work_trip_data_list.append(work_attendant)
        work_trip_data_list.append(flight_time)
        print(work_trip_data_list)
        input("\nPress enter to continue...")

        return work_trip_data_list

    def addPlane(self):
        plane_data_list = []
        while True:
            print("\n1: FokkerF100\n2: FokkerF28\n3: BAE146")
            choice = input("\nChoose a plane type: ")
            planedict = {"1":"NAFokkerF100","2":"NAFokkerF28","3":"NABAE146"}
            try:
                plane_type = planedict[choice]
                break
            except:
                print("Input invalid")
        plane_data_list.append(plane_type)

        planeinsignia = input("\nEnter plane Insignia (3 letters): ")
        #if __checker.planeinsignia(planeinsignia)
        planeinsignia = "TF-" + planeinsignia
        plane_data_list.append(planeinsignia)
        return plane_data_list

    def enterVariable(self, to_enter):
        return input("Enter a new {}: ".format(to_enter))

    def editemp(self,pilot_list,emp_type):
        edit_emp_list = []
        print()
        ssn = pilot_list[0]
        #if __checker.checkSSN(ssn):
        edit_emp_list.append(ssn)
        name = input("Enter the new {}'s name: ".format(emp_type)).capitalize()
        # self.__checker.checkName(name)
        edit_emp_list.append(name)
        role = emp_type.capitalize()
        #if __checker.checkRole(role)
        edit_emp_list.append(role)
        rank = input("Enter the new {}'s rank: ".format(emp_type)).capitalize()
        #if __checker.checkRank(rank)
        edit_emp_list.append(rank)
        if emp_type != "flight attendant":
            licens = input("Enter the new {}'s license: ".format(emp_type)).capitalize()
            #if __checker.checkLicense(licens)
            edit_emp_list.append(licens)
        else:
            licens = "N/A"
        address = input("Enter the new {}'s address: ".format(emp_type)).capitalize()
        #if __checker.checkAddress(address)
        edit_emp_list.append(address)
        mobile = input("Enter the new {}'s mobile number: ".format(emp_type)).capitalize()
        #if __checker.checkMobile(mobile)
        edit_emp_list.append(mobile)
        home_phone = input("Enter the new {}'s home phone number: ".format(emp_type)).capitalize()
        #if __checker.checkHomePhone(home_phone)
        edit_emp_list.append(home_phone)
        print(edit_emp_list)
        input("Press enter to continue...")
        return edit_emp_list
        
    def askForDate(self):
        '''Asking for a specific date to show work trips by day'''
        day = input("Enter day (DD): ")
        month = input("Enter month (MM): ")
        year = input("Enter year (YYYY): ")
        date = year + "-" + month + "-" + day
        return date
