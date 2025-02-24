#Lab 6 - Austin Silvia 2/24/25

#Write a Python program using lists (1D or 2D) to assign passengers seats in an airplane. Assume a small airplane with seat numbering as follows.

#Row
#1 A B C D
#2 A B C D
#3 A B C D
#4 A B C D
#5 A B C D
#6 A B C D
#7 A B C D
#The program should display the seat pattern, with an ‘X’ making the seats already assigned. For example, after seats 1A, 2B and 4C are taken the display should look like this:
#Row
#1 X B C D
#2 A X C D
#3 A B C D
#4 A B X D
#5 A B C D
#6 A B C D
#7 A B C D
#After displaying the seats available, the program prompts for the seat desired, the user types in a seat and then the display of available seats is updated. This continues until all seats are filled or until the user signals that the program should end. If a user types in a seat that is already assigned, the program should say that the seat is occupied and ask for another choice.
#• You must use a function to display the seating map
#• You must use a function that asks the user in they want to continue reserving seats or stop. The function should only accept an uppercase or lowercase ‘y’ or ‘n’.

#--IMPORTS-----------------------------------------------------------------------------


#--FUNCTIONS---------------------------------------------------------------------------
def seating():
    for i in range(0, len(row)):
        print(f"{row[i][0]} {row[i][1]} {row[i][2]} {row[i][3]} {row[i][4]}")

def taken(rec, field):
    if row[rec][field] == "X":
            print("Seat has already been taken, please choose another")
            return 1
    else:
          return 2

#--MAIN EXECUTION CODE-----------------------------------------------------------------

row =[
    ["1", "A", "B", "C", "D"],
    ["2", "A", "B", "C", "D"],
    ["3", "A", "B", "C", "D"],
    ["4", "A", "B", "C", "D"],
    ["5", "A", "B", "C", "D"],
    ["6", "A", "B", "C", "D"],
    ["7", "A", "B", "C", "D"]
]

print("Row")

seating()

pick_seat = input("Would you like to choose a seat [y/n]")

while pick_seat.lower() == "y":
    row_choice = input("Which row would you like to sit in [1, 2, 3, 4, 5, 6, 7]: ")

    if row_choice != "1" and row_choice != "2" and row_choice != "3" and row_choice != "4" and row_choice != "5" and row_choice != "6" and row_choice != "7":
         print("!!ERROR!! INVALID INPUT")

    else:
        seat = input("Which seat would you like to sit in [A, B, C, D]: ")

        if seat.upper() == "A":
            ans = taken(int(row_choice) - 1, 1)
            if ans != 1:
                row[int(row_choice) - 1][1] = "X"
                seating()
    
        if seat.upper() == "B":
            ans = taken(int(row_choice) - 1, 2)
            if ans != 2:
                row[int(row_choice) - 1][2] = "X"
                seating()
    
        if seat.upper() == "C":
            ans = taken(int(row_choice) - 1, 3)
            if ans != 3:
                row[int(row_choice) - 1][3] = "X"
                seating()
    
        if seat.upper() == "D":
            ans = taken(int(row_choice) - 1, 4)
            if ans != 4:
                row[int(row_choice) - 1][4] = "X"
                seating()
        
    pick_seat = input("Do you want to continue picking a seat? [y/n]: ")
print("Thank you for choosing Janky Airlines! :)")