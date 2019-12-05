class UserInputCheck:
    def __init__(self):
        pass

    def empDataInput(self, type=""):
        data_list = []
        print()
        ssn = input("Enter new {}'s ssn: ".format(type)).capitalize()
        #if __data_worker.checkSSN(ssn):
        data_list.append(ssn)
        name = input("Enter new {}'s name: ".format(type)).capitalize()
        #if __data_worker.checkName(name)
        data_list.append(name)
        role = input("Enter new {}'s role: ".format(type)).capitalize()
        #if __data_worker.checkRole(role)
        data_list.append(role)
        rank = input("Enter new rank: ".format(type)).capitalize()
        #if __data_worker.checkRank(rank)
        data_list.append(rank)
        if type != "flight attendant":
            licens = input("Enter new {}'s license: ".format(type)).capitalize()
            #if __data_worker.checkLicense(licens)
            data_list.append(licens)
        else:
            licens = "N/A"
        address = input("Enter new {}'s address: ".format(type)).capitalize()
        #if __data_worker.checkAddress(address)
        data_list.append(address)
        mobile = input("Enter new {}'s mobile number: ".format(type)).capitalize()
        #if __data_worker.checkMobile(mobile)
        data_list.append(mobile)
        home_phone = input("Enter new {}'s home phone number: ".format(type)).capitalize()
        #if __data_worker.checkHomePhone(home_phone)
        data_list.append(home_phone)
        print(data_list)
        input("Press enter to continue...")
        return data_list