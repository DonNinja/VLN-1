from LogicLayer.Logic import LogicAPI

class UIDataPrinter:
    def __init__(self):
        self.__data_getter = LogicAPI()
        pass

    def printAllEmps(self):
        all_emp_list = self.__data_getter.showAllEmps()
        for emp in all_emp_list:
            print('''{:^10} ; {:^20} ; {:^9} ; {:^22} ; {:^12} ; {:^12} ; {:^7} ; {:^7}'''.format(emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']))
        input("\nPress enter to continue...")