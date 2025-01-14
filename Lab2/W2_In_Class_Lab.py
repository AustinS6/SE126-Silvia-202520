#W2D2 - Text file Handling Review w/ filters!








#--IMPORTS----------------------------------
import csv

#--FUNCTIONS--------------------------------
def difference(people, max_cap):
    diff = max_cap - people
    return diff

#--MAIN EXECUTION CODE----------------------


#initialize needed counting variables
total_rec = 0
rooms_over = 0

print(f"{'NAME':20}     {'MAX':5}   {'PPL':5}   {'OVER'}") #FIELD HEADERS for display
print("-----------------------------------------------------")
#----connected to file--------
with open("Text_Files/classLab2.csv") as csvfile:
    #we must indent one level while "connected to the file"

    file = csv.reader(csvfile)

    for rec in file:
        #below code occurs for every record (row) i nthe file (text file!)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1]) #all text data read as a string, so cast as a num!
        ppl = int(rec[2])

        #call the difference() to find people over/under capacity
        remaining = difference(ppl, max)

        #count and display rooms that are over capacity (remaining is negative)
        if remaining < 0:
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")

        total_rec += 1

#----connected to file--------
#display final data (counting vars)
print(f"\nRooms currently OVER CAPACITY: {rooms_over}")
print(f"Total rooms in file: {total_rec}\n\n")