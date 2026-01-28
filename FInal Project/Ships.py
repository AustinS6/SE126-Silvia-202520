def enAttack():
    print()
def enDefend():
    print()
def enRepair():
    print()
def enEmp():
    print()

#Player Ship Options:
Resolute = {
    "Admiral" : "Yularin",
    "General" : "Anakin Skywalker",
    "Commander" : "Rex",
    "HP" : 20,
    "atc" : 14,
    "def" : 4,
    "Ability1" : "Repair",
    "Ability2" : "Emp"
}

Triumphant = {
    "Admiral" : "Coburn",
    "General" : "Plo Koon",
    "Commander" : "Wolffe",
    "HP" : 18,
    "atc" : 6,
    "def" : 4,
    "Ability1" : "Repair",
    "Ability2" : "None"
}

Endurance = {
    "Admiral" : "Kilian",
    "General" : "Mace Windu",
    "Commander" : "Ponds",
    "HP" : 14,
    "atc" : 8,
    "def" : 2,
    "Ability1" : "None",
    "Ability2" : "Emp"
}

#Secret Ship for player: Password FOTR2
Mandator = {
    "Admiral" : "Thrawn",
    "General" : "Yoda",
    "Commander" : "Gree",
    "HP" : 200,
    "atc" : 100,
    "def" : 25,
    "Ability1" : "Repair",
    "Ability2" : "Emp"
}

#Enemy Ships:
Invincible = {
    "Admiral" : "Trench",
    "HP" : 25,
    "atc" : 12,
    "def" : 6,
    "Ability" : [enAttack, enDefend, enEmp]
}

Omni = {
    "Admiral" : "Kilani",
    "HP" : 20,
    "atc" : 8,
    "def" : 4,
    "Ability" : [enAttack, enDefend, enRepair]
}

Procurer = {
    "Admiral" : "Mar Tuuk",
    "HP" : 14,
    "atc" : 6,
    "def" : 2,
    "Ability" : [enAttack, enDefend, enEmp]
}

Malevolence = {
    "Admiral" : "General Grevious",
    "HP" : 100,
    "atc" : 80,
    "def" : 20,
    "Ability" : [enAttack, enDefend, enRepair, enEmp]
}

main_menu = "y"

while main_menu == "y":
    print("\tStar Wars: Battle of the Fleets")
    print("1. Start Game")
    print("2. How to Play")
    print("3. EXIT")

    menu_select = input("Choose an option [1, 2, 3]: ")

    if menu_select == "1":
        ans = "y"

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

        while ans == "y":
            ship_select = input("\nWhich ship would you like to select [1, 2, 3]: ")

            if ship_select == "1":
                player_ship = {
                    "Admiral" : "Yularin",
                    "General" : "Anakin Skywalker",
                    "Captain" : "Rex",
                    "HP" : 20,
                    "atc" : 10,
                    "def" : 8,
                    "Ability1" : "enRepair",
                    "Ability2" : "enEmp"
                }
        
                ans = "n"
                main_menu = "n"

            elif ship_select == "2":
                player_ship = {
                    "Admiral" : "Coburn",
                    "General" : "Plo Koon",
                    "Commander" : "Wolffe",
                    "HP" : 16,
                    "atc" : 4,
                    "def" : 4,
                    "Ability1" : "enRepair"
                }

                ans = "n"
                main_menu = "n"

            elif ship_select == "3":
                player_ship = {
                    "Admiral" : "Kilian",
                    "General" : "Mace Windu",
                    "Commander" : "Ponds",
                    "HP" : 14,
                    "atc" : 4,
                    "def" : 2,
                    "Ability1" : "enEmp"
                }

                ans = "n"
                main_menu = "n"

            elif ship_select == "FOTR2":
                player_ship = {
                    "Admiral" : "Thrawn",
                    "HP" : 200,
                    "atc" : 100,
                    "def" : 50,
                    "Ability1" : "enRepair",
                    "Ability2" : "enEmp"
                }

                ans = "n"
                main_menu = "n"

            else:
                print("**ERROR** SHIP NOT FOUND!")
            print("-" * 40)
            for key in player_ship:
                print(f"{key:8} {player_ship[key]}")
            print("-" * 40)
    
    elif menu_select == "2":
        print("How to play:")

    elif menu_select == "3":
        main_menu = "n"

    else:
        print("**ERROR** INVALID INPUT")