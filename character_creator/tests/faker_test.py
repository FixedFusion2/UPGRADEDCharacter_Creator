
from faker import Faker
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