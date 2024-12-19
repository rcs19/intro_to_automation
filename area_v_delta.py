from miller import flux_surface, area, plot_surface
import matplotlib.pyplot as plt
import numpy as np

def main():
    # x-values; list of deltas to plot
    x_delta_list = np.arange(-1,1.1,0.1)
    # y-values; calculated from list of deltas
    areas = []
    for d in x_delta_list:
        R, Z = flux_surface(delta=d)
        areas.append(area(R, Z))

    fig, ax = plt.subplots()
    ax.plot(x_delta_list, areas, label="Area")
    ax.set_xlabel("Delta")
    ax.set_ylabel("Area")

    # R, Z = flux_surface()
    # plot_surface(R, Z, ax=ax)

    plt.show()
    return

if __name__=="__main__":
    main()