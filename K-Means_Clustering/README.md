# K-Means Clustering
![K-Means Clustering](img/K-Means_Clustering_Gif.gif)

Coding Popular Machine Learning Algorithms from Scratch

## Algorithms
* [K-Means Clustering](https://github.com/Jadams29/ML_From_Scratch/tree/master/K-Means_Clustering)



Generate K centroids and randomly place on the grid. Iterate over all nodes and assign them to one 
of the centroid based on which is closest to that node. Once all node have been assigned to a centroid, for each
centroid calculate the mean of its assigned nodes. Move the centroid to the mean location. Iterate over the nodes
again and assign them to the closest centroid, repeat until the centroids stop moving location.

(If a centroid does not have nodes assigned to it for an iteration, the centroid should be moved to some random
location. All nodes should be reassigned to the centroids, if situation occurs repeat these steps) 
 
 To determine an optimal number of centroids (K) you can use the elbow method. (DESCRIBE ELBOW METHOD)

## Steps
* Generate K Centroids and randomly assign them locations 
![K-Means Clustering](img/K-Means_Clustering_Plot_1.png | width=100)
# TEST
<img src="img/K-Means_Clustering_Plot_1.png" width="100" height="100">