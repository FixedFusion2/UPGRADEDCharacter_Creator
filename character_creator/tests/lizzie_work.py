# Lizzie's File for Code

import time
import random

delay = 0.06

def type_print(string):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)

type_print("First, create a character before testing my code\n\n")
from trues_file import *
# VIEWING CHARACTER
# This will likely be a function: First check to see if they have one or more characters. If they do, show characters in a numbered list and have the user pick the number corresponding to the character they want to view. If user has no charcters, tell them and redirect to main menu where they can make a character.
def find_character(furture_action):
    global characters
    while True:
        type_print(f"How would you like to find your character for {furture_action}\n1) Name\n2) Class\n3) Level\n")
        find = input("Type the number corresponding to your action\n").strip()
        if find == "1":
            name = input("Enter the name of the character you want to find\n").strip().title()
            type_print(f"\nCharacters containing '{name}' in their name:\n")
            for character in characters:
                if name in character["Name"]:
                    print(f"{character["Name"]}")
            break
        elif find == "2":
            class_name = input("Enter the name of the character you want to find\n").strip().title()
            type_print(f"\nCharacters with '{class_name}' as their class:\n")
            for character in characters:
                if class_name in character["Class"]:
                    print(f"{character["Name"]}: {character["Class"]}")
            break
        elif find == "3":
            level = input("Enter the level for the character you want to find\n").strip()
            type_print(f"\nCharacters whose level is '{level}':\n")
            for character in characters:
                if int(level) in character["Level"]:
                    print(f"{character["Name"]}: Level {character["Level"]}")
            break
        else:
            type_print("Invalid input. Please Try again\n")
            continue

def view_character():
    global characters
    if not characters:
        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
        # Call main menu
    type_print("First,\n")
    find_character("viewing")
    while True:
        character = input("Type the name of the character you wish to view\n").strip().title()
        for chara in characters:
            if character == chara["Name"]:
                type_print(f"Viewing Character:\n Name: {character['Name']}\n Class: {character['Class']}\nStats:\n Strength: {character['Stats']['Strength']}\n Health: {character['Stats']['Health']}\n Wisdom: {character['Stats']['Wisdom']}\n Dexterity: {character['Stats']['Dexterity']}\n Intelligence: {character['Stats']['Intelligence']}\n {character['Level']}\n XP: {character['XP']}\n Weapon: {character['Weapon']}\n")
                time.sleep(2)
                type_print("Would you like to\n1)View another character\nor\n2) Go back to main menu\n")
                again = input("Type the number for the action you would like to do\n")
                if again == "1":
                    view_character()
                    break
                else:
                    type_print("Redirecting to main menu . . .\n")
                    time.sleep(0.5)
                    # Call menu()
                    break
            else:
                print("Could not find the character you typed in. Check your spelling and punctuation.")
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
                print("Invalid input. Try again")
                continue

    def edit_invintory():
        # Use helper to know if adding or removing. Have user type in something to add\remove to invintory list
        adding = adding_removing("invintory")
        if adding == "ADDING":
            while True:
                add = input("What would you like to add to your character's invintory\n").strip().title()
                # I need True to set up an invintory so I can append 'add' into it 
        else:
            while True:
                remove = input("What would you like to remove from your character's invintory\n").strip().title()
                # True needs to give me an invintory so I can hunt down 'remove' and remove it from the list

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
        character = input("Type the name of the character you wish to edit\n").strip().title()
        for chara in characters:
            if character == chara["Name"]:
                while True:
                    type_print(f"What would you like to edit on {character}:\n1) XP amount\n2) Reroll a stat\n3) Adjust {character}'s Inventory\n")
                    action = input("Enter the number correspondng to what you want to edit\n")
                    if action == "1":
                        xp = edit_XP()
                        type_print(f"Ajusting XP . . .\n")
                        time.sleep(0.5)
                        chara["XP"] += xp
                        type_print("XP updated\n")
                        type_print(f"XP for {chara["Name"]} is {chara['XP']}")
                        break
                    elif action == "2":
                        stat, value = edit_stat()
                        type_print(f"Your new stat for {stat} is {value}\n")
                        chara[stat] = value
                        break
                    elif action == "3":
                        #item = edit_invintory()
                        print("Unable to edit invintory right now. Please pick something else to edit\n")
                        break
                    else:
                        print("Invalid input. Please try again")
                        continue
                type_print("Would you like to:\n1) continue editing characters or\n2) Leave\n")
                again = input("Type the number for the action you would like to do\n")
                if again == "1":
                    view_character()
                    break
                else:
                    type_print("Redirecting to main menu . . .\n")
                    time.sleep(0.5)
                    # Call menu()
                    break
            else:
                print("Could not find the character you typed in. Check your spelling and punctuation.")
                continue
    


