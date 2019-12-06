class DataAPI:
    def __init__(self):
        self.file_stream = open("STUDENTDATA\\Crew.csv", "r")

    def getEmps(self):
        all_emp_list = []
        for line in self.file_stream:
            emp_data_list = line.split(",")
            all_emp_list.append(emp_data_list)
        return all_emp_list