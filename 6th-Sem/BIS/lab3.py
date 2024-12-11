import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score

file_path = "E:/samyak/6th-Sem/6th-Sem/BIS/Lab_3_Data.txt"
data = pd.read_csv(file_path)


# Display the first few rows to verify the data structure
print(data.head())

# Step 2: Preprocess the data
# We will use 'Sales' and 'Profit' for clustering (adjust based on your needs)
features = data[['Sales', 'Profit']]  # Use 'Sales' and 'Profit' columns for clustering

# Standardizing the features (important for K-Means)
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Step 3: Perform K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(features_scaled)

# Print the first few rows with the cluster labels
print(data.head())

# Step 4: Evaluate clustering using silhouette score
silhouette_avg = silhouette_score(features_scaled, data['Cluster'])
print(f'Silhouette Score: {silhouette_avg}')

# Step 5: Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['Sales'], data['Profit'], c=data['Cluster'], cmap='viridis', marker='o')
plt.title('Customer Segments based on Sales and Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')



plt.show()

# Optional: Elbow method for optimal number of clusters
wcss = []  # Within-cluster sum of squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(features_scaled)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method for Optimal Number of Clusters')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS (Within-cluster sum of squares)')
plt.show()
