from DataLayer.Data import DataAPI
import string

class LogicAPI():
    def __init__(self):
        self.__data_getter = DataAPI()
        pass

    def showAllEmps(self):
        return self.__data_getter.getEmps()

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