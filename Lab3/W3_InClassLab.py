#W3 In Class Lab

#--IMPORTS----------------------------------
import csv

#--FUNCTIONS--------------------------------




#--MAIN EXECUTION CODE----------------------
dTop_tot = 0
lTop_tot = 0

print(f"{'TYPE':8}     {'BRAND':10}   {'CPU':5}   {'RAM':7}   {'1st Disk':7}       {'No HDD':8}   {'2nd Disk':7}            {'OS':5}   {'YR':5}")
print("----------------------------------------------------------------------------------------------------------------------------------")

with open("Text_Files/filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    desk_total = 0
    lap_total = 0

    type = []
    brand = []
    pcbrand = []
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
            device.append("DESKTOP")
        else:
            device.append("LAPTOP")


        if(rec[1] == "DL"):
            pcbrand.append("DELL")

        if(rec[1] == "HP"):
            pcbrand.append("HP")

        if(rec[1] == "GW"):
            pcbrand.append("GATEWAY")

        cpu.append(rec[2])
        ram.append(rec[3])
        firstDisk.append(rec[4])
        noHDD.append(int(rec[5]))

        if int(rec[5]) == 2:
            secondDisk.append(rec[6])
            os.append(rec[7])
            year.append(int(rec[8]))
        else:
            secondDisk.append("")
            os.append(rec[6])
            year.append(int(rec[7]))

for index in range(0, len(year)):
    if type[index] == "D" and year[index] <= 16:
        desk_total += 1
        dTop_tot += 2000
    if type[index] == "L" and year[index] <= 16:
        lap_total += 1
        lTop_tot += 1500

print("----------------------------------------------------------------------------------------------------------------------------------")

for i in range(0, len(type)):
    print(f"{device[i]:8}     {pcbrand[i]:10}   {cpu[i]:5}   {ram[i]:7}   {firstDisk[i]:7}   {noHDD[i]:8}          {secondDisk[i]:7}           {os[i]:5}   {year[i]:5}")

print(f"To replace {desk_total} it will cost $ {dTop_tot}")

print(f"To replace {lap_total} it will cost $ {lTop_tot}")
