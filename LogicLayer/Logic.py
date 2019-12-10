from DataLayer.Data import DataAPI
from LogicLayer.SortData import SortData

class LogicAPI():
    def __init__(self):
        self.__data_getter = DataAPI()
        self.__data_sorter = SortData()

    def showAllEmps(self):
        """ This returns a collection of every employee to the UI so it can print them out """
        return self.__data_getter.getEmps()
    
    def showAllPilots(self):
        """ This gets a collection of every employee, then calls a function to sort the collection into a collection of just pilots and returns that """
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortPilots(all_emps) # Sorts through all_emps and returns only flight attendants
    
    def showAllAttendants(self):
        """ This gets a collection of every employee, then calls a function to sort the collection into a collection of just flight attendants and returns that """
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortAttendants(all_emps) # Sorts through all_emps and returns only flight attendants
    
    def showAllPlanes(self):
        """ This returns a list of every plane so the UI can print them out """
        return self.__data_getter.getAirplanes()
    
    def showPilotSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that is both a pilot and has the inputted SSN and returns him if it finds him, but returns None if he finds nothing """
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortPilotSSN(all_emps, ssn)
    
    def showAttendantSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that is both a flight attendant and has the inputted SSN and returns him if it finds him, but returns None if he finds nothing """
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortAttendantSSN(all_emps, ssn)
    
    def showEmpSSN(self, ssn):
        """ This gets a list of every employee then looks for the employee that has the inputted SSN and returns him, but returns None if he finds nothing """
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortEmployeeSSN(all_emps, ssn)
    
    def showPilotByPlane(self, plane_type):
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortPilotsByPlane(all_emps, plane_type)

    def addEmpLL(self,data_list):
        self.__data_getter.registerNewData(data_list)
        pass

    def addPlane(self,data_list):
        self.__data_getter.registerPlanes(data_list)

    def editPilot(self,ssn):
        all_emps = self.__data_getter.getEmps()
        return self.__data_sorter.sortPilotSSN(all_emps, ssn)

        



# import re
# class Employee:

#     def __init__(self, file_stream, choice):
#         self.__choice = choice
#         self.__file = file_stream
#         self.__emp = self.createEmp(choice)
#         self.__name = self.nameEmp()


#     def __str__(self):
#         str_emp = str(self.__emp)
#         return "{}".format(str_emp)


#     def createEmp(self, choice):
#         dict_employees = {}
#         if choice == '1':
#             ssn = input("Enter ssn:")
#             check = self.digit_ssn(ssn)
#             length = self.len_ssn(check)
#             date = self.date_check_ssn(ssn)
#             if check and length:
#                 print("hæ")
#             else:
#                 print("bæ")

#         return dict_employees

#     def digit_ssn(self, ssn):
#         list_num = []
#         try:
#             number = [str(int(i)) for i in ssn.split()]
#             for line in number:
#                 for i in line:
#                     list_num.append(i)
#             return list_num
#         except:
#             ValueError
#             print('Error, only numbers allowed')
#             return False

#     def len_ssn(self, check):
#         if len(check) == 10:
#             return True

#     def date_check_ssn(self, ssn):
#         ssn_ints = [int(i) for i in ssn]
#         dates = ssn_ints[0] + ssn_ints[1]
#         month = ssn_ints[2] + ssn_ints[3]
#         if re.match(r"^[0-7]\d[01]\d{3}[-]*\d{3}[09]$", ssn):
#             print("SSN is valid")
#         else:
#             print("SSN is invalid")


#     def nameEmp(self):
#         name = str(input("What is your name? "))
#         print(name.isalpha()) 
#         return name.isalpha()