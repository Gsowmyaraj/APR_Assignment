# Euclidean Distance Calculation and Visualization using Iris Dataset

##Overview

This project demonstrates how to calculate pairwise Euclidean distances between multiple data points and visualize them in a 2D space.
We use the Iris dataset (first 5 data points) and apply the Euclidean distance formula to compute distances between every pair of points.
The output includes:
A printed table of pairwise distances
A 2D scatter plot with distance annotations
This project serves as a foundation for understanding how distance metrics work in machine learning algorithms like k-NN and clustering.

----

##Features

Loads a small dataset (Iris) using sklearn
Calculates Euclidean distance manually (no external distance libraries)
Computes pairwise distances for first 5 points
Generates console output showing distances
Plots data points using Matplotlib
Displays distances on a 2D scatter plot with connecting dashed lines

----

##Tech Stack

Language: Python 3
Libraries Used:
numpy – For basic array handling
matplotlib – For visualization
scikit-learn – To load the Iris dataset
math – For square root calculations

-----

##Installation

1. Install Python 3
2. Install required libraries using pip:
   ```bash 
pip install numpy matplotlib scikit-learn

---

##Usage

1. Run the script in your terminal or IDE:
  ``bash
python euclidean_distance.py
 * You will see:
Console Output: Pairwise Euclidean distances
Plot Window: Scatter plot with points, connecting lines, and distance labels

---

##Methodology

1.Dataset Selection:
Loaded the Iris dataset using sklearn.datasets.load_iris().
Selected the first 5 rows to simplify calculations.
2.Euclidean Distance Calculation:
Used the formula
𝑑(𝑃,𝑄)=∑𝑖=1𝑛(𝑥𝑖−𝑦𝑖)2d(P,Q)=i=1∑n(xi​−yi	)2
plemented this manually in Python.
3.Pairwise Distance Computation:
Calculated distances between every unique pair of points.
For 5 points, a total of 10 distances were computed.
4.Visualization:
Plotted points using Sepal Length (x-axis) and Sepal Width (y-axis).
Connected every pair with a dashed line and labeled it with the computed distance.

----

##Output

Sample Console Output:
Distance between Point 0 and Point 1 = 0.5385
Distance between Point 0 and Point 2 = 0.5099
Distance between Point 0 and Point 3 = 0.6481
Distance between Point 0 and Point 4 = 0.1414
...

Sample Visualization:
5 points plotted in 2D space
Dashed lines connecting every pair
Red labels showing distances between points
Shortest line corresponds to smallest distance (0.1414 between point 0 & 4)

----

##Results

Closest Points: Point 0 & Point 4 (Distance = 0.1414)
Farthest Points: Point 0 & Point 3 / Point 3 & Point 4 (Distance ≈ 0.6481)=
The visualization confirmed the numerical results — shorter lines represent closer points.
This approach can be extended to k-Nearest Neighbors, clustering, and other ML algorithms requiring distance metrics.

