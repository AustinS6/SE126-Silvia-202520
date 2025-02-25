#Lab 7 - Austin Silvia 2/25/25

#Build a mini programming dictionary a user can search through and ad to using the words.csv file:

#Access the words.csv file and store the data to a dictionary, where each word in the file is a key of the dictionary and the value stored to each key is the word’s corresponding definition. Then, create a repeatable program that allows a user to interact with the dictionary based on the following menu:
#My Programming Dictionary Menu
#1. Show all words – Show all words stored to the dictionary
#2. Search for a word – Allow the user to enter a word and if it is in the dictionary, show its definition (tell the user if the word is not in the dictionary)
#3. Add a word – Allow a user to add a word to the dictionary if it does not already exist
#4. EXIT

#The program should not be case sensitive for user input, and the user should only be able to quit when they have selected menu option number 4.

#Bonus #1 [+5]: When the user is finished using the program, create a new file called updated_words.csv which contains the entire dictionary (including any new words added during the session) and follows the original words.csv field structure (first field is the word, second field is the definition).

#Bonus #2 [+10]: Add a menu option “3.5” which will show all of the words in the dictionary, ordered alphabetically in ascending order (A -> Z)

#--IMPORTS-----------------------------------------------------------------------------
import csv

#--FUNCTIONS---------------------------------------------------------------------------


#--MAIN EXECUTION CODE-----------------------------------------------------------------
word = {}

with open("Text_Files/words.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file:
        word.update({rec[0] : rec[1]})

ans = "y"

while ans == "y":
    print("My Programming dictionary Menu:")
    print("1. Show all words")
    print("2. Search for a word")
    print("3. Add a word")
    print("4. EXIT")
    
    search = input("Which would you like to search for? [1, 2, 3, 4]: ")

    if search == "1":
        print("You have chosen to SHOW ALL WORDS:")
        print(f"{'WORD':16} {'DEFINITION'}")
        print("-" * 200)
        for key in word:
            print(f"{key:16} {word[key]}")
        print("-" * 200)

    if search == "2":
        print("You have chosen to search for a WORD:")
        word_search = input("Which word would you like to search for?: ")
        found = 0
        for key in word:
            if word_search.lower() == key.lower():
                found = key
        
        if found != 0:
            print(f"Your search for {word_search} is complete: ")
            print(f"{'WORD':16} {'DEFINITION'}")
            print("-" * 200)
            print(f"{found:16} {word[found]}")
            print("-" * 200)
        else:
            print(f"Your search for {word_search} is complete, and nothing was found!")

    if search == "3":
        print("You have chosen to add a WORD")

        add_word = input("What word would you like to add?: ")
        add_definition = input("What is the definition of the word you have added?: ")
        word.update({add_word : add_definition})

        print(f"{'WORD':16} {'DEFINITION'}")
        print("-" * 200)
        for key in word:

            print(f"{key:16} {word[key]}")
        print("-" * 200)

    if search == "4":
        print("Goodbye :)")
        ans = "n"