
#Cory Babich & Austin
#Final Project
#SE126.06
#3-11-2025 [W10D2]

#VARIABLE DICTIONARY

#--IMPORTS---------------------------------------
import random

#--FUNCTIONS-------------------------------------
def updateEnemy(newEnem): #updates current foe states to match the stats of the enemy template it is passed to it.
    currentFoe["name"] = newEnem["name"]
    currentFoe["admiral"] = newEnem["admiral"]
    currentFoe["HP"] = newEnem["HP"]
    currentFoe["HPmax"] = newEnem["HPmax"]
    currentFoe["atc"] = newEnem["atc"]
    currentFoe["def"] = newEnem["def"]
    currentFoe["ability"] = newEnem["ability"]

# Enemy function calls that call ability functions and provide expected variables
def enAttack(): 
    return attack(currentFoe, player)
def enEmp():
    return empAttack(currentFoe, player)
def enDefend():
    return defend(currentFoe)
def enRepair():
    return repair(currentFoe)

#Ability functions that are triggered by player and enemies in combat
def attack(attacker, target):
    damage = attacker["atc"]

    #reduce damage if the target is defending
    if target["isDef"] == True:
        damage = damage/2
    
    #increase damage if the attacker is aiming


    damage = damage - target["def"]

    # If the target's armor reduces the incoming damage to a negative number, it is set to 0.
    if damage < 0:
        damage = 0

    #Print flavor text for notifying the player, change based on if the player is the attack is or not.
    if attacker == player:
        print(f"Hit them with the Ion Cannons. (You deal {damage} damage)")
    else:
        print(f"Their launching missils! (You take {damage} damage)")

    target["HP"] -= damage

def defend(defender):
    defender["isDef"] = True

    #Inform the player if they or the enemy ship took this action, based on the location passed to this function
    if defender == player:
        print(f"Take evasive maneuvers!")
    else:
        print(f"They're trying to dodge our cannons")

def repair(repairer):
    repairNum = (1 + random.randrange(3)) + (1 + random.randrange(3)) # Randomly generates 2 random values ranging from 1 to 4 and adds them together
    
    if repairer["HP"] + repairNum >= repairer["HPmax"]:
        repairer["HP"] = repairer["HPmax"]
        
        if repairer == player:
            print("We're fully repaired Captain!")
        else:
            print("The enemy fully fixed their ship!")
    else:
        repairer["HP"] += repairNum

        if repairer == player:
            print(f"Repairs underway! (You healed {repairNum} HP)")
        else:
            print(f"They're repairing their Ship! (The enemy healed {repairNum} HP)")

def empAttack(attacker, target):
    #Take half the attacker's atc value as the damage value, and if damage is less than the target's def value set damage to 0
    damage = int(attacker["atc"] / 2)
    damage = damage - target["def"]
    if damage < 0:
        damage = 0
    #Reduced the target's HP by the damage value, and set that they are effected by an EMP ("isEMP") to True
    target["HP"] -= damage
    target["isEMP"] = True

    #Inform the player if they or the enemy ship took this action, based on the location passed to this function
    if attacker == player:
        print(f" We've hit them with the EMP Sir! (You deal {damage} damage)")
    else:
        print(f"We've been EMPed! Systems are down temporarily. (You take {damage} damage)")

