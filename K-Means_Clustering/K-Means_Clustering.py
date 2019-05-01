from scripts import*
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import cm


if __name__ == "__main__":
    testing = True
    if not testing:
        generate_data = input("Would you like to generate data? (Yes or No)")

        if generate_data.lower() in ['yes', 'y']:
            dimensions = input("Enter the dimensions for your data. (eg. 3 3 3 would be a 3 by 3 by 3 matrix)")

    nodes = np.random.randint(0, 1000, size=(2, 500))
    # We are vectorizing the Node class ~~ [Node(), Node(),Node(),...,(n+1)Node()]
    Node_Mapper = np.vectorize(Node)
    # We are passing in the two arrays generated in nodes
    Nodes = Node_Mapper(nodes[0], nodes[1])
    # We are vectorizing the distance function ~~ [distance(), distance(), ..., (n+1)distance()]
    Distance_Mapper = np.vectorize(distance)
    # Initialize k
    k = 6
    if k > 6:
        # Specify the color mapping based on k
        cmap = cm.get_cmap('gist_ncar')
    else:
        cmap = cm.get_cmap('gist_rainbow')
    # Generate a color_list that will be used for assigning colors to the different centroids
    color_list = [cmap(np.random.randint(0, 100)) for i in range(k)]

    # Generate K number of Randomly Generated Centroids
    Centroids = Create_K_Centroids(k, k_centroids=np.random.randint(0, 1000, size=(2, k)), colors=color_list)
    previous_centroid_cords = []
    initial = False
    for temp in range(51):
        with plt.style.context('bmh'):
            if temp == 0:
                initial = True
            else:
                initial = False
            fig, ax = plt.subplots()  # Create a new plot for each iteration

            # Generate a list of of centroid coordinates
            temp_centroid_cords = [[i.x, i.y] for i in Centroids]
            # Check if the current cords have previously been used, if so we break, else we continue through
            if temp_centroid_cords in previous_centroid_cords:
                # The centroids did not move
                break
            else:
                previous_centroid_cords.append(temp_centroid_cords)

            # Determine which centroid each node belows to.
            node_distribution = np.asarray([np.argmin(Distance_Mapper(i, Centroids)) for i in Nodes])
            plot_key_list = ["Centroid_{}".format(i + 1) for i in range(len(Centroids))]
            # Distribute the nodes to their respective centroids
            distribute_nodes(Centroids, nodes=nodes, nodes_final_location=node_distribution,
                             subplot=ax, plot_key_list=plot_key_list, initial=initial)
            # Establish the title for the scatter plot
            plt.title('K-Means Clustering')
            ax.legend(loc='upper center', bbox_to_anchor=(1.0, 1.0), shadow=True, ncol=1, prop={'size': 8})
            ax.grid(True)
            plt.savefig("img/K-Means_Clustering_Plot_{}.png".format(temp))
            plt.show()

            print()



    print("Finished")
