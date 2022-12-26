import numpy as np
import matplotlib.pyplot as plt

# Set the number of iterations to use when generating the Mandelbrot set
num_iterations = 200

# Set the range of x and y values to use when generating the Mandelbrot set
x_min, x_max, y_min, y_max = -2, 1, -1.5, 1.5

# Generate a 2D array of complex numbers representing the points in the image
x_values = np.linspace(x_min, x_max, 1000)
y_values = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x_values, y_values)
C = X + 1j * Y

# Generate the Mandelbrot set using the complex numbers in C
M = np.zeros(C.shape, dtype=np.int32)
for i in range(num_iterations):
    mask = (M == 0) & (abs(C) < 2)
    M[mask] = i
    C[mask] = C[mask] ** 2 + C

# Display the Mandelbrot set
plt.imshow(M, cmap='gist_ncar', extent=(x_min, x_max, y_min, y_max))
plt.show()

