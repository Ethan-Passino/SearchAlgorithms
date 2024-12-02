# **Search Algorithms in Python 🧠⚡**

Welcome to the **Search Algorithms in Python** repository! This project showcases the implementation of some of the most fundamental and efficient search algorithms in computer science. Each algorithm is written in Python, with detailed comments explaining their **time complexity**, **space complexity**, and **use cases**. Perfect for learning and experimentation! 🚀

---

## **Algorithms Implemented 📚**

### **1. Linear Search**
- **Description**: Sequentially checks each element until the target is found.
- **Best Use**: Small or unsorted datasets.
- **Time Complexity**: O(n)

---

### **2. Binary Search**
- **Description**: Divides a sorted list into halves to find the target.
- **Best Use**: Large sorted datasets.
- **Time Complexity**: O(log n)

---

### **3. Jump Search**
- **Description**: Skips blocks of elements and performs linear search within a block.
- **Best Use**: Sorted datasets.
- **Time Complexity**: O(√n)

---

### **4. Exponential Search**
- **Description**: Finds a range for the target and uses binary search within it.
- **Best Use**: Sorted datasets, especially unbounded arrays.
- **Time Complexity**: O(log n)

---

### **5. Ternary Search**
- **Description**: Splits the array into three parts and searches within the relevant section.
- **Best Use**: Sorted datasets or unimodal arrays.
- **Time Complexity**: O(log n)

---

### **6. Hash Table Search**
- **Description**: Uses hashing for direct access to elements.
- **Best Use**: Key-value lookups in dictionaries or databases.
- **Time Complexity**: O(1) (average), O(n) (worst)

---

### **7. Binary Search Tree (BST) Search**
- **Description**: Searches a binary search tree by traversing left or right depending on the target's value relative to the node.
- **Best Use**: Dynamic datasets with frequent insertions and deletions.
- **Time Complexity**: 
  - Best Case: O(log n)
  - Worst Case: O(n) (for unbalanced trees)
- **Space Complexity**: 
  - Recursive: O(log n)
  - Iterative: O(1)

---

### **8. Depth-First Search (DFS)**
- **Description**: Explores as far as possible along each branch before backtracking.
- **Best Use**: Graph traversal; useful for paths and connectivity.
- **Time Complexity**: O(V + E) (V = vertices, E = edges)
- **Space Complexity**: O(V)

---

### **9. Breadth-First Search (BFS)**
- **Description**: Explores all neighbors of a node before moving to the next level.
- **Best Use**: Shortest path in unweighted graphs.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

---

### **10. A* Search**
- **Description**: Combines BFS with heuristics to find the shortest path efficiently in a weighted graph.
- **Best Use**: Pathfinding (e.g., in games and navigation systems).
- **Time Complexity**: O(E) (E = edges)
- **Space Complexity**: O(V)

---

### **11. Fibonacci Search**
- **Description**: A variant of binary search using Fibonacci numbers to divide the search range.
- **Best Use**: Works well on sorted datasets where the dataset size is known.
- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

---

### **12. Knuth-Morris-Pratt (KMP) Algorithm**
- **Description**: Used for pattern searching in strings by preprocessing the pattern to skip unnecessary comparisons.
- **Best Use**: String matching.
- **Time Complexity**: O(n + m) (n = text length, m = pattern length)
- **Space Complexity**: O(m)

---

### **13. Binary Search in 2D Matrix**
- **Description**: Performs a binary search in a row-wise or column-wise sorted 2D matrix.
- **Best Use**: Efficient search in grid data.
- **Time Complexity**: O(log(mn)) (m = rows, n = columns)
- **Space Complexity**: O(1)

---

### **14. Bidirectional Search**
- **Description**: Searches from both the start and goal nodes, meeting in the middle.
- **Best Use**: Pathfinding when start and goal are both defined.
- **Time Complexity**: O(b^(d/2)) (b = branching factor, d = depth of the solution)
- **Space Complexity**: O(b^(d/2))

---

### **15. Iterative Deepening Search (IDS)**
- **Description**: Combines the space efficiency of DFS with the optimality of BFS by incrementally increasing the depth limit.
- **Best Use**: When the depth of the solution is unknown.
- **Time Complexity**: O(b^d)
- **Space Complexity**: O(d)

---

### **16. Dijkstra's Algorithm**
- **Description**: Finds the shortest path in a graph with non-negative weights.
- **Best Use**: Weighted graphs for single-source shortest path problems.
- **Time Complexity**: O(V^2) (or O((V + E) log V) with a priority queue)
- **Space Complexity**: O(V + E)

---

### **17. Bellman-Ford Algorithm**
- **Description**: Solves the single-source shortest path problem in graphs with negative weights.
- **Best Use**: Weighted graphs where edge weights may be negative.
- **Time Complexity**: O(VE)
- **Space Complexity**: O(V)

---

## **How to Use 🛠️**

Each algorithm is implemented as a standalone function. Simply call the function with your dataset and target value. Here’s an example:

```python
# Dijkstra's Algorithm
weighted_graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}
print("Shortest paths from A:", dijkstra(weighted_graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}

# Bidirectional Search
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
bi_search = BidirectionalSearch(graph)
print("Path from A to F:", bi_search.search('A', 'F'))  # Output: ['A', 'C', 'F']

```

## Running Results 🖥️

When you run the script, it will display the results of all search algorithms with pre-defined test data.
![image](https://github.com/user-attachments/assets/14afe147-cad1-451f-84f4-9405eec44590)

![8mcsD1y](https://github.com/user-attachments/assets/0073e271-d055-4b11-b0db-32649b7e7bea)

![image](https://github.com/user-attachments/assets/2bfe2a54-732a-4e8a-8bfa-159b77733fd4)

![KT5YfSA](https://github.com/user-attachments/assets/8abc0baf-6f90-4332-8695-352840508b44)



