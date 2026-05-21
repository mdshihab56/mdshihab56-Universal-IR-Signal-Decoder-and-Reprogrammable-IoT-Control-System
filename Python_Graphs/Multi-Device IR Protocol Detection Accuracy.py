import matplotlib.pyplot as plt

GRAPH_COLOR = 'royalblue'
BAR_EDGE = 'black'

devices = [
    'Sony',
    'Samsung',
    'LED Strip',
    'General AC',
    'Vision AC',
    'Vision TV',
    'Panasonic TV',
    'BLDC Fan'
]

accuracy = [96, 94, 92, 89, 91, 95, 93, 90]

plt.figure(figsize=(12,6))

bars = plt.bar(
    devices,
    accuracy,
    color=GRAPH_COLOR,
    edgecolor=BAR_EDGE,
    linewidth=2
)

plt.ylim(80,100)

plt.title(
    "Multi-Device IR Protocol Detection Accuracy",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel(
    "Remote Device Type",
    fontsize=14
)

plt.ylabel(
    "Detection Accuracy (%)",
    fontsize=14
)

plt.grid(axis='y', linestyle='--', alpha=0.6)

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        yval + 0.3,
        f'{yval}%',
        ha='center',
        fontsize=11,
        fontweight='bold'
    )

plt.tight_layout()
plt.show()