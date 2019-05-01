import math
import numpy as np

color_list_1 = ["blue", "green", "red", "brown", "magenta", "orange", "black"]

class Centroid:
    def __init__(self, nodes=[], name=None, centroid_node=None, centroid_color='black', node_color='black', mean=None):
        self.nodes = nodes
        self.name = name
        self.centroid_node = centroid_node
        self.centroid_color = centroid_color
        self.node_color = node_color
        self.x = self.centroid_node.x
        self.y = self.centroid_node.y
        self.mean = mean

    def describe(self):
        print()
        print("Centroid_{}".format(self.name))
        print("Centroid_Node: {},{}".format(self.centroid_node.x, self.centroid_node.y))
        if len(self.nodes) >= 2:
            if len(self.nodes[0][0]) > 5:
                print("Nodes: {}".format(np.asarray(self.nodes).shape))
        else:
            print("Nodes: {}".format(self.nodes))
        print("Node Color: {}".format(self.node_color))
        if self.mean is not None:
            print("Mean: {},{}".format(self.mean.x, self.mean.y))
        print()
        return


class Node:
    def __init__(self, x=0, y=0, centroid=None):
        self.x = float(x)
        self.y = float(y)
        self.centroid = centroid

    def set_centroid(self, centroid):
        self.centroid = centroid


def distance(node1, node2):
    # sqrt( (X1-X2)^2 + (Y1-Y2)^2 )
    return math.sqrt(math.pow((node1.x - node2.x), 2) + math.pow((node1.y - node2.y), 2))


def distance1(x1, y1, centroid):
    # sqrt( (X1-X2)^2 + (Y1-Y2)^2 )
    return math.sqrt(math.pow((x1 - centroid.x), 2) + math.pow((y1 - centroid.y), 2))


def Create_K_Centroids(number_of_centroids, k_centroids, colors):
    centroid_array = []
    for i in range(number_of_centroids):
        centroid = Centroid([], name=str(i), centroid_node=Node(k_centroids[0][i], k_centroids[1][i]),
                            centroid_color=color_list_1[i], node_color=color_list_1[i])
        centroid_array.append(centroid)
    return np.asarray(centroid_array)


def distribute_nodes(centroids, nodes, nodes_final_location, subplot, plot_key_list, initial=False):

    for i in range(len(centroids)):
        t = np.where(nodes_final_location == i)
        t_0 = nodes[:, t]
        centroids[i].nodes = np.asarray([t_0[0], t_0[1]])
        if initial:
            node_color = 'black'
        else:
            node_color = centroids[i].centroid_color
        edgecolors = "black"

        # Adding the nodes to the Scatterplot
        subplot.scatter(centroids[i].nodes[0], centroids[i].nodes[1],
                        c=node_color, label=plot_key_list[i], alpha=0.3, edgecolors=edgecolors)
        # Adding the Centroids to the Scatterplot
        subplot.scatter([centroids[i].centroid_node.x], [centroids[i].centroid_node.y],
                        c=centroids[i].centroid_color, s=300,
                        edgecolors=edgecolors, alpha=0.7)
        avg_x, avg_y = np.mean(centroids[i].nodes[0]), np.mean(centroids[i].nodes[1])
        centroids[i].centroid_node = Node(x=int(avg_x), y=int(avg_y))
        centroids[i].mean = Node(x=int(avg_x), y=int(avg_y))
        centroids[i].x = int(avg_x)
        centroids[i].y = int(avg_y)
        centroids[i].nodes = []
    return


# def quick_k_means(k, data, centroids, dist_mapper):
#     # K = the number of centroids to make
#     # data = Nodes
#     # Centroids = Starting Centroids
#     prev_locations = []
#     for k in range(51):
#         temp_locations = [[i.centroid_node.x, i.centroid_node.y] for i in centroids]
#         if temp_locations in prev_locations:
#             break
#         else:
#             node_grouping = np.asarray([np.argmin(dist_mapper(i, centroids)) for i in data])
#             for cent in range(len(centroids)):
#                 avg_x = data[np.where(node_grouping==cent)]
#                 print()
#
#     print()


    return
