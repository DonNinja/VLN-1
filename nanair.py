import csv
'''Add new aircraft, check for input and makes sure there arent any airplanes
currently registered with the same Insignia'''

def airplane_input_check(planeInsignia, planeTypeID, plane_list):
    input_list = []
    input_list.append(planeInsignia)
    input_list.append(planeTypeID)
    if len(input_list[0]) == 6 and len(input_list[1]) <= 12:
        for i in plane_list:
            if planeInsignia in i:
                return False
        return True
    else:
        return False

def open_aircraft_file():
    with open('Aircraft.csv','r') as userFile:
        airplane_list = []
        userFileReader = csv.reader(userFile)
        for row in userFileReader:
            airplane_list.append(row)
    return airplane_list

def edit_aircraft_file(plane_list):
    with open('Aircraft.csv', 'a', newline='') as newFile:
        newFileWriter = csv.writer(newFile)
        planeInsignia = input("Enter new plane insignia(ex. TF-XXX): ")
        planeTypeID = input("Enter new plane type ID(ex. NABAE146): ")
        valid_input = airplane_input_check(planeInsignia, planeTypeID, plane_list)
        if valid_input == True:
            newFileWriter.writerow([planeInsignia, planeTypeID])
        else:
            print("Invalid input")

plane_list = open_aircraft_file()
edit_aircraft_file(plane_list)
    

################################
