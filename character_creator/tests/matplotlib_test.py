import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)

# Example data
charcters = ('Thor Odenson', 'Tolkien Lewis', 'Harry Potter', 'Slim Jim', 'Jimithy Timson')
y_pos = np.arange(len(charcters))
performance = 3 + 10 * np.random.rand(len(charcters))
error = np.random.rand(len(charcters))

fig, ax = plt.subplots()

hbars = ax.barh(y_pos, performance, xerr=error, align='center')
ax.set_yticks(y_pos, labels=charcters)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Power')
ax.set_title('Power of characters')

# Label with specially formatted floats
ax.bar_label(hbars, fmt='%.2f')
ax.set_xlim(right=15)  # adjust xlim to fit labels

plt.show()