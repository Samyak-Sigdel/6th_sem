

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


file_path = "E:/samyak/6th-Sem/6th-Sem/BIS/Lab_3_Data.txt"
data = pd.read_csv(file_path, delimiter=',') 


# Display the first few rows to verify the data structure
print(data.head())


# Step 2: Preprocess the data
# We will use 'Sales' and 'Profit' for clustering (adjust based on your needs)
features = data[['Sales', 'Profit']]  # Use 'Sales' and 'Profit' columns for clustering


# Standardizing the features (important for K-Means)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)


# Step 3: Perform K-Means clustering with a fixed number of clusters (e.g., 5)
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(features_scaled)


# Step 4: Calculate the Euclidean distance from each point to its respective cluster center
distances = np.linalg.norm(features_scaled - kmeans.cluster_centers_[data['Cluster']], axis=1)


# Add the distance information to the dataframe
data['Distance_to_Center'] = distances


# Print the first few rows with the cluster labels and distances
print(data[['CustomerID', 'Sales', 'Profit', 'Cluster', 'Distance_to_Center']].head())


# Step 5: Evaluate clustering using silhouette score
silhouette_avg = silhouette_score(features_scaled, data['Cluster'])
print(f'Silhouette Score: {silhouette_avg}')


# Step 6: Visualize the clusters with Customer IDs displayed
plt.figure(figsize=(10, 8))


# Define custom colors for the clusters (dynamically generated based on n_clusters)
n_clusters = kmeans.n_clusters
cluster_colors = plt.cm.get_cmap('tab10', n_clusters)  # Generate colors from the 'tab10' colormap


# Scatter plot of Sales vs Profit, color-coded by cluster
scatter = plt.scatter(data['Sales'], data['Profit'], c=data['Cluster'], cmap=cluster_colors, marker='o')


# Annotate each point with the corresponding CustomerID
for i, customer_id in enumerate(data['CustomerID']):
    plt.annotate(f'{customer_id}', (data['Sales'][i], data['Profit'][i]), fontsize=8, color='black', alpha=0.7)


# Add labels, a color bar, and a legend
plt.title('Customer Segments based on Sales and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')




# Add a legend for each cluster
handles, labels = plt.gca().get_legend_handles_labels()
for i in range(n_clusters):  # Dynamically handle the number of clusters
    handles.append(plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=cluster_colors(i), markersize=10))
    labels.append(f"Cluster {i+1}")


plt.legend(handles=handles, labels=labels)


# Show the plot
plt.show()




