#W4D2 - Sequential Search Review + Creating & Writing to Text Files



#--IMPORTS-------------------------------------------
import csv
#--FUNCTIONS-----------------------------------------

#--MAIN EXECUTING CODE-------------------------------

#creating empty lists - one for each field
dragons = []
riders = []
count = []
color1 = []
color2 = []

with open("Text_Files/dragons.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        dragons.append(rec[0])
        riders.append(rec[1])
        count.append(rec[2])
        color1.append(rec[3])

        if rec[2] == "2":
            color2.append(rec[4])
        elif rec[2] == "1":
            color2.append("---")
        else:
            color2.append("ERROR")
#disconnected from file ------------------

#process the lists to display data to the console
print(f"{'DRAGONS':15} {'RIDERS':30} {'#':3} {'COLOR1':8} {'COLOR2'}")
print("-----------------------------------------------------------------")

for i in range(0, len(dragons)):
    print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]}")
print("-----------------------------------------------------------------")

#SEARCH FOR A SPECIFIC DRAGON
#step 1: set-up and gain of search
found = "x"
search = input("Which dragon are you looking for: ")

#step 2: perform search --> for loop w/ if statement
for i in range(0, len(dragons)):
    if search.lower() in dragons[i].lower():
        #hold onto the found location of our searched-for value
        found = i

#step 3: filter and display results
if found != "x": #search was found!
    print(f"Your search for {search} was FOUND:")
    print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]}")
else:
    print(f"Your search for {search} was NOT FOUND :[")


#SEARCH FOR A COLOR SET
found = []
search = input("Enter the dragon color you are looking for: ")

for i in range(0, len(color1)):

    if search.lower() in color1[i] or search.lower() in color2[i]:
        found.append(i)

if not found: #"if the found list is empty"
    print(f"Your search for {search} was NOT FOUND :[")
else:
    print(f"Your search for {search} was FOUND:")
    for i in range(0, len(found)):
        print(f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]}")

#WRITE SOME DATA TO A NEW FILE
#create and write dragons and riders of the data to a new text file:
file = open('Text_Files/targs.csv', 'w')

for i in range(0, len(dragons)-1):
    file.write(f"{dragons[i]},{riders[i]}\n")
else:
    file.write(f"{dragons[i]},{riders[i]}")

file.close()