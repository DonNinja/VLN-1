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

    def checkSSN(self, ssn, data):
        """ This checks for multiple varies of SSN """
        check_data = self.checking_if_in_data(data, ssn)
        check_int = self.digit_check(ssn)
        check_len = self.len_ssn(ssn)
        check_date = self.date_check_ssn(ssn)
        if check_int and check_len and check_date and check_data:
            return True
        return False
    
    def checkName(self,name):
        """ This forwards to a function for check """
        check = self.name_check(name)
        if check:
            return check
        else:
            return False

    def checkPhone(self, num):
        """ This checks if phonenum is ints and checks length of list """
        list_num = []
        int_check = self.digit_check(num)
        if int_check:
            for line in num:
                for i in line:
                    list_num.append(i)
        if len(list_num) == 7:
            return True
        else:
            print("Not a valid phone number")
            return False


    def checkLicens(self, licens):
        """ This checks if licens is valid. If licens is N/A it returns it right away """
        if licens == 'N/A':
            return licens
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
        
    def checkEmail(self, email):
        """ This checks validation for email (only numbers and alphabet) no longer then 20 letters """
        email_list = []
        for line in email:
            for ch in line:
                email_list.append(ch)
        if email.isalnum():
            if len(email_list) < 20:
                return email
            else:
                print("Email is in wrong format")
                return False
        else:
            print("Email is in wrong format")
            return False
       

    def checkRank(self, rank, role):
        """ This takes input int from user and turns it into the desired rank """
        if self.digit_check(rank):
            if rank == '1' and role == 'Pilot':
                rank = CAPTAIN
                return rank
            if rank == '2' and role == 'Pilot':
                rank = COPILOT
                return rank
            if rank == '1' and role == 'Cabincrew':
                rank = FLIGHTATT
                return rank
            if rank == '2' and role == 'Cabincrew':
                rank = FLIGHTSMANAGER
                return rank
            if rank != '1' or '2':
                return False


    def checkAddress(self, address):
        """ This forwards to a check function """
        check = self.address_check(address)
        if check:
            return check
        else:
            return False

    def digit_check(self, data):
        """ This checks for int """
        try:
            ssn = [str(int(i)) for i in data.split()]
            return True
        except:
            ValueError
            print('Error, only numbers allowed')
            return False

    def len_ssn(self, check):
        """ This checks length of SSN """
        list_ssn = []
        for row in check:
            for i in row:
                list_ssn.append(i)
        if len(list_ssn) == 10:
            return True

    def date_check_ssn(self, ssn):
        """ This checks if SSN is valid """
        if re.match(r"^[0-7]\d[01]\d{3}[-]*\d{3}[09]$", ssn):
            print("SSN is valid")
            return True
        else:
            print("SSN is invalid")
            return False

    def address_check(self, address):
        """ This splits adress in two parts, checks if alpha in [0], checks int in [-1] """
        address_list = address.split(" ")
        first_address = address_list[0]
        digit_address = address_list[-1]
        full_address = ''
        if first_address.isalpha() and digit_address.isdigit():
            if first_address == digit_address:
                print("Address is invalid")
                return False
            else:
                full_address = first_address.capitalize() + " " + digit_address 
                print("Address is valid")  
                return full_address
        else:
            print("Address is invalid")
            return False

    def name_check(self, name):
        """ This splits name and checks in two parts (only takes first and last name) only alpha """
        name_list = name.split(" ")
        first_name = name_list[0]
        last_name = name_list[-1]
        full_name = ''
        if first_name.isalpha() and last_name.isalpha():
            if first_name == last_name:
                print("Name is invalid")
                return False
            else:
                full_name = first_name.capitalize() + " " + last_name.capitalize() 
                print("Name is valid")  
                return full_name
        else:
            print("Name is invalid")
            return False
        