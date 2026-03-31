
from faker import Faker
fake = Faker()

name = fake.name()


address = fake.address()


article = fake.text()

print(f"Hello {name}!")
print(f"Your address is {address}.")
print(f"Todays words are {article}.")

for _ in range(10):
  print(fake.name())