#Function call to let player choose a ship
def playerSelect(playerShip):
    ans = "y"

    #Display each player ship from left to right, The name of each ship on the top row and their stats below them
    print(f"Ship 1: {'Resolute':12}  Ship 2: {'Triumphant':11}  Ship 3: {'Endurance'}")
    print("-" * 80)
    print(f"        {Resolute['Admiral']:20}  {Triumphant['Admiral']:20} {Endurance['Admiral']}")
    print(f"        {Resolute['General']:20}  {Triumphant['General']:20} {Endurance['General']}")
    print(f"        {Resolute['Commander']:20}  {Triumphant['Commander']:20} {Endurance['Commander']}")
    print(f"        HP: {str(Resolute['HP']):16}  HP: {str(Triumphant['HP']):16} HP: {str(Endurance['HP'])}")
    print(f"        atc: {str(Resolute['atc']):15}  atc: {str(Triumphant['atc']):15} atc: {str(Endurance['atc'])}")
    print(f"        def: {str(Resolute['def']):15}  def: {str(Triumphant['def']):15} def: {str(Endurance['def'])}")
    print(f"        {Resolute['Ability1']:20}  {Triumphant['Ability1']:20} {Endurance['Ability1']}")
    print(f"        {Resolute['Ability2']:20}  {Triumphant['Ability2']:20} {Endurance['Ability2']}")
    print("-" * 80)

    #Input trap start, and ask for which ship the player wants
    while ans == "y":
        ship_select = input("\nWhich ship would you like to select [1, 2, 3]: ")

        #If the player's input is 1 set the reference dictionary "playerShip"'s value equal to dictionary "Resolute"'s values 
        if ship_select == "1" or ship_select.upper() in "RESOLUTE":
            for key in Resolute:
                if key == "Ability1":
                    if Resolute["Ability1"] != "None":
                        playerShip["hasRepair"] = True
                if key == "Ability2":
                    if Resolute["Ability2"] != "None":
                        playerShip["hasEMP"] = True
                else:
                    playerShip[key] = Resolute[key]    

            ans = "n"
        
        #If the player's input is 2 set the reference dictionary "playerShip"'s value equal to dictionary "Triumphant"'s values 
        elif ship_select == "2" or ship_select.upper() in "TRIUMPHANT":
            for key in Triumphant:
                if key == "Ability1":
                    if Triumphant["Ability1"] != "None":
                        playerShip["hasRepair"] = True
                if key == "Ability2":
                    if Triumphant["Ability2"] != "None":
                            playerShip["hasEMP"] = True
                else:
                    playerShip[key] = Triumphant[key]
        
            ans = "n"

        #If the player's input is 3 set the reference dictionary "playerShip"'s value equal to dictionary "Endurance"'s values 
        elif ship_select == "3"or ship_select.upper() in "ENDURANCE":
            for key in Endurance:
                if key == "Ability1":
                    if Endurance["Ability1"] != "None":
                        playerShip["hasRepair"] = True
                if key == "Ability2":
                    if Endurance["Ability2"] != "None":
                        playerShip["hasEMP"] = True
                else:
                    playerShip[key] = Endurance[key]
        
            ans = "n"

        #If the player's input is "FOtR2" set the reference dictionary "playerShip"'s value equal to dictionary "Mandator"'s values
        #The is no obviouse way for the player to know this is an option, this was a cheat code we added for fun.
        elif ship_select.upper() == "FOTR2":
            for key in Mandator:
                if key == "Ability1":
                    if Mandator["Ability1"] != "None":
                        playerShip["hasRepair"] = True
                if key == "Ability2":
                    if Mandator["Ability2"] != "None":
                        playerShip["hasEMP"] = True
                else:
                    playerShip[key] = Mandator[key]
        
            ans = "n"

        #Invalid error Catch
        else:
            print("**ERROR** SHIP NOT FOUND!")
        print("-" * 40)
    

#--MAIN EXECUTING CODE----------------------------------

# Player stats and enemy in focus
player = {
    "name":"SS No Name",
    "General" : "General No Name",
    "General": "Captin No Name",
    "Commander" : "Commander No Name",
    "HPmax":10,
    "HP":10,
    "atc":5,
    "def":5,
    "isDef":False,
    "isEMP":False,
    "hasRepair": False,
    "hasEMP": False
}
currentFoe = {
    "name":"NoFoeShipError",
    "admiral" : "NoFoeAdmiralERROR",
    "HP":0,
    "HPmax":0,
    "atc":0,
    "def":0,
    "isDef":False,
    "isEMP":False, 
    "ability":[]
} # This is blank on compliation so that the enemy templates can fill it when they join the fight
                # Funcations and other processes will only referrence the states of currentFoe

#Player Ships options
Resolute = {
    "name" : "Resolute",
    "Admiral" : "Yularin",
    "General" : "Anakin Skywalker",
    "Commander" : "Rex",
    "HP" : 20,
    "HPmax" : 20,
    "atc" : 14,
    "def" : 4,
    "Ability1" : "Repair",
    "Ability2" : "Emp"
}

Triumphant = {
    "name" : "Triumphant",
    "Admiral" : "Coburn",
    "General" : "Plo Koon",
    "Commander" : "Wolffe",
    "HP" : 18,
    "HPmax" : 18,
    "atc" : 6,
    "def" : 4,
    "Ability1" : "Repair",
    "Ability2" : "None"
}

Endurance = {
    "name" : "Endurance",
    "Admiral" : "Kilian",
    "General" : "Mace Windu",
    "Commander" : "Ponds",
    "HP" : 14,
    "HPmax" : 14,
    "atc" : 8,
    "def" : 2,
    "Ability1" : "None",
    "Ability2" : "Emp"
}

#Secret option for fun
Mandator = {
    "name" : "Mandator",
    "Admiral" : "Thrawn",
    "General" : "Yoda",
    "Commander" : "Gree",
    "HP" : 200,
    "HPmax" : 200,
    "atc" : 100,
    "def" : 25,
    "Ability1" : "Repair",
    "Ability2" : "Emp"
}

# Enemy ship templates

