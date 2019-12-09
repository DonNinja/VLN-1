from LogicLayer.Logic import LogicAPI

class UIDataPrinter:
    def __init__(self):
        self.__data_getter = LogicAPI()
        pass

    def printAllEmps(self):
        all_emp_list = self.__data_getter.showAllEmps()
        for emp in all_emp_list:
            emp_values = emp['ssn'], emp['name'], emp['role'], emp['rank'], emp['licence'], emp['address'], emp['mobilephonenumber'], emp['homephonenumber']
            for value in emp_values:
                if value:
                    print(value, end="\t")
            print()
        input("\nPress enter to continue...")