import numpy as np
import matplotlib.pyplot as plt

GRAPH_COLOR = 'purple'

pulse_widths = np.random.normal(
    560,
    40,
    1000
)

plt.figure(figsize=(10,6))

plt.hist(
    pulse_widths,
    bins=30,
    color=GRAPH_COLOR,
    edgecolor='black',
    linewidth=1.5
)

plt.title(
    "IR Pulse Width Distribution",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel(
    "Pulse Width (µs)",
    fontsize=14
)

plt.ylabel(
    "Frequency",
    fontsize=14
)

plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()