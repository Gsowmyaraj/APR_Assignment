import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from math import sqrt

# Load Iris dataset
iris = load_iris()
data = iris.data[:5]  # Take first 5 data points for simplicity
labels = iris.target[:5]

# Function to compute Euclidean distance
def euclidean_distance(point1, point2):
    return sqrt(sum((p1 - p2) ** 2 for p1, p2 in zip(point1, point2)))

# Calculate pairwise distances
print("Pairwise Euclidean Distances:\n")
n = len(data)
distances = []
for i in range(n):
    for j in range(i + 1, n):
        dist = euclidean_distance(data[i], data[j])
        distances.append((i, j, dist))
        print(f"Distance between Point {i} and Point {j} = {dist:.4f}")

# Visualization (Using first 2 features for 2D plotting)
plt.figure(figsize=(8, 6))
plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', s=100, edgecolors='k')

# Annotate points with their index
for idx, (x, y) in enumerate(zip(data[:, 0], data[:, 1])):
    plt.text(x + 0.02, y + 0.02, str(idx), fontsize=12)

# Draw lines between points with distance labels
for i, j, dist in distances:
    x_coords = [data[i, 0], data[j, 0]]
    y_coords = [data[i, 1], data[j, 1]]
    plt.plot(x_coords, y_coords, 'gray', linestyle='--', alpha=0.5)
    mid_x = (x_coords[0] + x_coords[1]) / 2
    mid_y = (y_coords[0] + y_coords[1]) / 2
    plt.text(mid_x, mid_y, f"{dist:.2f}", fontsize=8, color='red')

plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Iris Dataset (First 5 Points) with Euclidean Distances')
plt.grid(alpha=0.3)
plt.show()
