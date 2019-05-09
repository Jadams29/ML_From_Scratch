
class Node:
    def __init__(self, x=0, y=0, centroid=None):
        self.x = float(x)
        self.y = float(y)
        self.centroid = centroid

    def set_centroid(self, centroid):
        self.centroid = centroid
