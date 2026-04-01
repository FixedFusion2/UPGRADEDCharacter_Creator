
from faker import *
import random

fake = Faker('en_US')

"""name = fake.name()


address = fake.address()


article = fake.text()

print(f"Hello {name}!")
print(f"Your address is {address}.")
print(f"Todays words are {article}.")
print("Here are some more names: ")
for _ in range(10):
  print(fake.name())
"""

def generate_character_profile():
    profile = {
        "name": fake.name(),
        "job": fake.job(),
        "company": fake.company(),
        "birthdate": fake.date_of_birth(minimum_age=18, maximum_age=80),
        "address": fake.address(),
        "email": fake.email(),
        "username": fake.user_name(),
        "blood_group": fake.profile(fields=['blood_group'])['blood_group'] # Using profile provider
    }
    return profile

def generate_backstory(character_profile):
    name = character_profile["name"]
    job = character_profile["job"]
    company = character_profile["company"]
    address = character_profile["address"]
    birthdate = character_profile["birthdate"]

    # Use fake.text() to generate a random narrative block
    # The 'text' provider creates paragraphs of lorem ipsum type text,
    # which can be customized in length.
    narrative_snippet = fake.text(max_nb_chars=300)

    backstory = f"""
    Name: {name}
    Occupation: {job} at {company}
    Born: {birthdate}
    Residence: {address}

    A brief history: {narrative_snippet}
    """
    return backstory

if __name__ == "__main__":
    my_character = generate_character_profile()
    my_backstory = generate_backstory(my_character)
    print(my_backstory)




fake = Faker()

def generate_backstory():
    # 1. Generate fake data points
    name = fake.name()
    name2 = fake.name()
    adjective = fake.word(part_of_speech='adjective')
    noun1 = fake.word(part_of_speech='noun')
    # Using 'verb' usually gives base form, sometimes needs manual -ing
    verb = fake.word(part_of_speech='verb') 
    noun2 = fake.word(part_of_speech='noun')
    place = fake.city()
    
    # 2. Define the template
    template = (
        f"{name} was a {adjective} {noun1}, known for {verb}ing the {noun2} "
        f"in the city of {place}. Their life changed when they met a "
        f"{fake.job()} named {name2}. {name2} was the one who gave {name} their power, because of this, they were {adjective}."
    )
    
    return template

# Generate and print a random backstory
print(generate_backstory())
