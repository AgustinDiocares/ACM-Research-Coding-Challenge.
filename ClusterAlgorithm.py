# Import the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from sklearn.cluster import KMeans

# Reading in the csv data file
data = pd.read_csv("ClusterPlot.csv")
data

# Plotting data like the example provided
plt.scatter(data['V1'], data['V2'])
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

x = data.copy()

# Clustering
kmeans = KMeans(2)
kmeans.fit(x)

# Clustering results
clusters = x.copy()
clusters['cluster_pred'] = kmeans.fit_predict(x)

# Plot with color
plt.scatter(clusters['V1'], clusters['V2'], c=clusters['cluster_pred'], cmap='rainbow')
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

# Standardizing the variable
from sklearn import preprocessing
x_scaled = preprocessing.scale(x)
x_scaled

# The Elbow Method
# The elbow method does is it starts of with making one cluster to the number of clusters
# in our sample and with the kmeans inertia value we determine what would be the appropriate number of clusters.
wss = []   # WSS stands for Within-Cluster-Sum-of-Squares

for i in range(1, 25):
    kmeans = KMeans(i)
    kmeans.fit(x_scaled)
    wss.append(kmeans.inertia_)
wss

# Visualizing the Elbow Method
plt.plot(range(1, 25), wss)
plt.xlabel('Number of clusters')
plt.ylabel('WSS')
plt.show()

# Stronger Clustering
kmeans_new = KMeans(6)
kmeans.fit(x_scaled)
cluster_new = x.copy()
cluster_new['cluster_pred'] = kmeans_new.fit_predict(x_scaled)
cluster_new

# Plotting the newly cluster
plt.scatter(cluster_new['V1'], cluster_new['V2'], c= cluster_new['cluster_pred'], cmap= 'rainbow')
plt.xlabel('V1')
plt.ylabel('V2')
plt.show()

# Analysis
