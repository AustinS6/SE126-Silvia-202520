#Austin Silvia
#
#SE126.02


#--------FUNCTIONS--------------------------------------------
def difference(people, max_cap):
    diff = max_cap - people

    return diff

def decision(response):
    while response != "y" and response != "n":
        print("***INVALID ENTRY!***")
        response = input(" Would you like to enter another meeting [y or n]: ")

        return response


#--------MAIN EXECUTING CODE----------------------------------
response = "y"

while response == "y":
    meetingName = input("What is the name of the meeting: ")
    
    max_cap = int(input("What is the meeting room capacity: "))
    
    people = int(input("How many people are attending this meeting: "))
    
    diffy = difference(people, max_cap)
    
    if diffy > 0:
        print("Not enough people attending the meeting")
        
        print(abs(diffy), "people should be added to the meeting")

        addyadd = int(input("How many people would you like to add to the meeting: "))

        addyadd = diffy + addyadd

    if diffy < 0:
        print("!MEETING DOES NOT MEET FIRE SAFETY. PLEASE REMOVE PEOPLE FROM MEETING!")
        
        print(abs(diffy), "people should be removed from the meeting")

        byebye = int(input("How many people would you like to remove from the meeting: "))

        diffy = diffy + byebye
        
    response = input("Would you like to enter another meeting [y or n]: ").lower()
    
    test2 = decision(response)

print("Goodbye! :)")