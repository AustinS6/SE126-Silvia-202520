#W3 In Class Lab

#--IMPORTS----------------------------------
import csv

#--FUNCTIONS--------------------------------




#--MAIN EXECUTION CODE----------------------


with open("Text_Files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    desk_total = 0
    lap_total = 0

    type = []
    brand = []
    device = []
    cpu = []
    ram = []
    firstDisk = []
    secondDisk = []
    noHDD = []
    os = []
    year = []

    for rec in file:

        type.append(rec[0])
        brand.append(rec[1])

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

        cpu.append(rec[2])
        ram.append(rec[3])
        firstDisk.append(rec[4])
        noHDD.append(int(rec[5]))

        if noHDD == 2:
            secondDisk.append(rec[6])
            os.append(rec[7])
            year.append(rec[8])

        else:
            secondDisk.append("")
            os.append(rec[6])
            year.append(rec[7])

for index in range(0, len(year)):
    if type == "D" and year <= 16:
        desk_total += 1
    if type == "L" and year <= 16:
        lap_total += 1
    
    #
    



