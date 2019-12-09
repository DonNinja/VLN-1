from LogicLayer.Logic import LogicAPI 
import re
COPILOT = 'Copilot'
CAPTAIN = 'Captain'
FLIGHTSMANAGER = 'Flight Service Manager'
FLIGHTATT = 'Flight Attendant'

class UserInputCheck:
    def __init__(self):
        self.__data_checker = LogicAPI()

    def checkSSN(self, ssn):
        check_int = self.digit_check(ssn)
        check_len = self.len_ssn(ssn)
        check_date = self.date_check_ssn(ssn)
        if check_int and check_len and check_date:
            return True
    
    def checkName(self, name):
        check = self.name_check(name)
        if check:
            return True

    def checkRank(self, rank, role):
        if self.digit_check(rank):
            if rank == '1' and role == 'Pilot':
                rank = CAPTAIN
            if rank == '2' and role == 'Pilot':
                rank = COPILOT
            if rank == '1' and role == 'Flight attendant':
                rank = FLIGHTATT
            if rank == '2' and role == 'Flight attendant':
                rank = FLIGHTSMANAGER
        print(rank)
        return rank


    def checkAdress(self, adress):
        list_adress = adress.split(" ")
        if list_adress[0] == 'Fellsmúli':
            print('Valid')
        else:
            print('Not in Fellsmúli??')

    def digit_check(self, data):
        try:
            ssn = [str(int(i)) for i in data.split()]
            return True
        except:
            ValueError
            print('Error, only numbers allowed')
            return False

    def len_ssn(self, check):
        ssn = [str(int(i)) for i in check.split()]
        if len(ssn) == 10:
            return True

    def date_check_ssn(self, ssn):
        #ssn_ints = [int(i) for i in ssn]
        #dates = ssn_ints[0] + ssn_ints[1]
        #month = ssn_ints[2] + ssn_ints[3]
        if re.match(r"^[0-7]\d[01]\d{3}[-]*\d{3}[09]$", ssn):
            print("SSN is valid")
            return True
        else:
            print("SSN is invalid")
            return False

    def name_check(self, name):
        name_strip = name.replace(" ", "")
        if name_strip.isalpha():
            print("Valid")
            return True
        else:
            print("Name is not in the right format")
            return False



    def addLocationCountry(self):
        pass