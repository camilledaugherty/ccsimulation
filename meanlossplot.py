import matplotlib.pyplot as plt
import numpy as np

# to run: python meanlossplot.py

fillp_sheep1 = 3.71
ledbat1 = 0.17
scream1 = 0.00

fillp_sheep2 = 0.24
ledbat2 = 0.37
scream2 = 0.20

schemes = ["FillP_Sheep", "LEDBAT", "SCReAM"]
exp1 = [3.71,0.17,0.00]
exp2 = [0.24,0.37,0.20] #hardcoded from experiment data

w, x = 0.4, np.arange(len(schemes))

fig, ax = plt.subplots()
ax.bar(x - w/2, exp1, width=w, label='Experiment 1 (High Bandwidth, Low Latency)')
ax.bar(x + w/2, exp2, width=w, label='Experiment 2 (Low Bandwidth, High Latency)')

ax.set_xticks(x)
ax.set_xticklabels(schemes)
ax.set_ylabel('Mean Packet Loss Rate')
ax.set_title('Packet Loss Rate')
ax.legend()

plt.show()

