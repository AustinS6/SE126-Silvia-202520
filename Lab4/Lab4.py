#W4D2 - Lab 4

#--Imports-------------------------------------------
import csv
#--Functions-----------------------------------------

#--Main Executing Code-------------------------------

fName = []
lName = []
email = []
dept = []
ext = []

with open("Text_Files/got_emails.csv")as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        fName.append(rec[0])
        lName.append(rec[1])
        email.append(rec[2])
        dept.append(rec[3])
        ext.append(rec[4])



print(f"{'FNAME':15} {'LNAME':15} {'AGE':3} {'EMAILS':30} {'DEPARTMENT':20 } {'EXT':4}")