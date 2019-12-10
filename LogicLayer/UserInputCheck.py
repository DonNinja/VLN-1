from LogicLayer.Logic import LogicAPI
import re
CAPTAIN = 'Captain'
COPILOT = 'Copilot'
FLIGHTATT = 'Flight Attendant'
FLIGHTSMANAGER = 'Flight Service Manager'
LICENSE_FOKKER100 = 'NAFokkerF100'
LICENSE_FOKKER28 = 'NAFokkerF28'
LICENSE_NABAE146 = 'NABAE146'

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

    def checkPhone(self, homephonenum):
        count = 0
        for row in homephonenum:
            for i in row:
                count += 1
        if count == 7:
            return homephonenum
        else:
            return False

    def checkLicense(self, licens):
        if self.digit_check(licens):
            if licens == '1':
                licens = LICENSE_FOKKER100
                return licens
            if licens == '2':
                licens = LICENSE_FOKKER28
                return licens
            if licens == '3':
                licens = LICENSE_NABAE146
                return licens
            if licens != '1' or '2' or '3':
                return False
       

    def checkRank(self, rank, role):
        if self.digit_check(rank):
            if rank == '1' and role == 'Pilot':
                rank = CAPTAIN
                return rank
            if rank == '2' and role == 'Pilot':
                rank = COPILOT
                return rank
            if rank == '1' and role == 'Flight attendant':
                rank = FLIGHTATT
                return rank
            if rank == '2' and role == 'Flight attendant':
                rank = FLIGHTSMANAGER
                return rank
            if rank != '1' or '2':
                return False


    def checkAddress(self, address):
        try:
            address_list = address.split()
            address_alpha = address_list[0] # Checka len á þessu
            address_int = address_list[1] # Checka len á þessu
            if len(address_list) == 2:
                if self.name_check(address_alpha):
                    if self.digit_check(address_int):
                        return True
        except IndexError:
            print("Address not in the right format!")
            return False
    

            

    def digit_check(self, data):
        try:
            ssn = [str(int(i)) for i in data.split()]
            return True
        except:
            ValueError
            print('Error, only numbers allowed')
            return False

    def len_ssn(self, check):
        list_ssn = []
        for row in check:
            for i in row:
                list_ssn.append(i)
        if len(list_ssn) == 10:
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