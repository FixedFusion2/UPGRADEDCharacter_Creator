import matplotlib.pyplot as plt
import numpy as np
from faker import *
fake = Faker()
name1 = fake.name()
name2 = fake.name()
name3 = fake.name()
name4 = fake.name()
name5 = fake.name()
# Fixing random state for reproducibility
np.random.seed(19680801)

# Example data
charcters = (name1, name2, name3, name4, name5)
y_pos = np.arange(len(charcters))
strength = 3 + 10 * np.random.rand(len(charcters))
error = np.random.rand(len(charcters))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, strength, xerr=error, align='center', color = 'red')
ax.set_yticks(y_pos, labels=charcters)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Strength', fontsize = 30)
ax.set_title('Strength of Characters', fontsize = 50)

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()

fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

recipe = ["375 g flour",
          "75 g sugar",
          "250 g butter",
          "300 g berries"]

data = [float(x.split()[0]) for x in recipe]
ingredients = [x.split()[-1] for x in recipe]


def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute:d} g)"


wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"))

ax.legend(wedges, ingredients,
          title="Ingredients",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))

plt.setp(autotexts, size=8, weight="bold")

ax.set_title("Matplotlib bakery: A pie")

plt.show()