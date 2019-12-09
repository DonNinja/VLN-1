from LogicLayer.Logic import LogicAPI

class UserInputCheck:
    def __init__(self):
        self.__data_checker = LogicAPI()
        self.__ssn = self.checkSSN(ssn)

    def checkSSN(self, ssn):
        status = True
        while status == True:
            check_int = self.digit_ssn(ssn)
            check_len = self.len_ssn(check_int)
            check_date = self.date_check_ssn(ssn)
            if check_int and check_len and check_date:
                status = False
                return ssn



    def digit_check(data):
        try:
            ssn = [str(int(i)) for i in ssn.split()]
            return True
        except:
            ValueError
            print('Error, only numbers allowed')
            return False

    def len_ssn(check):
        if len(check) == 10:
            return True

    def date_check_ssn(ssn):
        #ssn_ints = [int(i) for i in ssn]
        #dates = ssn_ints[0] + ssn_ints[1]
        #month = ssn_ints[2] + ssn_ints[3]
        if re.match(r"^[0-7]\d[01]\d{3}[-]*\d{3}[09]$", ssn):
            print("SSN is valid")
            return True
        else:
            print("SSN is invalid")
            return False


    def addLocationCountry(self):
        pass