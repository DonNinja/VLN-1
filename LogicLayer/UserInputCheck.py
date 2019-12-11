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
        pass

    def checkSSN(self, ssn):
        check_int = self.digit_check(ssn)
        check_len = self.len_ssn(ssn)
        check_date = self.date_check_ssn(ssn)
        if check_int and check_len and check_date:
            return True

    
    def checkName(self, first_name, last_name):
        check = self.name_check(first_name, last_name)
        if check:
            return True
        else:
            return False

    def checkPhone(self, num):
        list_num = []
        int_check = self.digit_check(num)
        if int_check:
            for line in num:
                for i in line:
                    list_num.append(i)
        if len(list_num) == 7:
            return True


    def checkLicens(self, licens):
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
                if self.address_check(address_alpha):
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

    def address_check(self, address):
        if address.isalpha():
            return True
        else:
            return False

    def name_check(self, first_name, last_name):
        if first_name.isalpha():
            if last_name.isalpha():
                print("Name is valid")
                return True
        else:
            print("Name in wrong format!")
            return False
                




    def addLocationCountry(self):
        pass