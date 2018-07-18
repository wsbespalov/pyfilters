import numpy as np
from matplotlib.pyplot import figure, show
import random

t = np.arange(0.0, 1.0, 0.01)
fig = figure(1)

# Signal
signal1 = np.sin(2*np.pi*t)
# Noise
noise = 0.0003*np.asarray(random.sample(range(0,1000), 100))

# Plot Signal
axis1 = fig.add_subplot(311)
axis1.plot(t, signal1)
axis1.grid(True)
axis1.set_ylim((-2, 2))
axis1.set_ylabel("Amplitude")

# Plot Noise
axis2 = fig.add_subplot(312)
axis2.plot(t, noise)
axis2.grid(True)
axis2.set_ylim((-2, 2))
axis2.set_ylabel("Amplitude")

# Plot Signal + Noise
axis3 = fig.add_subplot(313)
axis3.plot(t, signal1 + noise)
axis3.grid(True)
axis3.set_ylim((-2, 2))
axis3.set_ylabel("Amplitude")

# Show plots
show()