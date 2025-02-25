#W8D2 - Dictionaries and text File Data


#--IMPORTS-----------------------------------------------------------------------------
import csv

#--FUNCTIONS---------------------------------------------------------------------------


#--MAIN EXECUTION CODE-----------------------------------------------------------------

#mini review on dictionaries
library = {
    # indexes are STRINGS set by the developer
    #'key' : value
    "1230" : "Red Rising",
    "1231" : "The Little Prince"
}

with open("Text_Files/dictionary_file.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        #add each record's data as a new key + value pair from the text file
        #key --> rec[0] ; value --> rec[1]
        library.update({rec[0] : rec[1]})
        #when using .update() --> pass {'key' : value}


#disconnect from file
print(f"\n{'KEY':6}\t{'TITLE'}")
print("-" * 80)
for key in library:
    #for every key (and value) pair found within the 'library' dictionary
    print(f"{key:6}\t{library[key]}")
print("-" * 80)

#SEQUENTIAL SEARCH FOR A TITLE
search = input("Enter the TITLE you are looking for: ")
found = 0

for key in library:
    if search.lower() == library[key].lower():
        #store the found title's location in the dictionary -->
        found = key

if found != 0:
    print(f"KEY:{found:6}\tTITLE:{library[found]}")
else:
    print(f"Your search for {search} came up empty :[")



#type() returns the class type of the data passed to it
if type(library) is list:
    print("'Library' is a LIST")




#BINARY SEARCH for LIBRARY NUMBER (dictionary keys)
#in order to binary search a set of keys you must FIRST ...
#min = 0
#max = len(library_nums) - 1
#mid = int((min + max) / 2)

#while min < max and search != library_nums[mid]: