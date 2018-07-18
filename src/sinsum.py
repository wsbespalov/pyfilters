import numpy as np
from matplotlib.pyplot import figure, show

t = np.arange(0.0, 1.0, 0.01)
fig = figure(1)

# Signal # 1
signal1 = np.sin(2*np.pi*t)
# Signal # 2
signal2 = np.sin(4*np.pi*t)

# Plot Signal # 1
axis1 = fig.add_subplot(311)
axis1.plot(t, signal1)
axis1.grid(True)
axis1.set_ylim((-2, 2))
axis1.set_ylabel("Amplitude")

# Plot Signal # 2
axis2 = fig.add_subplot(312)
axis2.plot(t, signal2)
axis2.grid(True)
axis2.set_ylim((-2, 2))
axis2.set_ylabel("Amplitude")

# Plot Signals Sum
axis3 = fig.add_subplot(313)
axis3.plot(t, signal1 + signal2)
axis3.grid(True)
axis3.set_ylim((-2, 2))
axis3.set_ylabel("Amplitude")

show()