from LogicLayer.Logic import LogicAPI

class DataPrinter:
    def __init__(self):
        self.__data_getter = LogicAPI()
        pass

    def printAllEmps(self):
        all_emp_list = self.__data_getter.showAllEmps()
        for emp in all_emp_list:
            for data in emp:
                print(data, end=" ")
            # print()
        input("\nPress enter to continue...")