Invincible = {
    "name" : "Invincible",
    "admiral" : "Trench",
    "HP" : 25,
    "HPmax":25,
    "atc" : 12,
    "def" : 6,
    "ability" : [enAttack, enDefend, enEmp]
}
Omni = {
    "name" : "Omni",
    "admiral" : "Kilani",
    "HP" : 20,
    "HPmax":20,
    "atc" : 8,
    "def" : 4,
    "ability" : [enAttack, enDefend, enRepair]
}
Procurer = {
    "name" : "Procurer",
    "admiral" : "Mar Tuuk",
    "HP" : 14,
    "HPmax":14,
    "atc" : 6,
    "def" : 2,
    "ability" : [enAttack, enDefend, enEmp]
}
Malevolence = {
    "name" : "Malevolence",
    "admiral" : "General Grevious",
    "HP" : 100,
    "HPmax":100,
    "atc" : 80,
    "def" : 20,
    "ability" : [enAttack, enDefend, enRepair, enEmp]
}

#Victory condition, if the current enemy is equal to this enemy the plaer has won
victory = {}

# The order in which enemies attack the player
battleOrder = [
    Procurer, Omni,
    Invincible, Malevolence, victory
]

contineuY = "Y"
battleNum = 0

chargeNum = 100
chargeDisplay = "Ready!"
menuInput = 0
additionalAbilities = ""

# Welcome message, and main menu
print("\nWelcome to Star Wars: Battle of the Fleets!")
print("1. Play Game \n2. How to Play \n3. Exit")

