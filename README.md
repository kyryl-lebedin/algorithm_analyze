# Algorithm Complexity ML Classifier

The objective of this website is to determine the complexity of an input algorithm in the form of a Python function using machine learning.

To start the server from your local machine, in the project directory run: 
```bash
py manage.py runserver
```


The model uses a **Random Forest** algorithm for training. The selected features are the coefficients of a third-degree polynomial, fitted to the size-time graph to represent the complexity of various algorithms.

To standardize the data, it was normalized by removing the mean and scaling it to unit variance. The training data was generated from various algorithms and randomized to eliminate statistical bias. The model was tested on 20% of the data. It is trained to classify into only five main complexity classes:

- Constant
- Linear
- Polynomial
- Logarithmic
- Log-linear

**Note:** This model is not trained to recognize any other classes beyond the five listed above.

## Model Performance:

| Class          | Precision | Recall  | F1-Score | Support |
| -------------- | --------- | ------- | -------- | ------- |
| 0 (Constant)   | 1.00      | 1.00    | 1.00     | 32      |
| 1 (Linear)     | 0.98      | 0.91    | 0.94     | 45      |
| 2 (Polynomial) | 0.95      | 0.95    | 0.95     | 42      |
| 3 (Logarithmic)| 0.97      | 0.97    | 0.97     | 39      |
| 4 (Log-linear) | 0.91      | 0.98    | 0.94     | 42      |

**Overall Accuracy:** **0.96**

**Macro Average:** 0.96 precision, 0.96 recall, 0.96 F1-score

**Weighted Average:** 0.96 precision, 0.96 recall, 0.96 F1-score

## Algorithm Type

Select the algorithm type you wish to analyze. You can choose from pre-defined types, which come with specific inputs, or write a custom algorithm and choose the input format that suits your needs.

## Input Type

- **Array:** Python list with random numbers.
- **Array & Random Index:** Python list with an additional random index within the range of the list.
- **nxn Matrix:** List of n lists, each containing random numbers, where the size is n.
- **Simple Graph:** Adjacency matrix representing a graph.

## Input Size

You can modify the input size to observe how it influences the runtime of algorithms. For complex algorithms, such as those with exponential, higher polynomial, or factorial complexities, it is recommended to reduce the input size to avoid exceeding time limits. For these cases, an input size of **5-20** is optimal.

## Example Algorithms

Here are popular algorithms from each category for testing the model. Expected time complexities are provided:

### Sorting Algorithms:

- **Bubble Sort:** Polynomial (O(n²))
- **Selection Sort:** Polynomial (O(n²))
- **Quick Sort:** Log-linear (O(n log n) on average, O(n²) worst case)
- **Merge Sort:** Log-linear (O(n log n))

### Searching Algorithms:

- **Linear Search:** Linear (O(n))
- **Binary Search:** Logarithmic (O(log n))

### Selecting Algorithms:

- **Quick Select:** Linear (O(n) on average, O(n²) worst case)
- **Median of Medians:** Linear (O(n))

### Matrix Algorithms:

- **Matrix Transpose:** Linear (O(n²)) where n is the size of the matrix (nxn)
- **Frobenius Norm:** Linear (O(n²)) where n is the size of the matrix (nxn)

### Graph Algorithms:

- **Depth First Search (DFS):** Linear (O(V + E)) where V is vertices and E is edges.
- **Breadth First Search (BFS):** Linear (O(V + E))
- **Dijkstra's Algorithm:** Log-linear (O((V + E) log V)) with priority queue optimization


