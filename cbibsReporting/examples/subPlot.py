# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 4, sharex=True, sharey=True)

# add a big axes, hide frame
fig.add_subplot(111, frameon=False)

# hide tick and tick label of the big axes
plt.tick_params(labelcolor='none', top='off', bottom='off', left='off', right='off')
plt.grid(False)
plt.xlabel("common X")
plt.ylabel("common Y")



