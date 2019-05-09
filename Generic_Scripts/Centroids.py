
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
