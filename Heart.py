import numpy as np
import matplotlib.pyplot as plt

def plottingHeartFunction(X,Y):
    # Heart equation
    F = (X**2 + Y**2 - 1)**3 - X**2 * Y**3

    # Plot the contour where F = 0
    plt.contour(X, Y, F, levels=[0], colors='red')

    plt.title("Heart Shape using Cartesian Equation", fontsize=12)

    # Show the plot
    plt.show()
def initializeValues():
    # Defined the grid of points
    x = np.linspace(-1.5, 1.5, 400)
    y = np.linspace(-1.5, 1.5, 400)
    return np.meshgrid(x, y)

if __name__ == '__main__':
    X,Y = initializeValues()
    plottingHeartFunction(X,Y)
    
