# LV 1st RPG Pseudocode

# Main Menu
# dictionary with options
# User has to choose a number to select an option
# Each option is associated with a number for easy selection
# What it would display
# 1. View Characters
# 2. Create Character
# 3. Edit Character
# 4. Exit
# menu_option is set to input type 1 to 4 to decide which option to choose

# dictionary with the different options the player can choose
# Each option is associated with a number for easy selection
# The options include actions like "View", "Create", "Edit", and "Leave"
def main_menu():
    """
    Displays the main menu options for the player.
    """
    options = {
        1: "View Character",
        2: "Create Character",
        3: "Edit Character",
        4: "Leave Game"
    }

    print("\nMain Menu")
    for key, value in options.items():
        print(f"{key}. {value}")

# CREATE CHARACTER FUNCTION
# This function allows the player to create a new character
# It prompts the player for character details and stores them in a dictionary
# User can choose a class "Rogue", "Cleric","Rogue"
  # ROGUE CLASS
    # If user chooses 2 then it is Rouge
    # Needs 15 xp to level up and doubles from there
    # Stats
    # Strength: 20
    # Health: 20
    # Wisdom:20


   # Cleric CLASS
    # If user chooses 3 then it is Cleric
    # Needs 20 xp to level up and doubles from there
    # Stats
    # Strength: 10
    # Health: 30
    # Wisdom:20
def create_character():
    character = {}
    character['name'] = input("Enter your character's name: ")
    print("Choose your class:")
    print("1. Rogue")
    print("2. Cleric")
    class_choice = input("Enter the number of your choice: ")
    
    if class_choice == '1':
        character['class'] = 'Rogue'
        character['strength'] = 20
        character['health'] = 20
        character['wisdom'] = 20
        character['xp'] = 0
        character['level'] = 1
    elif class_choice == '2':
        character['class'] = 'Cleric'
        character['strength'] = 10
        character['health'] = 30
        character['wisdom'] = 20
        character['xp'] = 0
        character['level'] = 1
    else:
        print("Invalid choice. Please try again.")
        return create_character()
    
    return character


# EDIT CHARACTER FUNCTION
# Running in the backround 
# This is a loop that allows the player to check if their character can level up
# If the character has enough XP, they level up
# When leveling up
# Cleric : add 1 to attack power, if cleric: add one spell slot if 
# new level is multiple of 5, tell user this charcter has leveled up
# Else return to the start(Check if character can level up)

# Level up loop
# def level_up_loop(character):
       # xp_needed = character['level'] * 15 if character['class'] == 'Rogue' else character['level'] * 20
         # if character['xp'] >= xp_needed:
              # character['level'] += 1
              # character['xp'] -= xp_needed
              # character['attack_power'] += 1
              # if character['class'] == 'Cleric' and character['level'] % 5 == 0:
                # character['spell_slots'] += 1
              # print(f"{character['name']} has leveled up to level {character['level']}!")
        #  else:
                # break

def level_up_loop(character):
    """
    Checks if the character has enough XP to level up.
    Rogue needs 15 XP per level.
    Cleric needs 20 XP per level.
    """
    if character['class'] == 'Rogue':
        xp_needed = character['level'] * 15
    else:
        xp_needed = character['level'] * 20

    if character['xp'] >= xp_needed:
        character['xp'] -= xp_needed
        character['level'] += 1
        character['strength'] += 1

    if character['class'] == 'Cleric' and character['level'] % 5 == 0:
        character['spell_slots'] += 1
        print("You gained an extra spell slot!")

        print(f"{character['name']} leveled up to level {character['level']}!")
    else:
         return
# TENGO QUE LLAMAR A LAS FUNCIONES EN UN MAIN LOOP Y EN EL OTRO PARA QUE CORRAN
def run_game():
    character = None

    while True:
        main_menu()
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            if character:
                print("\nCharacter Info:")
                for key, value in character.items():
                    print(f"{key}: {value}")
            else:
                print("No character created yet.")

        elif choice == '2':
            character = create_character()
            print("Character created successfully!")

        elif choice == '3':
            if character:
                level_up_loop(character)
            else:
                print("No character to edit. Create one first.")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


run_game()



