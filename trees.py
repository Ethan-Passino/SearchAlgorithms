from collections import deque

# Binary Search Tree (BST) Implementation
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        """Inserts a new key into the BST."""
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        """Searches for a key in the BST."""
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)


# Graph Implementation for DFS and BFS
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        """Adds a directed edge from node u to node v."""
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def dfs(self, start, visited=None):
        """Performs Depth-First Search (DFS) from a starting node."""
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.adjacency_list.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        """Performs Breadth-First Search (BFS) from a starting node."""
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            current = queue.popleft()
            print(current, end=" ")

            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Test Cases
if __name__ == "__main__":
    # Test Binary Search Tree
    print("Binary Search Tree:")
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)

    # Test BST Search
    print("Searching for 7:", "Found" if bst.search(7) else "Not Found")  # Output: Found
    print("Searching for 12:", "Found" if bst.search(12) else "Not Found")  # Output: Not Found

    # Test Graph with DFS and BFS
    print("\nGraph Traversal:")
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)
    graph.add_edge(3, 7)

    print("DFS starting from node 1:")
    graph.dfs(1)  # Output: 1 2 4 5 3 6 7

    print("\nBFS starting from node 1:")
    graph.bfs(1)  # Output: 1 2 3 4 5 6 7
