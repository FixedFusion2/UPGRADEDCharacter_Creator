#TE 2nd Upgraded Character Creator
#Import all Libraries
import random
import time
import os
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helper import *

#Menu
def menu():
    #Call All Functions
    clear_screen()
    while True:
        print("Main Menu")
        print("1. View Character")
        print("2. Create Character")
        print("3. Edit Character")
        print("4. View Stats Graph")
        print("5. Compare Characters")
        print("6. Generate Random Character")
        print("7. Data Analysis Dashboard")
        print("8. Exit")
        menu_option = input("Select an option (1-4): ")
        if menu_option == "1":
            view_character()
        elif menu_option == "2":
            create_character()
        elif menu_option == "3":
            edit_character()
        elif menu_option == "4":
            if characters:
                DataVisualization.bar_char(characters[-1])
            else:
                print("No characters to graph.")
        elif menu_option == "5":
            if len(characters):
                DataVisualization.compare_characters(characters)
            else:
                print("Need at least 2 characters.")
        elif menu_option == "6":
            char, _,_ = RandomGenerator.random_character()
            characters.append({
                "Name": char.name,
                "Class": char.Class,
                "Stats": char.Stats,
                "Weapon": char.Weapon,
                "Inventory": char.Inventory,
                "XP": char.XP,
                "Level": char.Level
            })
            print(f"Generated: {char.name}") 
        elif menu_option == "7":
            if characters:
                df = pd.DataFrame([{
                    "Strength": c["Stats"]["Strength"],
                    "Health": c["Stats"]["Health"],
                    "Wisdom": c["Stats"]["Wisdom"],
                    "Dexterity": c["Stats"]["Dexterity"],
                    "Intelligence": c["Stats"]["Intelligence"],
                    "XP": c["XP"],
                    "Level": c["Level"]
                } for c in characters])

                StatisticalAnalyzer.summary(df)  
            else:
                print("No Data Available")
        elif menu_option == "8":
            type_print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
            continue

menu()
