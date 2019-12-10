class Employee():
    def __init__(self, ssn, name, role, rank, licence, address, mobile_phone_number, home_phone_number):
        self.__ssn = ssn
        self.__name = name
        self.__role = role
        self.__rank = rank
        self.__licence = licence
        self.__address = address
        self.__mobile_phone_number = mobile_phone_number
        self.__home_phone_number = home_phone_number

    # methods to get for example only the name 
    #outside of the class

    def setSsn(self,newssn):
        self.__ssn = newssn

    def getSsn(self):
        return self.__ssn

    def setName(self,newname):
        self.__name = newname

    def getName(self):
        return self.__name

    def setRole(self,newrole):
        self.__role = newrole

    def getRole(self):
        return self.__role

    def setRank(self,newrank):
        self.__rank = newrank

    def getRank(self):
        return self.__rank

    def setLicence(self,newlicence):
        self.__licence = newlicence

    def getLicence(self):
        return self.__licence

    def setAddress(self,newaddress):
        self.__address = newaddress

    def getMobilePhoneNumber(self):
        return self.__mobile_phone_number

    def setMobilePhoneNumber(self,newmobilephonenumber):
        self.__mobile_phone_number = newmobilephonenumber

    def getHomePhoneNumber(self):
        return self.__home_phone_number

    def setHomePhoneNumber(self,newhomephonenumber):
        self.__home_phone_number = newhomephonenumber


    def __str__(self):
        return "{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}".format(self.__ssn,
                                                        self.__name,self.__role,
                                                        self.__rank,self.__licence,
                                                        self.__address,self.__mobile_phone_number,
                                                        self.__home_phone_number) 
    


    