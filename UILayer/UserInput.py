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
        return input("\nEnter the new location's airport's id (3 letters, ex.: Keflavik = KEF): ").upper()

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
        ssn = input("\nEnter a{}'s SSN: ".format(emp_type))
        #Check hvort að kennitalan tilheyri einhverjum starfsmanni
        return ssn

    def addTripDest(self):
        return input("\nEnter trip destination id (Not KEF) 'HELP' to show all destinations: ").upper()
    
    def addTripDepTime(self):
        print("\nNow entering a departure time and date:")
        while True:
            work_dep_day = input("\nEnter a day (dd): ").zfill(2)
            work_dep_month = input("Enter a month (mm): ").zfill(2)
            work_dep_year = input("Enter a year (yyyy): ")
            work_dep_hour = input("Enter an hour (HH): ")
            work_dep_min = input("Enter minutes (MM): ")
            work_dep_sec = "00"
            work_departure_time = "{}-{}-{} {}:{}:{}".format(work_dep_year, work_dep_month, work_dep_day, work_dep_hour, work_dep_min, work_dep_sec)
            try:
                work_date = datetime.datetime.strptime(work_departure_time, '%Y-%m-%d %H:%M:%S')
                return work_date
            except:
                print("There was something wrong with your input, please try again")
    
    def addTripPlaneID(self):
        return input("\nEnter plane insignia (3 letters) (Keep empty if you don't want to enter one) 'HELP' to show all planes: TF-").upper()
    
    def addTripCaptain(self):
        return input("\nEnter the Captain's SSN (Keep empty if you don't want to enter one) 'HELP' to show all captains: ")
    
    def addTripCopilot(self):
        return input("\nEnter the Co-Pilot's SSN (Keep empty if you don't want to enter one) 'HELP' to show all copilots: ")
    
    def addTripFSM(self):
        return input("\nEnter a flight service manager's SSN (Keep empty if you don't want to enter one) 'HELP' to show all flight service managers: ")
    
    def addTripFA(self):
        return input("\nEnter a flight attendant's SSN (Keep empty if you don't want to enter one): ")

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

        planeinsignia = input("\nEnter plane Insignia (3 letters): TF-").upper()
        #if __checker.planeinsignia(planeinsignia)
        planeinsignia = "TF-" + planeinsignia
        plane_data_list.append(planeinsignia)
        return plane_data_list

    def enterVariable(self, to_enter):
        return input("\nEnter a new {}: ".format(to_enter))
    
    def enterEditTripPlaneID(self):
        return input("\nEnter plane insignia (3 letters) 'HELP' to show all planes: TF-").upper()
    
    def enterEditTripCaptain(self):
        return input("\nEnter the Captain's SSN ('HELP' to show all captains): ")
    
    def enterEditTripCopilot(self):
        return input("\nEnter the Co-Pilot's SSN ('HELP' to show all copilots): ")
    
    def enterEditTripFSM(self):
        return input("\nEnter a flight service manager's SSN ('HELP' to show all flight service managers): ")
    
    def enterEditTripFA(self):
        return input("\nEnter a flight attendant's SSN ('HELP' to show all flight attendants): ")

    def enterEmail(self):
        return input("\nEnter a new email (@NaNAir.is will be added to it): ")

    def askForDate(self):
        '''Asking for a specific date to show work trips by day'''
        day = input("\nEnter day (DD): ")
        month = input("\nEnter month (MM): ")
        year = input("\nEnter year (YYYY): ")
        date = year + "-" + month + "-" + day
        return date


    def askForLocID(self):
        return input("\nEnter a location's ID (ex.: KEF): ").upper()
