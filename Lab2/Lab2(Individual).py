#W2D2 Individual Lab2








#--IMPORTS----------------------------------
import csv

#--FUNCTIONS--------------------------------




#--MAIN EXECUTION CODE----------------------

#----connected to file--------

print(f"{'TYPE':8}     {'BRAND':10}   {'CPU':5}   {'RAM':7}   {'1st Disk':7}       {'No HDD':8}   {'2nd Disk':7}            {'OS':5}   {'YR':5}")
print("----------------------------------------------------------------------------------------------------------------------------------")

with open("Text_Files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)


    for rec in file:

        type = rec[0]
        Brand = rec[1]

        if(rec[0] == "D"):
            device = "DESKTOP"
        else:
            device = "LAPTOP"

        if(rec[1] == "DL"):
            pcbrand = "DELL"

        if(rec[1] == "HP"):
            pcbrand = "HP"

        if(rec[1] == "GW"):
            pcbrand = "GATEWAY"

        cpu = rec[2]
        ram = rec[3]
        firstDisk = rec[4]
        noHDD = int(rec[5])

        if noHDD == 2:
            secondDisk = rec[6]
            os = rec[7]
            year = rec[8]

            print(f"{device:8}     {pcbrand:10}   {cpu:5}   {ram:7}   {firstDisk:7}   {noHDD:8}          {secondDisk:7}           {os:5}   {year:5}")
        else:
            os = rec[6]
            year = rec[7]

            print(f"{device:8}     {pcbrand:10}   {cpu:5}   {ram:7}   {firstDisk:7}   {noHDD:8}                            {os:5}   {year:5}")