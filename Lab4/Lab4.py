#Austin Silvia
#2/3/2025
#
# Part 1:
#Write a program that utilizes the got_emails.csv file. Store the file data into 1D parallel lists, then use the information in the lists to assign additional data to each employee. Use the tables below to assign each employee in the file a unique email address, a department, and a unique phone extension.
#When you are complete, display the following data for each employee (first name, last name, department, email, and phone extension) to the user.
#
# Part 2:
#Once you have completed populating all eight parallel lists and displaying the five required back to the user (and in the same Python file), create and write the following data for each employee to a file named westeros.csv: first name, last name, email, department, and phone extension. NOTE: each employee’s data should be on its own record (row) within the newly created file. You will most likely end up with an extra empty line at the end of the file (this is okay for this lab as we will not be reprocessing the data found in this new file). Once the file is ready, close it and alert the user via a displayed message. Also tell them how many employees are in the file, and the total count of employees for each department.
#
#W4D2 - Lab 4

#--Imports-------------------------------------------
import csv
#--Functions-----------------------------------------

#--Main Executing Code-------------------------------

fName = []
lName = []
age = []
screenName = []
hAllegience = []
email = []
dept = []
ext = []

#Variables:
extAdd = 0
starkTot = 0
targaryenTot = 0
tullyTot = 0
lannisterTot = 0
baratheonTot = 0
nightWatchTot = 0
empTot = 0

print(f"{'FIRST':8} {'LAST':10} {'EMAILS':30} {'DEPARTMENT':23} {'EXT':3}")
print("---------------------------------------------------------------------------------")

with open("Text_Files/got_emails.csv")as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        age.append(rec[2])
        screenName.append(rec[3])
        hAllegience.append(rec[4])
        if rec[4] == "House Stark":
            dept.append("Research & Development")
            ext.append(100 + extAdd)
            extAdd += 1
            starkTot += 1
        elif rec[4] == "House Targaryen":
            dept.append("Marketing")
            ext.append(200 + extAdd)
            extAdd += 1
            targaryenTot += 1
        elif rec[4] == "House Tully":
            dept.append("Human Resources")
            ext.append(300 + extAdd)
            extAdd += 1
            tullyTot += 1
        elif rec[4] == "House Lannister":
            dept.append("Accounting")
            ext.append(400 + extAdd)
            extAdd += 1
            lannisterTot += 1
        elif rec[4] == "House Baratheon":
            dept.append("Sales")
            ext.append(500 + extAdd)
            extAdd += 1
            baratheonTot += 1
        elif rec[4] == "The Night's Watch":
            dept.append("Auditing")
            ext.append(600 + extAdd)
            extAdd += 1
            nightWatchTot += 1
        else:
            print("INVALID INPUT")
        email.append(rec[3] + "@westeros.net")
        empTot += 1

for i in range(0, len(fName)):
    print(f"{fName[i]:8} {lName[i]:10} {email[i]:30} {dept[i]:23} {ext[i]:3}")
print("---------------------------------------------------------------------------------")

#Creating New File
file = open('Text_Files/westeros.csv', 'w')

for i in range(0, len(fName)-1):
    file.write(f"{fName[i]},{lName[i]},{email[i]},{dept[i]},{ext[i]}\n")
else:
    i += 1
    file.write(f"{fName[i]},{lName[i]},{email[i]},{dept[i]},{ext[i]}")

file.close()

print("FILE COMPLETED :)")

print(f"Total number of employees: {empTot}")
print(f"The total amount of employees Dept. Research & Development: {starkTot}")
print(f"The total amount of employees Dept. Marketing: {targaryenTot}")
print(f"The total amount of employees Dept. Human Resources: {tullyTot}")
print(f"The total amount of employees Dept. Accounting: {lannisterTot}")
print(f"The total amount of employees Dept. Sales: {baratheonTot}")
print(f"The total amount of employees Dept. Auditing: {nightWatchTot}")