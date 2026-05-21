import numpy as np
import matplotlib.pyplot as plt

timings = np.random.normal(560,40,1000)

plt.hist(timings, bins=30)

plt.title("IR Pulse Duration Distribution")
plt.xlabel("Pulse Width (us)")
plt.ylabel("Frequency")

plt.show()