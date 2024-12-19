from numpy import linspace, cos, arcsin, sin, pi
import numpy as np
import matplotlib.pyplot as plt

def flux_surface(A = 2.2,
    kappa = 1.5,
    delta = 0.3,
    R0 = 2.5):
    """
    Create a flux surface
    
    Arguments
    ---------
    A:
        Aspect Ratio
    kappa:
        Elongation
    delta:
        Triangulation
    R0:

    Returns
    -------
    R_s:

    Z_s:

    
    """

    theta = linspace(0, 2 * pi)
    r = R0 / A
    R_s = R0 + r * cos(theta + (arcsin(delta) * sin(theta)))
    Z_s = kappa * r * sin(theta)
    return(R_s, Z_s)

def plot_surface(R_s, Z_s, ax=None, savefig=True):
    """
    Plot Flux Surface
    
    Arguments
    ---------
    R_s:
        R?
    Z_s:
        Z?
    
    """
    if ax is not None:
        ax.plot(R_s, Z_s)
        ax.axis("equal")
        ax.set_xlabel("R [m]")
        ax.set_ylabel("Z [m]")
    else:
        plt.plot(R_s, Z_s)
        plt.axis("equal")
        plt.xlabel("R [m]")
        plt.ylabel("Z [m]")

    if savefig:
        plt.savefig("./miller.png")

def area(r, z):
    # abs because (r, z) start on the out-board midplace and r decreases
    return np.abs(np.trapezoid(z, r))

def main():
    """
    Main code to create a flux surface and plot it
    """
    R_s, Z_s = flux_surface()
    plot_surface(R_s, Z_s)
    print("AREA=",area(R_s, Z_s))

if __name__=="__main__":
    main()