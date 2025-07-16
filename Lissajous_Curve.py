import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
t = np.linspace(0, 2 * np.pi, 1000)  # Time array
a, b = 3, 2  # Frequencies for x and y
phi = np.pi / 2  # Phase shift

# Lissajous curve and its reflection
x = np.sin(a * t)
y = np.sin(b * t + phi)
y_reflection = -np.sin(b * t + phi)  # Reflection across x-axis

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Animated Lissajous Curve with Reflection')
ax.grid(True)
ax.set_aspect('equal')

# Plot objects for the curve and its reflection
line, = ax.plot([], [], color='blue', label='Lissajous Curve')
line_reflection, = ax.plot([], [], color='red', linestyle='--', label='Reflection')
ax.legend()

# Initialization function
def init():
    line.set_data([], [])
    line_reflection.set_data([], [])
    return line, line_reflection

# Animation function
def animate(i):
    # Update the curve up to index i
    line.set_data(x[:i], y[:i])
    # Update the reflection
    line_reflection.set_data(x[:i], y_reflection[:i])
    return line, line_reflection

# Create animation
ani = FuncAnimation(fig, animate, init_func=init, frames=len(t), interval=20, blit=True)

# Show the animation
plt.show()