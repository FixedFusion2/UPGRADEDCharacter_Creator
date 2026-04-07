# LD, LV, & TE First group Project
import random
import time
import os
from faker import Faker
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

fake = Faker()

#CSV Path so we can use the file path easier with this variable
CSV_PATH = r"character_creator\\docs\\characters.csv"

#Clear Screen Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#Type Print Function for text
def type_print(string, delay = 0.08):
    for char in string:
        print(char, end="", flush = True)
        time.sleep(delay)
    print()#Newline

#Class Definitions
#Character Class
class Character:
    def __init__(self, name, c_class, stats, weapon, inventory=None, xp=0, level=1, spell_slots=0):
        #Defining objects
        self.name = name
        self.Class = c_class
        self.Stats = stats
        self.Weapon = weapon
        self.Inventory = inventory if inventory else []
        self.XP = xp
        self.Level = level
        self.Spell_slots = spell_slots

    def level_up(self):
        # Check for xp
        xp_needed = 15 if self.Class in ["Rogue", "Fighter"] else 20
        xp_needed *= self.Level
        leveled = False
        while self.XP >= xp_needed:
            self.XP -= xp_needed
            self.Level += 1
            self.Stats['Strength'] += 1
            leveled = True
            type_print(f"{self.name} leveled up to level {self.Level}!")
            if self.Class == 'Cleric' and self.Level % 5 == 0:
                self.Spell_slots += 1
                type_print(f"{self.name} gained an extra spell slot!")
            xp_needed = 15 if self.Class in ["Rogue", "Fighter"] else 20
            xp_needed *= self.Level
        return leveled
    #Dict for various charcter information
    def to_dict(self):
        return {
            "Name": self.name,
            "Class": self.Class,
            "Strength": self.Stats.get("Strength", 0),
            "Health": self.Stats.get("Health", 0),
            "Wisdom": self.Stats.get("Wisdom", 0),
            "Dexterity": self.Stats.get("Dexterity", 0),
            "Intelligence": self.Stats.get("Intelligence", 0),
            "XP": self.XP,
            "Level": self.Level,
            "Weapon": self.Weapon,
            "Inventory": self.Inventory,
            "Spell_slots": self.Spell_slots      
          }
#Random generation Class
class RandomGenerator:
    @staticmethod
    #Random_Character Class using faker
    def random_character(base_class=None):
        #Make random information for random character
        c_class = base_class or random.choice(list(classes.keys()))
        base = classes[c_class]
        stats = base['Stats'].copy()
        stats['Dexterity'] = random.randint(10,30)
        stats['Intelligence'] = random.randint(10,30)
        name = fake.name()
        weapon = random.choice(base['Weapons'])
        inventory = [fake.word().title() for _ in range(random.randint(1,3))]
        backstory = fake.sentence(nb_words=12)
        personality = fake.word().title()
        return Character(name,base['Name'], stats, weapon, inventory, xp=0, level=1, spell_slots = 0), backstory, personality

#Show data with matplotlib
class DataVisualization:
    @staticmethod
    def radar_chart(char: Character):
        labels = list(char.Stats.keys())
        stats = list(char.Stats.values())
        angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
        stats = np.concatenate((stats,[stats[0]]))
        angles = np.concatenate((angles,[angles[0]]))
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        ax.plot(angles,stats, 'o-', linewidth=2)
        ax.fill(angles, stats, alpha=0.25)
        ax.set_thetagrids(angles * 180/np.pi, labels)
        ax.set_title(f"{char.name}'s Stats")
        plt.show()

    @staticmethod
    #Compare Characters Function
    def compare_characters(chars):
        labels = list(chars[0].Stats.keys())
        angles= np.linspace(0,2 * np.pi, len(labels), endpoint=False)
        fig, ax = plt.subplots(subplot_kw=dict(polar=True))
        for char in chars:
            stats = list(char.Stats.values())
            stats = np.concatenate((stats,[stats[0]]))
            ax.plot(np.concatenate((angles,[angles[0]])), stats, label=char.name)
            ax.fill(np.concatenate((angles,[angles[0]])), stats, alpha=0.1)
        ax.set_thetagrids(angles * 180/np.pi, labels)
        ax.set_title("Character Comparison")
        ax.legend()
        plt.show()
    
    @staticmethod
    #Show bar chart
    def bar_char(char: Character):
        stats = list(char.Stats.values())
        labels = list(char.Stats.keys())
        plt.bar(labels, stats, color='skyblue')
        plt.title(f"{char.name}'s Stats")
        plt.show()
    
class StatisticalAnalyzer:
    @staticmethod
    #Summary Function
    def summary(df: pd.DataFrame):
        #Save various stats
        numeric_cols = ['Strength', 'Health', 'Wisdom', 'Dexterity', 'Intelligence', 'XP', 'Level']
        type_print("Character Stats Summary:")
        type_print(str(df[numeric_cols].describe()))
        print(df[numeric_cols].describe())


classes = { 
1 : {"Name": "Fighter", "Weapons": ["Greatsword", "Greataxe", "Maul"], "Stats": {"Strength": 30, "Health": 20, "Wisdom": 10}},
2 : {"Name": "Rogue", "Weapons": ["Daggers", "Blowgun", "Knives"], "Stats": {"Strength": 20, "Health": 20, "Wisdom": 20}},
3 : {"Name": "Cleric", "Weapons": ["Mace", "Warhammer", "Morning Star"], "Stats": {"Strength": 10, "Health": 30, "Wisdom": 20}}}

#Load Existing Characters
try: 
    #Bringing characters from file path.
    df_chars = pd.read(CSV_PATH)
except:
    def_chars = pd.DataFrame(columns=["Name","Class","Strength","Health","Wisdom","Dexterity","Intelligence","XP","Level","Weapon","Inventory","Spell_slots"])

characters = []

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
            print('View Stats Graph')
        elif menu_option == "5":
            print("Compare Characters Menu")
        elif menu_option == "6":
            print("Generate Random Character")
        elif menu_option == "7":
            StatisticalAnalyzer.summary(df_chars)
        elif menu_option == "8":
            type_print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")
            continue

