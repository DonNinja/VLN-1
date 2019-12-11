
class UserInput:
    def __init__(self):
        pass
    
    def addEmpSSN(self, emp_type):
        print()
        return input("Enter the new {}'s ssn: ".format(emp_type)).capitalize()

    def addEmpName(self, emp_type):
        return input("Enter {} first and last name (Non-Icelandic characters): ".format(emp_type))

    def addEmpRank(self, emp_type):
        if emp_type == "Pilot":
            print("\n1: Captain\n2: Copilot")
            return input("\nChoose a rank: ")
        else:
            print("\n1: Flight Service Manager\n2: Flight Attendant")
            return input("\nChoose a rank: ")
                

    def addEmpEmail(self, emp_type):
        return input("Enter {}'s email address (@NaNAir.com will be added to it): ".format(emp_type))

    def addEmpLicens(self, emp_type):          
        if emp_type != "Cabincrew":
            print("\n1: FokkerF100\n2: FokkerF28\n3: BAE146")
            return input("\nChoose a plane license: ")
        else:
            return "N/A"

    def addEmpAddress(self, emp_type):
        return input("Enter the new {}'s address (Non-Icelandic characters): ".format(emp_type)).capitalize()

    def addEmpMobile(self, emp_type):
        return input("Enter the new {}'s mobile number (7 digits): ".format(emp_type)).capitalize()
    
    def addHomePhone(self, emp_type):
        return input("Enter the new {}'s home phone number (7 digits): ".format(emp_type)).capitalize()
    
    def addLocationCountry(self):
        loc_data_list = []
        loc_country = input("\nEnter the new location's country: ").capitalize()
        loc_data_list.append(loc_country)
        loc_airport_name = input("\nEnter the new location's aiport's name: ").capitalize()
        loc_data_list.append(loc_airport_name)
        loc_flight_time_hours = input("\nEnter the new location's flight time (Hours): ")
        loc_flight_time_mins = input("\nEnter the new location's flight time (Minutes): ")
        loc_flight_time = '.'.join(loc_flight_time_hours, loc_flight_time_mins)
        loc_data_list.append(loc_flight_time)
        loc_distance = input("\nEnter the distance from Iceland (Kilometers): ")
        loc_data_list.append(loc_distance)
        loc_contact_name = input("\nEnter the new location's contact's name: ")
        loc_data_list.append(loc_contact_name)
        loc_emer_num = input("\nEnter the new location's emergency phone number: ")
        loc_data_list.append(loc_emer_num)
        input("\nPress enter to continue...")
        return loc_data_list

    def enterSSN(self, emp_type):
        ssn = input("\nEnter a{}'s SSN: ".format(emp_type))
        #Check hvort að kennitalan tilheyri einhverjum starfsmanni
        return ssn
    
    def addWorkTrip(self):
        work_trip_data_list = []
        work_destination = input("\nEnter a destination: ")
        work_trip_data_list.append(work_destination)

        work_departure_date = input("Enter a departure date (DD/MM/YYYY): ")
        work_trip_data_list.append(work_departure_date)
        work_departure_time = input("\nEnter a departure time (hh:mm): ")
        work_trip_data_list.append(work_departure_time)

        work_pilot_ssn = input("Enter the Pilot's SSN: ")
        work_trip_data_list.append(work_pilot_ssn)
        work_copilot_ssn = input("\nEnter the Co-Pilot's SSN: ")
        work_trip_data_list.append(work_copilot_ssn)
        more_pilots = input("Would you like to enter more pilots? (Y/N): ").upper()
        while more_pilots == "Y":
            work_extra_pilot_ssn = input("\nEnter another pilot's SSN")
            work_trip_data_list.append(work_extra_pilot_ssn)
            more_pilots = input("Would you like to enter more pilots? (Y/N): ").upper()
        work_attendant = input("\nEnter a flight attendant's SSN: ")
        work_trip_data_list.append(work_attendant)
        more_attendants = input("Would you like to enter more flight attendants? (Y/N): ").upper()
        while more_attendants == "Y":
            work_extra_attendant_ssn = input("\nEnter another flight attendant's SSN: ")
            more_attendants = input("Would you like to enter more flight attendants? (Y/N): ").upper()
            work_trip_data_list.append(work_extra_attendant_ssn)
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
        



