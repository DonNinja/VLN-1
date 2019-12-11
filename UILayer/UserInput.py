from LogicLayer.UserInputCheck import UserInputCheck
from LogicLayer.Logic import LogicAPI


class UserInput:
    def __init__(self):
        pass
    
    def addEmp(self, emp_type):
        data_list = []
        print()
        ssn = input("Enter the new {}'s ssn: ".format(emp_type)).capitalize()
        while self.__checker.checkSSN(ssn) != True:
                ssn = input("Enter the new {}'s ssn: ".format(emp_type)).capitalize()
        data_list.append(ssn)

        name = input("Enter the new {}'s name: ".format(emp_type)).capitalize()
        while self.__checker.checkName(name) != True:
            name = input("Enter the new {}'s name: ".format(emp_type)).capitalize()
        data_list.append(name)
        role = emp_type.capitalize()
        data_list.append(role)
        if role == 'Pilot':
            rank_input = input("Enter {}'s rank, 1 for Captain, 2 for Copilot: ".format(emp_type)).capitalize()
            rank = self.__checker.checkRank(rank_input, role)
            while rank == False:
                rank_input = input("Enter {}'s rank, 1 for Captain, 2 for Copilot: ".format(emp_type)).capitalize()
                rank = self.__checker.checkRank(rank_input, role)
            data_list.append(rank)
        if role == 'Flight attendant':
            rank_input = input("Enter {}'s rank, 1 for Flight attendant, 2 for Flight Service Manager: ".format(emp_type)).capitalize()
            rank = self.__checker.checkRank(rank_input, role)
            while rank == False:
               rank_input = input("Enter {}'s rank, 1 for Flight attendant, 2 for Flight Service Manager: ".format(emp_type)).capitalize()
               rank = self.__checker.checkRank(rank_input, role)
            data_list.append(rank)
        if emp_type != "flight attendant":
            licens_input = input("Enter {}'s license, 1 for NAFokkerF100, 2 for NAFokkerF28, 3 for NABAE146: ".format(emp_type)).capitalize()
            licens = self.__checker.checkLicense(licens_input)
            while licens == False:
                licens_input = input("Enter {}'s license, 1 for NAFokkerF100, 2 for NAFokkerF28, 3 for NABAE146: ".format(emp_type)).capitalize()
                licens = self.__checker.checkLicense(licens_input)
            data_list.append(licens)
        else:
            licens = "N/A"
        address = input("Enter the new {}'s address: ".format(emp_type)).capitalize()
        while self.__checker.checkAddress(address) != True:
            address = input("Enter the new {}'s address: ".format(emp_type)).capitalize()
        data_list.append(address)
        mobile = input("Enter the new {}'s mobile number: ".format(emp_type)).capitalize()
        while self.__checker.checkPhone(mobile) != True:
            mobile = input("Enter the new {}'s mobile number: ".format(emp_type)).capitalize()
        data_list.append(mobile)
        home_phone = input("Enter the new {}'s home phone number: ".format(emp_type)).capitalize()
        while self.__checker.checkPhone(home_phone) != True:
            home_phone = input("Enter the new {}'s home phone number: ".format(emp_type)).capitalize()
        data_list.append(home_phone)
    
        self.__insert.addEmpLL(data_list)
        
        print(data_list)
        input("Press enter to continue...")
        return data_list
    
    def addLocation(self):
        loc_data_list = []
        loc_country = input("Enter the new location's country: ").capitalize()
        loc_data_list.append(loc_country)
        loc_airport_name = input("Enter the new location's aiport's name: ").capitalize()
        loc_data_list.append(loc_airport_name)
        loc_flight_time_hours = input("Enter the new location's flight time (Hours): ")
        loc_flight_time_mins = input("Enter the new location's flight time (Minutes): ")
        loc_flight_time = "{}:{}:00".format(loc_flight_time_hours, loc_flight_time_mins)
        loc_data_list.append(loc_flight_time)
        loc_distance = input("Enter the distance from Iceland (Kilometers): ")
        loc_data_list.append(loc_distance)
        loc_contact_name = input("Enter the new location's contact's name: ")
        loc_data_list.append(loc_contact_name)
        loc_emer_num = input("Enter the new location's emergency phone number: ")
        loc_data_list.append(loc_emer_num)
        print(loc_data_list)
        input("Press enter to continue...")
        return loc_data_list

    def enterSSN(self, emp_type):
        ssn = input("Enter a{}'s SSN: ".format(emp_type))
        #Check hvort að kennitalan tilheyri einhverjum starfsmanni
        return ssn
    
    def addWorkTrip(self):
        work_trip_data_list = []
        work_destination = input("Enter a destination: ")
        work_trip_data_list.append(work_destination)
        work_departure_date = input("Enter a departure date (DD/MM/YYYY): ")
        work_trip_data_list.append(work_departure_date)
        work_departure_time = input("Enter a departure time (hh:mm): ")
        work_trip_data_list.append(work_departure_time)
        work_pilot_ssn = input("Enter the Pilot's SSN: ")
        work_trip_data_list.append(work_pilot_ssn)
        work_copilot_ssn = input("Enter the Co-Pilot's SSN: ")
        work_trip_data_list.append(work_copilot_ssn)
        more_pilots = input("Would you like to enter more pilots? (Y/N): ").upper()
        while more_pilots == "Y":
            work_extra_pilot_ssn = input("Enter another pilot's SSN")
            work_trip_data_list.append(work_extra_pilot_ssn)
            more_pilots = input("Would you like to enter more pilots? (Y/N): ").upper()
        work_attendant = input("Enter a flight attendant's SSN: ")
        work_trip_data_list.append(work_attendant)
        more_attendants = input("Would you like to enter more flight attendants? (Y/N): ").upper()
        while more_attendants == "Y":
            work_extra_attendant_ssn = input("Enter another flight attendant's SSN: ")
            more_attendants = input("Would you like to enter more flight attendants? (Y/N): ").upper()
            work_trip_data_list.append(work_extra_attendant_ssn)
        print(work_trip_data_list)
        input("Press enter to continue...")
        return work_trip_data_list

    def addPlane(self):
        plane_data_list = []
        print()
        choose = input("choose 1 = FokkerF100 2 =AFokkerF28 3 = BAE146")
        planedict = {"1":"NAFokkerF100","2":"NAFokkerF28","3":"NABAE146"}
        planeid = planedict[choose]
        plane_data_list.append(planeid)

        planeinsignia = input("Enter plane Insignia: ")
        #if __checker.planeinsignia(planeinsignia)
        plane_data_list.append(planeinsignia)

        print(plane_data_list)
        return plane_data_list

    def enterEmail(self):
        return input("Enter a new email: ")
    
    def enterAddress(self):
        return input("Enter a new address: ")
