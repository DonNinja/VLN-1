import csv
def readCrew():
    """ This reads the Crew.csv file and returns the ordered dictionary """
    data = []
    data.clear()
    with open("./STUDENTDATA/Crew.csv", "r") as file_stream:
        file_reader = csv.DictReader(file_stream)
        for line in file_reader:
            data.append(line)
    file_stream.close()
    return data

def checking_ssn(data, ssn):
    for line in data:
        if line['ssn'] == ssn:
            print(line)
            return line

def edit_wich():
    print("Type in what you would like to edit\nName?\nRole?\nRank?\nEmail?\nLicens?\nAddress?\nMobilenumber?\nHomephonenumber?")
    info_input = input("... ").lower()
    return info_input

def edit_info(info, employee):
    list_of_info = []
    new_info = input("Provide the new information: ")
    for item in employee.items():
        if item[0] == info:
            item[1] = list_of_info.append(new_info)
        else:
            list_of_info.append(item)
        
    

def main():
    data = readCrew()
    ssn = input("Enter SSN: ")
    employee = checking_ssn(data, ssn)
    if employee:
        info = edit_wich()
        editing = edit_info(info,employee)
main()