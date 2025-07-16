import numpy as np
import matplotlib.pyplot as plt

# Set up the grid
x = np.linspace(-10, 10, 500)
y = np.linspace(-10, 10, 500)
X, Y = np.meshgrid(x, y)

# Define a simple 2D Fourier pattern
def fourier_pattern(X, Y, frequencies=[1, 2], amplitudes=[1, 0.5]):
    Z = np.zeros_like(X)
    for freq, amp in zip(frequencies, amplitudes):
        # Combine sine waves in x and y directions
        Z += amp * (np.sin(freq * X) + np.sin(freq * Y))
    return Z

# Generate the pattern
Z = fourier_pattern(X, Y)

# Plot the 2D pattern
plt.figure(figsize=(8, 8))
plt.imshow(Z, cmap='viridis', extent=[-10, 10, -10, 10])
plt.colorbar(label='Amplitude')
plt.title('2D Fourier Pattern')
plt.xlabel('x')
plt.ylabel('y')
plt.show()