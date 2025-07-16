import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Parameters
t = np.linspace(0, 2*np.pi, 1000)  # Time array
num_terms = 5  # Number of Fourier terms to display
freq = np.arange(1, num_terms + 1)  # Frequencies for Fourier terms
amplitudes = 1 / freq  # Amplitudes decrease with frequency (1/n)

# Create the original signal (sum of sines)
def original_signal(t):
    signal = np.zeros_like(t)
    for n in range(1, num_terms + 1):
        signal += (1/n) * np.sin(n * t)
    return signal

# Set up the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Initialize lines for each Fourier component and the sum
lines = []
for i in range(num_terms + 1):  # +1 for the summed signal
    line, = ax.plot([], [], [], lw=2)
    lines.append(line)

# Set plot limits and labels
ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-2, 2)
ax.set_zlim(0, num_terms + 1)
ax.set_xlabel('Time (t)')
ax.set_ylabel('Amplitude')
ax.set_zlabel('Frequency Component')
ax.set_title('3D Fourier Series Decomposition')

# Initialization function for animation
def init():
    for line in lines:
        line.set_data([], [])
        line.set_3d_properties([])
    return lines

# Animation update function
def update(frame):
    # Update each Fourier component
    for i in range(num_terms):
        y = amplitudes[i] * np.sin(freq[i] * t[:frame])
        lines[i].set_data(t[:frame], y)
        lines[i].set_3d_properties([i+1] * len(t[:frame]))
    
    # Update the summed signal
    y_sum = original_signal(t[:frame])
    lines[-1].set_data(t[:frame], y_sum)
    lines[-1].set_3d_properties([0] * len(t[:frame]))
    
    return lines

# Create animation
ani = animation.FuncAnimation(fig, update, init_func=init, frames=len(t), interval=20, blit=True)

# Show plot
plt.show()