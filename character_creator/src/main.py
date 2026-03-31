# LD, LV, & TE First gorup Project
import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_print(string, delay = 0.08):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

classes = { 
1 : {"Name": "Fighter", "Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},
2 : {"Name": "Rogue", "Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},
3 : {"Name": "Cleric", "Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}}

characters = []

def menu():
    clear_screen()
    while True:
        print("Main Menu")
        print("1. View Character")
        print("2. Create Character")
        print("3. Edit Character")
        print("4. Exit")
        menu_option = input("Select an option (1-4): ")
        if menu_option == "1":
            view_character()
        elif menu_option == "2":
            create_character()
        elif menu_option == "3":
            edit_character()
        elif menu_option == "4":
            type_print("Thank you for using our character editor!\n\n\nCredits:\nTrue: Team Leader\nLizzie: Lead Programmer\nLucci: UX/UI Designer\n\n- 'Main Menu' built by Lucci\n- 'Building a Character' built by True\n- 'Character Level Up Check' built by Lucci\n- 'Finding a Character' built by Lizzie\n- 'Viewing/Editing a Character' built by Lizzie\n")
            exit()
        else:
            print("Invalid option. Please try again.")
            continue

def create_character():
    #Ask if user wants to create another character
    def another_character():
        while True:
            another = input("Do you want to create another character? (yes/no): ").strip()
            if another.lower() != 'yes':
                menu()
                break
            else:
                clear_screen()
                create_character()

    #For each class in class options
    print(f"\nCreate Character\n1. Fighter Stats: Strength {classes[1]['Stats']['Strength']}, Health {classes[1]['Stats']['Health']}, Wisdom {classes[1]['Stats']['Wisdom']}")
    print(f"\n2. Rogue Stats: Strength {classes[2]['Stats']['Strength']}, Health {classes[2]['Stats']['Health']}, Wisdom {classes[2]['Stats']['Wisdom']}")
    print(f"\n3. Cleric Stats: Strength {classes[3]['Stats']['Strength']}, Health {classes[3]['Stats']['Health']}, Wisdom {classes[3]['Stats']['Wisdom']}\n")

    #Try and except
    try:
    #Class is set to input type 1-3 to choose your class
        c_class = int(input("Enter the number of your class choice: "))
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your class choice.")
        return

    #If choice is invalid, stop function
    if c_class not in classes:
        print("Invalid class choice.")
        return       

    #Get select class data
    base_class = classes[c_class]
    #Copy base stats so originial class stats are not changed
    character = { "Class": base_class["Name"], "Stats": base_class["Stats"].copy(), "Weapon": None, "Inventory": [] }
    #Inform user about random stats
    type_print("You have two empty stats.\n")
    print("Rolling for your stats...")  
    time.sleep(0.5)
    #generator random stats
    character["Stats"]["Dexterity"] = random.randint(10, 30)
    character["Stats"]["Intelligence"] = random.randint(10, 30)
    #Display rolled stats
    type_print(f"Your rolled stats are: Dexterity: {character['Stats']['Dexterity']}, Intelligence: {character['Stats']['Intelligence']}\n")
    #Ask user to choose a weapon
    print("Choose your weapon from the following options:")
    #For i in weapons
    for i, weapon in enumerate(base_class["Weapons"], 1):
        #Print weapon options
        print(f"{i}: {weapon}")
        #Try and accept weapon choice
    try:
        weapon_choice = int(input("Enter the number of your weapon choice: "))
        #If weapon choice is valid, set weapon
        if 1 <= weapon_choice <= len(base_class["Weapons"]):
            #Set character weapon
            character["Weapon"] = base_class["Weapons"][weapon_choice - 1]
            #Else invalid weapon choice
        else:
            print("Invalid weapon choice.")
            return
        #Catch value error
    except ValueError:
        print("Invalid input. Please enter a number corresponding to your weapon choice. Trying again")
        clear_screen()
        create_character()
    #Add xp and level to char dict.
    character["XP"] = 0
    character["Level"] = 1
    #Name character
    character["Name"] = input("Enter your character's name: ").title().strip()
    #Finish character creation
    characters.append(character)
    type_print(f"Character created:\nName: {character['Name']}\n Class: {character['Class']}\nStats:\n Strength: {character['Stats']['Strength']}\n Health: {character['Stats']['Health']}\n Wisdom: {character['Stats']['Wisdom']}\n Dexterity: {character['Stats']['Dexterity']}\n Intelligence: {character['Stats']['Intelligence']}\nXP: {character['XP']}\nLevel: {character['Level']}\nWeapon: {character['Weapon']}\n")
    another_character()


def level_up_loop(character):
    """
    Checks if the character has enough XP to level up.
    Rogue needs 15 XP per level.
    Cleric needs 20 XP per level.
    """
    if character['Class'] == 'Rogue' or character['Class'] == "Fighter":
        xp_needed = character['Level'] * 15
    else:
        xp_needed = character['Level'] * 20

    if character['XP'] >= xp_needed:
        character['XP'] -= xp_needed
        character['Level'] += 1
        character['Stats']['Strength'] += 1
        print(f"{character['Name']} leveled up to level {character['Level']}!")

    if character['Class'] == 'Cleric' and character['Level'] % 5 == 0:
        character['Spell_slots'] += 1
        print("You gained an extra spell slot!")


def find_character(furture_action):
    global characters
    while True:
        type_print(f"How would you like to find your character for {furture_action}\n1) Name\n2) Class\n3) Level\n")
        find = input("Type the number corresponding to your action\n").strip()
        if find == "1":
            name = input("Enter the name of the character you want to find\n").strip().lower()
            type_print(f"\nCharacters with '{name}' in thier name:\n")
            for character in characters:
                if name in character["Name"].lower():
                    print(f"{character["Name"]}")
            print() # Make empty line
            break
        elif find == "2":
            class_name = input("Enter the class name of the character you want to find\n").strip().title()
            type_print(f"\nCharacters with '{class_name}' as their class:\n")
            for character in characters:
                if class_name == character["Class"]:
                    print(f"{character["Name"]}: {character["Class"]}")
            print() # Make empty line
            break
        elif find == "3":
            level = input("Enter the level for the character you want to find\n").strip()
            type_print(f"\nCharacters whose level is '{level}':\n")
            for character in characters:
                if int(level) == character["Level"]:
                    print(f"{character["Name"]}: Level {character["Level"]}")
            print() # Make empty line
            break
        else:
            type_print("Invalid input. Please Try again\n")
            continue

def view_character():
    global characters
    if not characters:
        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
        menu()
    type_print("First,\n")
    find_character("viewing")
    while True:
        character = input("Type the NAME of the character you wish to view\nIF no character's show up, type 'Leave' to try again\n").strip().title()
        if character == "Leave":
            view_character()
        for chara in characters:
            if character == chara["Name"]:
                type_print(f"\nViewing Character:\nName: {chara['Name']}\n Class: {chara['Class']}\nStats:\n Strength: {chara['Stats']['Strength']}\n Health: {chara['Stats']['Health']}\n Wisdom: {chara['Stats']['Wisdom']}\n Dexterity: {chara['Stats']['Dexterity']}\n Intelligence: {chara['Stats']['Intelligence']}\nLevel: {chara['Level']}\nXP: {chara['XP']}\nWeapon: {chara['Weapon']}\nInventory:\n - {chara["Inventory"]}\n")
                time.sleep(2)
                type_print("Would you like to\n1) View another character\nor\n2) Go back to main menu\n")
                again = input("Type the number for the action you would like to do\n")
                if again == "1":
                    view_character()
                    break
                else:
                    type_print("Redirecting to main menu . . .\n")
                    time.sleep(0.5)
                    menu()
                    break
        else:
            print("Could not find the character you typed in. Try again")
            continue

def edit_character():
    def edit_XP():
        # Helper to add/remove. Have user type in number to add/remove. Update XP
        adding = adding_removing("XP")
        if adding == "ADDING":
            while True:
                type_print("How much XP would you like to add to your character?\n")
                add = input("This needs to be a whole number\n").strip().upper()
                if check_valid_num(add) == True:
                    return int(add)
                else:
                    continue
        else:
            while True:
                type_print("How much XP would you like to remove from your character?\n")
                remove = input("This needs to be a whole number\n").strip().upper()
                if check_valid_num(remove) == True:
                    return int(remove)
                else:
                    continue

    def edit_stat():
        # Have user select stat to reroll. Reroll with random number and save it
        while True:
            # i need to display the list of stats and have the user pick the stat. I will choose a random number between 10 and 30 and return the stat picked AND the new value
            type_print("Which stat would you like to reroll:\nStrength\nWisdom\nDexterity\nIntelligence\n")
            choice = input("Type the NAME of the stat you would like to reroll\n").strip().title()
            if choice == "Strength":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Wisdom":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Dexterity":
                new_value = random.randint(10, 30)
                return choice, new_value
            elif choice == "Intelligence":
                new_value = random.randint(10, 30)
                return choice, new_value
            else:
                print("Invalid input. Check your spelling and try again")
                continue

    def edit_inventory():
        # Use helper to know if adding or removing. Have user type in something to add\remove to inventory list
        adding = adding_removing("inventory")
        if adding == "ADDING":
            while True:
                add = input("What would you like to add to your character's inventory\n").strip().title()
                chara["Inventory"].append(add)
                type_print(f"Added {add} to {chara['Name']}'s inventory\n")
                again = input("Would you like to add another item (yes/no)\n").strip().lower()
                if again != "yes":
                    # user said no or gave invalid input
                    break
                else:
                    continue
        else:
            while True:
                remove = input("What would you like to remove from your character's inventory\n").strip().title()
                if remove in character["Inventory"]:
                    chara["Inventory"].remove(remove)
                    type_print(f"Removed {remove} from {chara['Name']}'s inventory\n")
                    time.sleep(2)
                    clear_screen()
                    edit_character()
                else:
                    type_print(f"{remove} is not in {chara['Name']}'s inventory\n")
                    continue

    def adding_removing(thing):
        # Helper function that will ask the user if they are adding or removing
        while True:
            type_print(f"Are you adding to {thing} or removing from {thing}\n")
            a_r = input("Enter 'ADDING' if adding or 'REMOVING' if removing\n").strip().upper()
            if a_r == "ADDING":
                return "ADDING"
            elif a_r == "REMOVING":
                return "REMOVING"
            else:
                print("Invalid input. Please try again")
                continue
    
    def check_valid_num(num):
        if num.isdigit() == True:
            if int(num) % 1 == 0:
                # User gave a valid number
                return True
            else:
                print("You seemed to have entered a number, but it's not a whole number. Try again")
        else:
            print("You seemed to have entered something other than a number. Try again")

    global characters
    if not characters:
        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
        # Call main menu
    type_print("First,\n")
    find_character("editing")
    while True:
        character = input("Type the name of the character you wish to edit\nIF no character's show up, type 'Leave' to try again\n").strip().title()
        for chara in characters:
            if character == chara["Name"]:
                while True:
                    type_print(f"What would you like to edit on {character}:\n1) XP amount\n2) Reroll a stat\n3) Adjust {character}'s Inventory\n")
                    choice = input("Enter the number correspondng to what you want to edit\n")
                    if choice == "1":
                        xp = edit_XP()
                        type_print(f"Ajusting XP . . .\n")
                        time.sleep(0.5)
                        chara["XP"] += xp
                        type_print("XP updated\n")
                        type_print(f"XP for {chara["Name"]} is {chara['XP']}\n")
                        level_up_loop(chara)
                        break
                    elif choice == "2":
                        stat, value = edit_stat()
                        type_print(f"Your new stat for {stat} is {value}\n")
                        chara[stat] = value
                        break
                    elif choice == "3":
                        edit_inventory()
                        break
                    else:
                        print("Invalid input. Please try again")
                        continue
                type_print("Would you like to:\n1) continue editing characters or\n2) Leave\n")
                again = input("Type the number for the action you would like to do\n")
                if again == "1":
                    clear_screen()
                    view_character()
                    break
                else:
                    type_print("Redirecting to main menu . . .\n")
                    time.sleep(0.5)
                    menu()
                    break
            else:
                print("Could not find the character you typed in. Check your spelling and punctuation.")
                continue
menu()