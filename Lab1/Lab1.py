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
        response = input(" Would you like to enter another meeting [y or n]")

        return response


#--------MAIN EXECUTING CODE----------------------------------
test = difference(100, 50)
print(test)

response = input(print("Would you like to enter another meeting [y or n]"))
test2 = decision(response)