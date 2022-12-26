import numpy as np
import matplotlib.pyplot as plt

# Set the number of iterations to use when generating the Mandelbrot set
num_iterations = 100

# Set the range of x and y values to use when generating the Mandelbrot set
x_min, x_max, y_min, y_max = -2, 2, -2, 2

# Generate a 2D array of complex numbers representing the points in the image
x_values = np.linspace(x_min, x_max, 1000)
y_values = np.linspace(y_min, y_max, 1000)
X, Y = np.meshgrid(x_values, y_values)
C = X + 1j * Y

# Generate the Mandelbrot set using the complex numbers in C
M = np.zeros(C.shape, dtype=np.int32)
for i in range(num_iterations):
    if M.all() == 0:
        mask = (abs(C) <= 2)
        M[mask] = i
        C[mask] = C[mask] ** 2 + C[mask]
    else:
        mask = (abs(C) <= 2)
        C[mask] = C[mask] ** 2 + C[mask]
        M[mask] = i

# Display the Mandelbrot set using a color map based on the number of iterations
plt.imshow(M, cmap='viridis', extent=(x_min, x_max, y_min, y_max))
plt.colorbar()
plt.title('Fraktal Set')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.show()
