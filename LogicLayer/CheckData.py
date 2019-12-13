import datetime
import dateutil

class CheckData:
    def __init__(self):
        pass
    
    def checkIfWorkedOnDay(self, inp, date, work_trips):
        ''' Checks if the employee or plane has flown on the same day '''
        for item in work_trips:
            dep_obj = dateutil.parser.parse(item['departure'])
            if (item['aircraftID'] == inp or item['captain'] == inp or item['copilot'] == inp or item['fsm'] == inp or item['fa1'] == inp or item['fa2'] == inp) and dep_obj.date() == date: #Checks if the inp is in any of the flights today
                return True
        return False
    
    def checkIfExists(self, inp, field, data):
        for item in data:
            if item[field] == inp:
                return False, ["User already exists"]
        return True, None