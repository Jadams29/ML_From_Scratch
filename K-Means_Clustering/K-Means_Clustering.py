from scripts import*
import numpy as np
import pandas
import random
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

from itertools import cycle

if __name__ == "__main__":
    testing = True
    if not testing:
        generate_data = input("Would you like to generate data? (Yes or No)")

        if generate_data.lower() in ['yes', 'y']:
            dimensions = input("Enter the dimensions for your data. (eg. 3 3 3 would be a 3 by 3 by 3 matrix)")

    nodes = np.random.randint(0, 1000, size=(2, 500))
    Node_Mapper = np.vectorize(Node)

    Nodes = Node_Mapper(nodes[0], nodes[1])
    Distance_Mapper = np.vectorize(distance)
    k = 5
    if k > 6:
        cmap = cm.get_cmap('gist_ncar')
    else:
        cmap = cm.get_cmap('gist_rainbow')
    color_list = [cmap(np.random.random()) for i in range(k)]


    # Generate K number of Randomly Generated Centroids
    Centroids = Create_K_Centroids(k, k_centroids=np.random.randint(0, 1000, size=(2, k)), colors=color_list)
    previous_centroid_cords = []

    for temp in range(50):
        fig, ax = plt.subplots()        # Create a new plot for each iteration
        temp_centroid_cords = [[i.x, i.y] for i in Centroids]
        if temp_centroid_cords in previous_centroid_cords:
            break
        else:
            previous_centroid_cords.append(temp_centroid_cords)
        node_distribution = np.asarray([np.argmin(Distance_Mapper(i, Centroids)) for i in Nodes])
        plot_key_list = ["Centroid_{}".format(i + 1) for i in range(len(Centroids))]
        distribute_nodes(Centroids, nodes=nodes, nodes_final_location=node_distribution,
                         subplot=ax, plot_key_list=plot_key_list)
        plt.title("K-Means Clustering")
        ax.legend()
        ax.grid(True)
        plt.show()
        for c in range(len(Centroids)):
            Centroids[c].describe()
        print()

    print("Finished")
