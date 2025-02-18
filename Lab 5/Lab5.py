#Austin Silvia
#2/10/2025
#
#Build a personal library search system using the file book_list.csv. It is set up as follows:
#Field  File Data
#0      Library Number (unique)
#1      Title
#2      Author
#3      Genre
#4      Page Count
#5      Status: Available/On Loan
#
#Store the file data into 1D parallel lists, then use the appropriate searching algorithms for the menu system options.
#Your program should give your user the following menu:
#Personal Library Menu
#1. Show All Titles – list all book data to the user alphabetically by title
#2. Search by Title – allow for an entire title or a title key word
#3. Search by Author – show all titles of the searched-for author
#4. Search by Genre - show all titles of the searched-for genre
#5. Search by Library Number – only allow for one specific library number item
#6. Show All Available – show all titles with status “available”
#7. Show All On Loan - show all titles with status “on loan”
#8. EXIT
#
#When your user runs any of the options 1 – 7, show all data associated with the search [Library Number, Title, Author, Genre, Page count, Status]. Do not allow the program to end unless the user chooses option 8 to exit. All searches should not be case sensitive.

#--IMPORTS-----------------------------------------------------------------------------
import csv

#--FUNCTIONS---------------------------------------------------------------------------
def display(x, foundList, records):
    
    print(f"{'LIB NUM':8} {'TITLE':35} {'AUTHOR':25} {'GENRE':16} {'PAGES':4} {'status'}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if x != "x":
        print(f"{library_num[x]:8} {title[x]:35} {author[x]:25} {genre[x]:16} {pages[x]:4} {status[x]}")

    elif foundList:
        for i in range(0, records):
            print(f"{library_num[foundList[i]]:8} {title[foundList[i]]:35} {author[foundList[i]]:25} {genre[foundList[i]]:16} {pages[foundList[i]]:4} {status[foundList[i]]}")

    else:
        for i in range(0, records):
            print(f"{library_num[i]:8} {title[i]:35} {author[i]:25} {genre[i]:16} {pages[i]:4} {status[i]}")
    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

def swap(i, listName):
    temp = listName[i]
    listName[i] = listName[i + 1]
    listName[i + 1] = temp

#--MAIN EXECUTION CODE-----------------------------------------------------------------
library_num = []
title = []
author = []
genre = []
pages = []
status = []

with open("Text_Files/book_list.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        library_num.append(rec[0])
        title.append(rec[1])
        author.append(rec[2])
        genre.append(rec[3])
        pages.append(rec[4])
        status.append(rec[5])

ans = input("Would you like to enter your Personal Library Menu? [y/n]: ").lower()

while ans != "y" and ans != "n":
    print("***INVALID ENTRY!***")
    ans = input("Would you like to enter your Personal Library Menu? [y/n]").lower()

while ans == "y":
    print("\tSEARCHING MENU")
    print("1. Show all Titles - In Alphabetical order")
    print("2. Search by TITLE")
    print("3. Search by AUTHOR")
    print("4. Search by GENRE")
    print("5. Search by Library Number")
    print("6. Show all Available")
    print("7. Show all On Loan")
    print("8. EXIT")

    search_type = input("\nWhich data would you like to access? [1-8]: ")

    if search_type not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("***INVALID ENTRY!***\nPlease try again")
    
    elif search_type == "1":
        print(f"You have chosen to Show all Titles")

        for i in range(0, len(title) - 1):
            
            for index in range(0, len(title) - 1):
                if title[index] > title[index + 1]:
                    swap(index, title)
                    swap(index, library_num)
                    swap(index, author)
                    swap(index, genre)
                    swap(index, pages)
                    swap(index, status)
        
        #print(f"{'TITLE'}")
        #print("------------")
        #print(f"{title[]}")
        #print("------------")
        display("x", 0, len(title))
    
    elif search_type == "2":
        print(f"You have chosen to Search by TITLE")

        for i in range(0, len(title) - 1):
            
            for index in range(0, len(title) - 1):
                if title[index] > title[index + 1]:
                    swap(index, title)
                    swap(index, library_num)
                    swap(index, author)
                    swap(index, genre)
                    swap(index, pages)
                    swap(index, status)

        min = 0
        max = len(title)
        mid = int((min + max) / 2)

        search = input("Enter the TITLE you wish to search for: ")

        while min < max and search.lower() not in title[mid].lower():
            if search.lower() < title[mid].lower():
                max = min - 1
            
            else:
                max = min + 1
            mid = int((min + max) / 2)

            if search.lower() in title[mid].lower():
                print(f"Your search for {search} is complete, see below details: ")
                print(f"{'LIB NUM':8} {'TITLE':35} {'AUTHOR':25} {'GENRE':16} {'PAGES':4} {'status'}")
                print("----------------------------------------------------------------------------------------------------------------")
                print(f"{library_num[mid]:8} {title[mid]:35} {author[mid]:25} {genre[mid]:16} {pages[mid]:4} {status[mid]}")
                print("----------------------------------------------------------------------------------------------------------------")

            else:
                print(f"Your search for {search} is complete, and no information was found. ")

    elif search_type == "3":
        print(f"You have chosen to Show all Authors")

        for i in range(0, len(title) - 1):
            
            for index in range(0, len(title) - 1):
                if title[index] > title[index + 1]:
                    swap(index, title)
                    swap(index, library_num)
                    swap(index, author)
                    swap(index, genre)
                    swap(index, pages)
                    swap(index, status)

        found = -1
        
        search_author = input("Enter the name of the Author you wish to search for: ")

        for i in range(0, len(author)):
            if search_author.lower() in author[i].lower():
                found = i
            
        if found != - 1:    
            print(f"Your search for {search_author} was found!")
            print(f"{library_num[found]:8} {title[found]:35} {author[found]:25} {genre[found]:16} {pages[found]:4} {status[found]}")
        
        else:
            print(f"your search for {search_author} was NOT found! :(")


    elif search_type == "4":
        print(f"You have chosen to Show all Titles")
    
    elif search_type == "5":
        print(f"You have chosen to Show all Titles")

    elif search_type == "6":
        print(f"You have chosen to Show all Titles")

    elif search_type == "7":
        print(f"You have chosen to Show all Titles")

    elif search_type == "8":
        print("GOODBYE, Have a Great Day :)")
        ans = "n"