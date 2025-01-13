#W2D1 - text File Handling - Introduction

#Step 1: import the csv (comma seperated value) library
import csv

total_records = 0

#STEP 2:
#connecting to the file's path - switch \ to /

print(f"{'NAME':10} \t {'NUM':3} \t {'COLOR'}")
print("------------------------------------")
with open("Text_Files/simple.csv") as csvfile:
    #indent 1 level! (new block)

    #allow processor to read the file data
    file = csv.reader(csvfile)


    for record in file:
        
        
         total_records += 1

        #the list view of each record (row)

         name = record[0]
         number = record[1]
         color = record[2]

         print(f"{name:10} \t {number:3} \t {color.title()}")
#----disconnected from file------------------------------
print("------------------------------------")

print(f"\nTOTAL RECORDS: {total_records}\n")