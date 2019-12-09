from DataLayer.Data import DataAPI
import string

class LogicAPI():
    def __init__(self):
        self.__data_getter = DataAPI()
        
    

    def showAllEmps(self):
        all_emp_list = self.__data_getter.getEmps()
        return all_emp_list

    def checkEmpRole(self, data, num):
        all_emp_list = self.__data_getter.getEmps()
        for row in all_emp_list: 
            if row[num] == data:
                return True
        