# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# ISanchez,12.8.2019,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    from ProcessingClasses import FileProcessor as Fp
    from IOClasses import EmployeeIO as Eio
else:
    raise Exception("This file was not created to be imported")

# Main Body of Script  ---------------------------------------------------- #
lstEmpTable = []
lstFileData = []

lstFileData = Fp.read_data_from_file("EmployeeData.txt")
for row in lstFileData:
    lstEmpTable.append(Emp(row[0],row[1],row[2].strip()))


while True: # Show user a menu of options
    Eio.print_menu_items()
    strChoice = Eio.input_menu_options() # Get user's menu option choice
    if strChoice == '1':
        Eio.print_current_list_items(lstEmpTable)  # Show user current data in the list of employee objects
    if strChoice == '2':
        lstEmpTable.append(Eio.input_employee_data()) # Let user add data to the list of employee objects
    if strChoice == '3':
        Fp.save_data_to_file('EmployeeData.txt', lstEmpTable) # let user save current data to file
    if strChoice == '4':
        break # Let user exit program


# Main Body of Script  ---------------------------------------------------- #

# # Test data module
# objP1 = Emp(1, "Bob", "Smith")
# objP2 = Emp(2, "Sue", "Jones")
# lstTable = [objP1, objP2]
# for row in lstTable:
#     print(row.to_string(), type(row))
#
# #Test processing module
# Fp.save_data_to_file("EmployeeData.txt", lstTable)
# lstFileData = Fp.read_data_from_file("EmployeeData.txt")
# lstTable.clear()
# for line in lstFileData:
#     lstTable.append(Emp(line[0], line[1], line[2].strip()))
# for row in lstTable:
#     print(row.to_string(), type(row))
#
# #Test IO classes
# Eio.print_menu_items()
# Eio.print_current_list_items(lstTable)
# print(Eio.input_employee_data())
# print(Eio.input_menu_options())