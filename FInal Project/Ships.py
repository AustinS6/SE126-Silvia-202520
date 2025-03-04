#Player Ship Options:
Resolute = {
    "Admiral" : "Yularin",
    "General" : "Anakin Skywalker",
    "Captain" : "Rex",
    "HP" : 20,
    "atc" : 10,
    "def" : 8
}

Triumphant = {
    "Admiral" : "Coburn",
    "General" : "Plo Koon",
    "Commander" : "Wolffe",
    "HP" : 16,
    "atc" : 4,
    "def" : 4
}

Endurance = {
    "Admiral" : "Kilian",
    "General" : "Mace Windu",
    "Commander" : "Ponds",
    "HP" : 14,
    "atc" : 4,
    "def" : 2
}

#Secret Ship for player: Password FOTR2
Mandator = {
    "Admiral" : "Thrawn",
    "HP" : 200,
    "atc" : 100,
    "def" : 50
}

#Enemy Ships:
Invincible = {
    "Admiral" : "Trench",
    "HP" : 25,
    "atc" : 12,
    "def" : 12
}

Omni = {
    "Admiral" : "Kilani",
    "HP" : 20,
    "atc" : 8,
    "def" : 8
}

Procurer = {
    "Admiral" : "Mar Tuuk",
    "HP" : 14,
    "atc" : 6,
    "def" : 2
}

Malevolence = {
    "General" : "Grevious",
    "HP" : 100,
    "atc" : 80,
    "def" : 40
}

print(f"Ship 1: {'Resolute':12}  Ship 2: {'Triumphant':11}  Ship 3: {'Endurance'}")
print("-" * 80)
print(f"        {Resolute['Admiral']:20}  {Triumphant['Admiral']:20} {Endurance['Admiral']}")
print(f"        {Resolute['General']:20}  {Triumphant['General']:20} {Endurance['General']}")
print(f"        {Resolute['Captain']:20}  {Triumphant['Commander']:20} {Endurance['Commander']}")
print(f"        HP: {str(Resolute['HP']):16}  HP: {str(Triumphant['HP']):16} HP: {str(Endurance['HP'])}")
print(f"        atc: {str(Resolute['atc']):15}  atc: {str(Triumphant['atc']):15} atc: {str(Endurance['atc'])}")
print(f"        def: {str(Resolute['def']):15}  def: {str(Triumphant['def']):15} def: {str(Endurance['def'])}")
print("-" * 80)

ans = "y"

while ans == "y":
    ship_select = input("\nWhich ship would you like to select [1, 2, 3]: ")

    print(ship_select)

    if ship_select == "1":
        player_ship = {
            "Admiral" : "Yularin",
            "General" : "Anakin Skywalker",
            "Captain" : "Rex",
            "HP" : 20,
            "atc" : 10,
            "def" : 8
        }
        
        ans = "n"

    elif ship_select == "2":
        player_ship = {
            "Admiral" : "Coburn",
            "General" : "Plo Koon",
            "Commander" : "Wolffe",
            "HP" : 16,
            "atc" : 4,
            "def" : 4
        }

        ans = "n"

    elif ship_select == "3":
        player_ship = {
            "Admiral" : "Kilian",
            "General" : "Mace Windu",
            "Commander" : "Ponds",
            "HP" : 14,
            "atc" : 4,
            "def" : 2
        }

        ans = "n"

    elif ship_select == "FOTR2":
        player_ship = {
            "Admiral" : "Thrawn",
            "HP" : 200,
            "atc" : 100,
            "def" : 50
        }

        ans = "n"

    else:
        print("**ERROR** SHIP NOT FOUND!")

print(player_ship)