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
performance = 3 + 10 * np.random.rand(len(charcters))
error = np.random.rand(len(charcters))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=charcters)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Strength', fontsize = 30)
ax.set_title('Strength of Characters', fontsize = 50)

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()
