from LogicLayer.UserInputCheck import UserInputCheck

class UserInput():
    def __init__(self):
        self.__checker = UserInputCheck()
    
    def addEmp(self, emp_type):
        data_list = []
        print()
        ssn = input("Enter the new {}'s ssn: ".format(emp_type)).capitalize()
        #if __checker.checkSSN(ssn):
        data_list.append(ssn)
        name = input("Enter the new {}'s name: ".format(emp_type)).capitalize()
        # self.__checker.checkName(name)
        data_list.append(name)
        role = emp_type.capitalize()
        #if __checker.checkRole(role)
        data_list.append(role)
        rank = input("Enter the new {}'s rank: ".format(emp_type)).capitalize()
        #if __checker.checkRank(rank)
        data_list.append(rank)
        if emp_type != "flight attendant":
            licens = input("Enter the new {}'s license: ".format(emp_type)).capitalize()
            #if __checker.checkLicense(licens)
            data_list.append(licens)
        else:
            licens = "N/A"
        address = input("Enter the new {}'s address: ".format(emp_type)).capitalize()
        #if __checker.checkAddress(address)
        data_list.append(address)
        mobile = input("Enter the new {}'s mobile number: ".format(emp_type)).capitalize()
        #if __checker.checkMobile(mobile)
        data_list.append(mobile)
        home_phone = input("Enter the new {}'s home phone number: ".format(emp_type)).capitalize()
        #if __checker.checkHomePhone(home_phone)
        data_list.append(home_phone)
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
        extra_pilot_list = []
        input("Enter a destination: ")
        input("Enter a departure date (DD/MM/YYYY): ")
        input("Enter a departure time (HH:MM): ")
        input("Enter the Pilot's SSN: ")
        input("Enter the Co-Pilot's SSN: ")
        more_pilots = input("Would you like to enter more pilots? (Y/N): ")
        while more_pilots:
            more_pilots = input("Would you like to enter more pilots? (Y/N): ")
            
        input("")
