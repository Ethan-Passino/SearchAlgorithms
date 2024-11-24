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

## **How to Use 🛠️**

Each algorithm is implemented as a standalone function. Simply call the function with your dataset and target value. Here’s an example:

```python
# Linear and Binary Search
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Linear Search:", linear_search(arr, 5))  # Output: 4
print("Binary Search:", binary_search(arr, 5))  # Output: 4

# Hash Table Search
hash_table = HashTable()
hash_table.insert('apple', 1)
print("Hash Table Search:", hash_table.search('apple'))  # Output: 1

# Binary Search Tree (BST) Search
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
print("Searching for 15 in BST:", "Found" if bst.search(15) else "Not Found")  # Output: Found

# A* Search
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 3)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}
heuristic = {'A': 6, 'B': 4, 'C': 5, 'D': 2, 'E': 2, 'F': 3, 'G': 0}
astar = AStar(graph, heuristic)
print("Path from A to G:", astar.search('A', 'G'))  # Output: ['A', 'B', 'E', 'G']

```

## Running Results 🖥️

When you run the script, it will display the results of all search algorithms with pre-defined test data. Here's an example of the output:
![image](https://github.com/user-attachments/assets/14afe147-cad1-451f-84f4-9405eec44590)

![8mcsD1y](https://github.com/user-attachments/assets/0073e271-d055-4b11-b0db-32649b7e7bea)

![image](https://github.com/user-attachments/assets/2bfe2a54-732a-4e8a-8bfa-159b77733fd4)



