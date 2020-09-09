If you run the program, the first thing it plots is the orgininal 
data points. 

The second Thing it does is seperate the data into two colors since
from just observing the data points we can tell there will be 
at least two clusters. Since the colors are overlaping neither V1 or V2
are being neglected. 

After standerdizing the variables I used the Elbow Method
to find the value for K or how many clusters there are in these 
data sets. The end of the elbow shows 6. K = 6, thus the number of 
clusters for the optimal value for the data sets are 6. Which can be 
seen in the Elbow Method graph.

After finding that it has 6 clusters I updated the plot showing where
the 6 different clusters are located in the graph.

Extra:
After doing a little research I learned that the elbow method is sometimes ambiguous, 
if I had more time I would have liked to use the average silhouette method, 
and Gap statistic method to double check my work. 

CITED WORK

How to find the Optimal number of Clusters:
	- https://www.datanovia.com/en/lessons/determining-the-optimal-number-of-clusters-3-must-know-methods/


existing code:
	- https://medium.com/code-to-express/k-means-clustering-for-beginners-using-python-from-scratch-f20e79c8ad00
	
how to read a csv file
	- https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
	
What is a K-Mean and how to read it
	- https://analyticsindiamag.com/beginners-guide-to-k-means-clustering/#:~:text=An%20ideal%20way%20to%20figure,is%20to%20minimise%20the%20sum.
	