#    global characters
#    if not characters:
#        type_print("You don't have any characters to edit.\nRedirecting you to main menu to make a character\n")
#        # Call main menu
#    else:
#        while True:
#            type_print("These are the characters you have to edit:\n")
#            for character in characters:
#                # Print the character names with a number before each one
#                print(f"{character['Name']} ({character["Class"]})")
#            print("Leave")
#            edit_choice = input("Type the name of the character you want to edit (or 'Leave' if you want to go back to main menu):\n").strip()
#            if edit_choice == "Leave":
#                type_print("Redirecting to main menu . . .\n")
#                time.sleep(0.5)
#                # Call main
#                break
#            for chara in characters:
#                if edit_choice == chara["Name"]: 
#                    # Now give the user a list of things to edit and call the inner function corresponding to the selection
#                    while True:
#                        type_print(f"What would you like to edit on {chara["Name"]}:\n1) XP amount\n2) Reroll a stat\n3) {chara["Name"]}'s Invintory\n")
#                        choice = input("Type the number corresponding to what you want to edit\n").strip().upper()
#                        if choice == "1":
#                            xp = edit_XP()
#                            type_print(f"Ajusting XP . . .\n")
#                            time.sleep(0.5)
#                            chara["XP"] += xp
#                            type_print("XP updated\n")
#                            type_print(f"XP for {chara["Name"]} is {chara['XP']}")
#                            break
#                        elif choice == "2":
#                            stat, value = edit_stat()
#                            type_print(f"Your new stat for {stat} is {value}\n")
#                            chara[stat] = value
#                            break
#                        elif choice == "3":
#                            #item = edit_invintory()
#                            print("Unable to edit invintory right now. Please pick something else to edit\n")
#                            continue
#                    # We have left the editing loop and now need to leave the selection loop
#                    type_print(f"Would you like to:\n1) continue editing characters or\n2) Leave\n")
#                    stay = input("Type the number corresponding to the action you would like to do\n")
#                    if stay == "1":
#                        continue
#                    else:
#                        type_print("Leaving character editor.\nRedirecting to main menu . . .\n")
#                else:
#                    print("Could not find the character you typed in. Check your spelling and punctuation.")
#                    continue

type_print("\nNow testing Viewing Character (My code)\n\n")
view_character()
type_print("\nNow testing Editing Character (My code)\n\n")
edit_character()

# When they have selected a character, show the character name, class, stats, current attack moves, XP amount, and level. Ask user if they would like to edit their character. If yes, direct to edit func. If no, redirect to main menu

# EDITING CHARACTER
# Delete a character, edit stats (including XP), edit attack menu.

# Deleting a character: Show user a numbered list of characters and have them select the number corresponding to the character they want to remove. Find that character (likely a dictionary with the character name as the dict name) and delete it.

# Edit stats: Ask user what they want to edit: add or remove XP, reroll a stat, edit attack menu/invintory

# Adding/removing XP: Ask if this is adding or removing. Have user type in a number and add or subtract based on previous answer

# Reroll a stat: Show the stats for the character and have the user type the name (as displayed) for the stat they want to reroll. Find that stat in the (likely) character dict and pick a number between 10 & 20. Show user the new stat and save it. Ask if they want to continue editing. Yes: Back to top of func. No: Redirect to main menu

# Edit Attack menu: Show user currect attack menu (It's a list). Ask if they want to add something or remove something
# Remove something: Show user numbered list of attacks and ask which number they would like to remove. Find that in the list and remove it from attack menu list. Add the same thing to a list of all POSSIBLE attacks the character could do (spells, aquired weapons, potions, etc.) When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.
# Add something: Show user numbered list of POSSIBLE attacks character can do . Have user select number they would like to add to attack menu. If attack menu full (six moves), tell user and redirect to remove something. If there is room for another move, remove selected move from POSSIBLE moves and add it to Attack menu list. When that is done, ask user if they want to conitue editing attack menu. If yes, back to top of attack menu edit. If no, redirect to main menu.