while contineuY == "Y":
    menuInput = input("-:")

    #If the player enters 1 at the menu, the game starts.
    if menuInput == "1":
    
        playerSelect(player) #Player ship selection function is called

        updateEnemy(battleOrder[battleNum]) #Sets the stats of currentFoe to the stats of the first enemy in the battle order list
        while contineuY == "Y":
            userInput = ""
            player["isDef"] = False #if the player defended last turn, it is reset at the start of this turn

            #The player's EMP blast has to charge for roughly 4 turns, this is handled here by generating a random number from 1 to 15 plus 23
            #The result is added to --
            if chargeNum < 100:
                chargeNum += 23 + ( 1 + random.randrange(14))
                chargeDisplay = str(chargeNum) + "%"
                if chargeNum >= 100:
                    chargeDisplay = "Ready!"

            #If the player's chosen ship has the repair and or EMP actions those actions should be displayed, 
            additionalAbilities = ""
            if player["hasRepair"] == True:
                additionalAbilities += " [Repair] "
            if player["hasEMP"] == True:
                additionalAbilities += f" [EMP : {chargeDisplay}] "

            #Main interface, Displays enemy ship's (Name, Health, and stats), Player Ship's (Name, Health, and stats), 
            # and expected player input  
            print("\n")
            print(f"Enemy Ship: {currentFoe["name"]:12} | HitPoints :{currentFoe["HP"]:2} , Attack :{currentFoe["atc"]:2} , Armor :{currentFoe["def"]:2}")
            print(f"Your Ship : {player["name"]:12} | HitPoints :{player["HP"]:2} , Attack :{player["atc"]:2} , Armor :{player["def"]:2}")
            print(f"-\nYour actions) [Attack]  [Defend] {additionalAbilities:85} [Exit: Leave game]")
    

            while userInput.upper() == "": #userInput is blank by defeault, but if the user gives an invalid input it will be set back to "" to 
                                   #repeat the prompt until they do. 
                
                if player["isEMP"] == False: # If the player is not effected by an EMP, take the user's input
                    userInput = input("-:")
                else:
                    # While affected by the EMP, the user's turn is skipped. 
                    # This input is used to comminucate that to the player, but any input they give is ignored.
                    input("-: (The EMP disabled the Engines Captain!)") 
                    #The userInput is set to "**" to break the input trap loop          
                    userInput = "**"

                #Player is attacking  
                if userInput.upper() in "ATTACK":
                    attack(player, currentFoe)# the attack function is called, and is passed he player 

                #Player is defending
                elif userInput.upper() in "DEFENCE":
                    player["isDef"] = True

                #Player repairs their ship to regains hit points.
                elif player["hasRepair"] == True and userInput.upper() in "REPAIR":
                    repair(player)

                #If the player's ship has the EMP ability and the user's input is in
                elif player["hasEMP"] == True and userInput.upper() in "EMP":
                    #The player should only be able to use the EMP Ability if it is at full charge (represented by chargeNum)
                    if chargeNum >= 100: 
                        empAttack(player, currentFoe)
                        chargeNum = 0 #After each use, chargeNum is set to 0 and needs to charge (Recharging is handled at the top of the loop) 
                    else:
                        #If chargeNum is less than 100, let the player know they cannot user this ability
                        print("Captain, the EMP is still charging. Try Something Else.")
                        userInput = "" #The userInput is set to "" so that the input trap will let the user choose a new action
                
                #The player can leave the game during combat by entering EXIT
                elif userInput.upper() in "EXIT":
                    contineuY = "N" # Main loop is set to end

                #All other inputs that are not produced by the isEMP check ("**"), are caught here and the user is informed of Invald input
                elif userInput != "**":
                    print("*** Invalid Input ***")
                    userInput = ""

            player["isEMP"] = False # If the player was hit by an EMP last turn, the EMP Status ends here.
            currentFoe["isDef"] = False #if the enemy defended last turn, it is reset after the player's action but before it takes a turn.
    
            if currentFoe["isEMP"] == False: #if the enemy is not under the effects of an EMP they take their turn.
                currentFoe["ability"][random.randrange(len(currentFoe["ability"]))]()
                # ^ This is the weirdedest line of code I've ever written, so below it is a break down.  
                '''
                                                                                   () "The rest of the line determines the function location, these parentheses"
                currentfoe["ability"]                                                 "references the ability list, in the currentfoe dictionary"
                                     [                                            ]   "indicates the position of the ability list needed."
                                      random.randrange(                          )    "Returns a random number from 0 to the number given"
                                                       len(currentFoe["ability"])     "returns the length of the ability list"
                '''
            else:
                currentFoe["isEMP"] = False
                print("They're stunned by the EMP, Sir!")

            #If the enemy ship's hp is 0, alert the player and let them know a new ship will be loaded in.
            if currentFoe["HP"] <= 0:
                print("\n!!! Ship Destroyed Captain !!!")
                print("But a new enemy approaches")
                #This input does not accept any value, but is used to pause the game so the user can read the text above, before continueing.
                input("\n(Press any button to continue)") 

                #Heal the player to full health
                player["HP"] = player["HPmax"]

                #increase the fight indicator by one and redefine the currentFoe accordingly, unless the enemy is "Victory" 
                #If the next enemy is vitory inform the player they have won the game
                battleNum += 1
                if battleOrder[battleNum] != victory:
                    updateEnemy(battleOrder[battleNum])
                else:
                    #Let the player know they won, before asking them if they would like to play again
                    print("\n\n\t\t!!!!! YOU WIN !!!!!!\n\n")
                    input("(press any button to continue)")

                    print("Do you want to play again? [Y/N]")
                    winInput = input("-:")
                    
                    #Input trap to ensure an input of "Y" or "N"
                    while winInput.upper() != "Y" and winInput.upper() != "N":
                        print("** Invalid Input **")
                        print("Please enter 'Y' for Yes or 'N' for No")
                        winInput = input("-:")

                    #If input is "Y", reset the battle order, player HP, EMP charge values, and let the player choose a new ship
                    if winInput.upper() == "Y":
                        playerSelect(player) #Player ship selection function is called
                        chargeNum = 100
                        player["HP"] = player["HPmax"]
                        battleNum = 0
                        updateEnemy(battleOrder[battleNum])

                    else:
                        #If input not "Y", set the main loop to end
                        contineuY = "N"

            #If the player's HP is equal to 0 or less, inform the player that they have lost, and ask if they want to play again
            elif player["HP"] <= 0:
                print("\n\n\t\t      Your Ship was Destroyed   :( \n\n")
                print("Do you want to play again? [Y/N]")
                winInput = input("-:")
                
                #Input trap to ensure an input of "Y" or "N"
                while winInput.upper() != "Y" and winInput.upper() != "N":
                    print("** Invalid Input **")
                    print("Please enter 'Y' for Yes or 'N' for No")
                    winInput = input("-:")

                #If input is "Y", reset the battle order, player HP, EMP charge values, and let the player choose a new ship
                if winInput.upper() == "Y":
                    playerSelect(player) #Player ship selection function is called
                    chargeNum = 100
                    player["HP"] = player["HPmax"]
                    battleNum = 0
                    updateEnemy(battleOrder[battleNum])

                else:
                    #If input not "Y", set the loop to end
                    contineuY = "N"
    
    #If the player enters 2 at the main menu, 
    elif menuInput == "2":
        print("\nThis game plays as a turn based combat, each turn the player enters in one of the following commands:\n")
        print("[Attack]  : Deal damage to the enemy equal to your Attack value minus their Armor value")
        print("[Defence] : Reduce the damage dealt by enemy's next attack by half")
        print("[Repair]  : Regain 2 to 8 hit points")
        print("[EMP]     : The enemy's next turn is skipped")
        print("\n Type [Exit] during combat to leave the game.\n")

        input() #small pause to give the user time to read the above text
        print("\nWelcome to Star Wars: Battle of the Fleets!")
        print("1. Play Game \n2. How to Play \n3. Exit")

    elif menuInput == "3": #Player leaves the game, set ContineuY to any value that is not "Y" to end the loop.
        contineuY = "N"
    else: 
        print("**INVALID INPUT**")
        print(f"{menuInput} is not a valid choice. Please enter an input of [1,2, or 3]")
   
print("\nGoodbye, and have a good day.\n")
