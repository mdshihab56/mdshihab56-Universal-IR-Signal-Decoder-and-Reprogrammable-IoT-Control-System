import numpy as np
import matplotlib.pyplot as plt

GRAPH_COLOR = 'darkred'
LINE_WIDTH = 3

time = np.array([
    0,1,2,3,4,5,6,7,8,9,10,11
])

signal = np.array([
    0,1,1,0,1,0,1,1,0,1,0,0
])

plt.figure(figsize=(12,4))

plt.step(
    time,
    signal,
    where='post',
    color=GRAPH_COLOR,
    linewidth=LINE_WIDTH
)

plt.title(
    "IR Signal Pulse Waveform",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel(
    "Time (ms)",
    fontsize=14
)

plt.ylabel(
    "Signal State",
    fontsize=14
)

plt.yticks([0,1], ['LOW','HIGH'])

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()