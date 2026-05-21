import matplotlib.pyplot as plt

GRAPH_COLOR = 'green'
LINE_WIDTH = 3

devices = [
    'Sony',
    'Samsung',
    'LED Strip',
    'General AC',
    'Vision TV',
    'Panasonic TV',
    'BLDC Fan'
]

delay = [11,13,15,19,12,14,16]

plt.figure(figsize=(12,6))

plt.plot(
    devices,
    delay,
    marker='o',
    markersize=10,
    linewidth=LINE_WIDTH,
    color=GRAPH_COLOR
)

plt.title(
    "IR Signal Decoding Delay",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel(
    "Device Type",
    fontsize=14
)

plt.ylabel(
    "Response Delay (ms)",
    fontsize=14
)

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()