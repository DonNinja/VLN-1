# def create_crew_list(file_stream):
#     crew_list = []
#     for line in file_stream:
#         to_add_to_crew_list = line.split(",")
#         crew_list.append(to_add_to_crew_list)
#         return crew_list

# def open_file(file_name):
#     try:
#         file_stream = open(file_name, "r")
#         return file_stream
#     except FileNotFoundError:
#         return "None"

# file_name = "crew.csv"
# file_stream = open_file(file_name)
# display_crew = create_crew_list(file_stream)

from UILayer.UserUI import UserUI

def main():
    ui = UserUI()
    ui.startScreen()

if __name__ == "__main__":
    main()