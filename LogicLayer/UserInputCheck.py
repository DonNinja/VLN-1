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
        error_list = []
        check_int, int_error = self.digitCheck(ssn) # Checks if input is digits
        check_len, length_error = self.lenSSN(ssn) # Checks length if input
        check_date, date_error = self.dateCheckSSN(ssn) # Checks if dates are valid
        if int_error:
            error_list.append(int_error)
        if length_error:
            error_list.append(length_error)
        if date_error:
            error_list.append(date_error)
        if check_int and check_len and check_date: # If all these return True SSN is valid
            return True, None
        return False, error_list
    
    def checkName(self,name):
        """ This forwards to a function for check """
        check, error_msg = self.nameCheck(name)
        if check:
            return check, None
        else:
            return False, error_msg

    def checkPhone(self, num):
        """ This checks if phonenum is ints and checks length of list """
        list_num = []
        int_check = self.digitCheck(num)
        if int_check:
            for line in num:
                for i in line:
                    list_num.append(i)
        if len(list_num) == 7:
            return True, None
        else:
            return False, "Phone number must be 7 numbers"


    def checkLicens(self, licens):
        """ This checks if licens is valid. If licens is N/A it returns it right away """
        if licens == 'N/A':
            return licens
        if self.digitCheck(licens):
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
        else:
            return False

    def checkEmail(self, email):
        """ This checks validation for email (only numbers and alphabet) no longer then 20 letters """
        email_list = []
        for line in email:
            for ch in line:
                email_list.append(ch)
        if email.isalnum():
            if len(email_list) < 20:
                return email + "@NaNAir.is", None
            else:
                return False, "Email is too long, must be under 20 characters"
        else:
            return False, "Email can not be only numbers, or includes forbidden characters"

    def checkRank(self, rank, role):
        """ This takes input int from user and turns it into the desired rank """
        if self.digitCheck(rank):
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
        else:
            return False
            
    def checkAddress(self, address):
        """ This forwards to a check function """
        check, error_msg = self.addressCheck(address)
        if check:
            return check, None
        else:
            return False, error_msg

    def digitCheck(self, data):
        """ This checks for int """
        try:
            [str(int(i)) for i in data.split()]
            return True, None
        except:
            ValueError
            return False, 'Error, only numbers allowed'

    def lenSSN(self, check):
        """ This checks length of SSN """
        list_ssn = []
        for row in check:
            for i in row:
                list_ssn.append(i)
        if len(list_ssn) == 10:
            return True, None
        else:
            return False, "It's too long or too short, must be 10 characters."

    def dateCheckSSN(self, ssn):
        """ This checks if SSN date is valid """
        if re.match(r"^[0-7]\d[01]\d{3}[-]*\d{3}[09]$", ssn):
            return True, None
        else:
            return False, "The date is invalid."

    def addressCheck(self, address):
        """ This splits adress in two parts, checks if alpha in [0], checks int in [-1] """
        address_list = address.split(" ")
        first_address = address_list[0]
        digit_address = address_list[-1]
        full_address = ''
        if first_address.isalpha() and digit_address.isdigit():
            if first_address == digit_address:
                return False, "First and last address can not be same"
            else:
                full_address = first_address.capitalize() + " " + digit_address 
                return full_address, None
        else:
            return False, "Invalid address (example: Fellsmuli 20)"

    def nameCheck(self, name):
        """ This splits name and checks in two parts (only takes first and last name) only alpha """
        name_list = name.split(" ") # Splits name on spaces
        first_name = name_list[0] # Takes the first 
        last_name = name_list[-1]
        full_name = ''
        if first_name.isalpha() and last_name.isalpha():
            if first_name == last_name:
                return False, "First and last name can not be the same"
            else:
                full_name = first_name.capitalize() + " " + last_name.capitalize() 
                return full_name, None
        else:
            return False, "Names must be all letters"

    def checkPilotAvailability(self):
        pass

    def checkNum(self, num):
        try:
            num = int(num)
            return True
        except:
            return False