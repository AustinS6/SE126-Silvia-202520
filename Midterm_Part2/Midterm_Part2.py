#Austin Silvia
#2/4/25

#Prompt Choice 2:
#Using the file named above, read the data from the file and store to 1D parallel lists. Once the lists have been fully populated with file data, create a new list to hold a “status” value for each book. Assign each book a status value of “On Loan” or “Available” and store to the newly created list. Half of the books should be “On Loan” and the other half should be “Available” – you can decide which books hold which status as long as it is an even split between the two potential values. Once the new list is populated, process through the five lists to display all of the data to the user as well as the total number of records in the file.

#Once all of the data has been displayed, write all of the list data to a new file called ‘midterm_choice2.csv’, where each book’s information is found on one record in the file and their data is separated by a comma (additional empty line in resulting file is okay).

#Finally, create a sequential search program that allows a user to repeatedly search the book database information stored in the lists based on the following menu:
#Personal Library Search:
#1. Search by TITLE
#2. Search by AUTHOR
#3. EXIT

#For option 1: When a searched-for item is found, print all data* in the program on the specific book from the lists. If they are not found, alert the user.
#For option 2: When a searched for item is found, print all data* in the program on all authors that match the criteria. If no one matches the searched-for criteria, alert the user.



#--IMPORTS--------------------------------------------
import csv
#--FUNCTIONS------------------------------------------

#--MAIN EXECUTING CODE--------------------------------

#Empty Lists to hold data
title = []
author = []
genre = []
pages = []
status = []

#variables
tot_rec = 0

print(f"{'TITLE':30} {'AUTHOR':18} {'GENRE':17} {'PAGES':3}  {'STATUS':10}")
print("------------------------------------------------------------------------------------")

with open("Midterm_Part2/books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        title.append(rec[0])
        author.append(rec[1])
        genre.append(rec[2])
        #Fantasy, Mystery, and Thriller books are Available
        if rec[2] == "fantasy":
            status.append("Available")
        if rec[2] == "mystery":
            status.append("Available")
        if rec[2] == "thriller":
            status.append("Available")
        #Horror and Science Fiction books are On Loan
        if rec[2] == "horror":
            status.append("On Loan")
        if rec[2] == "science fiction":
            status.append("On Loan")
        pages.append(rec[3])
        tot_rec += 1

for i in range(0, len(title)):
    print(f"{title[i]:30} {author[i]:18} {genre[i]:17} {pages[i]:3}    {status[i]:10}")
print("------------------------------------------------------------------------------------")
print (f"The total amount of records in the file is: {tot_rec}")
#Creating New File
file = open("Midterm_Part2/midterm_choice2.csv", 'w')

for i in range(0, len(title)-1):
    file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}\n")
else:
    i += 1
    file.write(f"{title[i]},{author[i]},{genre[i]},{pages[i]},{status[i]}")

file.close()

print("FILE COMPLETED :)")
print("")

#Sequential Search
answer = "y"

while answer == "y":
    print("\n\nPersonal Library Search\n\n")
    print("1. Search by TITLE")
    print("2. Search by AUTHOR")
    print("3.EXIT")
    search_type = input("Enter your search type [1-3]:")

    if search_type == "1":
        #Searching for specific book title
        print("\tSEARCH BY TITLE")

        found = -1

        search_title = input("Enter the TITLE of the book: ")

        for i in range(0, len(title)):
            if search_title.lower() in title[i].lower():
                found = i
        
        if found != -1:
            #Book title was found
            print(f"Your search for {search_title} was FOUND!")
            print(f"{title[found]:30} {author[found]:18} {genre[found]:17} {pages[found]:3}    {status[found]:10}")
        else:
            #If Book title was not found
            print(f"Your search for {search_title} was *NOT* FOUND!")
            print(f"Please try again.")
    
    elif search_type == "2":
        #Searching for authors
        print("\tSEARCH BY AUTHOR")

        found = []

        search_author = input("Enter the name of the AUTHOR:")

        for i in range(0, len(author)):
            if search_author.lower() in author[i].lower():
                found.append(i)
            
        if not found:
            #If author(s) were not found
            print(f"Your search for {search_author} was *NOT* FOUND!")
            print(f"Please try again.")
        
        else:
            #author(s) were found
            print(f"Your search for {search_author} was FOUND!")

            for i in range(0, len(found)):
                print(f"{title[found[i]]:30} {author[found[i]]:18} {genre[found[i]]:17} {pages[found[i]]:3}    {status[found[i]]:10}")
    
    elif search_type == "3":
        #Exiting the sequential search
        print("GOODBYE :)")
        answer = "n"
    
    else:
        #In case user inputs wrong number
        print("INVALID INPUT")