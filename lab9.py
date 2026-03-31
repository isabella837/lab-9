import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore

# Function 1: Curve Plotting
def plot_curve(x_values, y_values):
    plt.figure()

    plt.plot(x_values, y_values, marker='o')

    plt.title("Curve Plot")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.grid(True)

    plt.show()

# Function 2: Hertzsprung-Russell Diagram
def plot_hr_diagram(temperature, luminosity):
    plt.figure()

    scatter = plt.scatter(temperature, luminosity,
                          c=temperature, cmap='plasma')
    
    plt.title("Hertzsprung-Russell Diagram")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Luminosity (L☉)")

    # IMPORTANT: Temperature decreases left --> right
    plt.gca().invert_xaxis()

    plt.colorbar(scatter, label="Temperature (K)")

    plt.grid(True)

    plt.show()

# Frunction 3: Creating Heat Maps and Density Plots
def plot_density(data, color_map='gray'):
    plt.figure()

    x = data[:, 0]
    y = data[:, 1]

    plt.hist2d(x, y, bins=30, cmap=color_map)

    plt.title("Creating Heat Maps and Density Plots")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.colorbar(label="Density")

    plt.show()

# Running the functions
if __name__ == "__main__":
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    plot_curve(x, y)

    temp = np.array([3000, 5000, 7000, 9000, 11000])
    lum = np.array([0.1, 1, 10, 100, 1000])
    plot_hr_diagram(temp, lum)

    np.random.seed(0)
    data = np.random.randn(1000, 2)
    plot_density(data, 'hot')

    







