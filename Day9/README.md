

### What is Clustering?
Clustering is an **unsupervised machine learning** technique used to group similar data points into clusters based on their characteristics. Unlike supervised learning, clustering does not require labeled data. In this project, I used the **K-Means clustering** algorithm to group Iris flowers according to their feature values, allowing similar flowers to be placed in the same cluster.

### What is PCA?

**Principal Component Analysis (PCA)** is a dimensionality reduction technique that transforms a dataset with many features into a smaller set of principal components while preserving as much important information (variance) as possible. In this project, PCA reduced the original four features of the Iris dataset to two principal components (**PC1** and **PC2**), making it easier to visualize the clusters in a two-dimensional space.

### How did you determine the best value of K?

I used the **Elbow Method** to determine the optimal number of clusters. This involved calculating the **Within-Cluster Sum of Squares (WCSS)** for values of **K** ranging from 1 to 10 and plotting the results. The graph showed a clear "elbow" at **K = 3**, indicating that three clusters provide the best balance between minimizing WCSS and avoiding unnecessary complexity.

### What insights did you gain from the visualizations?

The visualizations provided several important insights:

* The **Elbow Method** indicated that **K = 3** is the optimal number of clusters for the Iris dataset.
* **K-Means clustering** successfully grouped the Iris flowers into three distinct clusters based on their feature similarities.
* **PCA** reduced the dataset from four dimensions to two while preserving most of the important information.
* The **PCA scatter plot** provided a clear visualization of the clusters, making it easier to observe the separation and relationships between the grouped Iris flowers.
