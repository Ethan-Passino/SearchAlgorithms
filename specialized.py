import heapq


# A* Search Algorithm
class AStar:
    def __init__(self, graph, heuristic):
        """
        Initializes the A* Search algorithm.
        :param graph: Dictionary representing the adjacency list of the graph.
        :param heuristic: Dictionary of heuristic costs for each node.
        """
        self.graph = graph
        self.heuristic = heuristic

    def search(self, start, goal):
        """
        Performs the A* search algorithm to find the shortest path.
        :param start: Starting node.
        :param goal: Goal node.
        :return: List representing the path from start to goal, or None if no path exists.
        """
        open_set = []  # Priority queue for nodes to be evaluated
        heapq.heappush(open_set, (0, start))  # Add the start node with priority 0
        came_from = {}  # Tracks the optimal path
        g_score = {node: float('inf') for node in self.graph}  # Cost from start to node
        g_score[start] = 0
        f_score = {node: float('inf') for node in self.graph}  # Estimated total cost
        f_score[start] = self.heuristic[start]

        while open_set:
            _, current = heapq.heappop(open_set)  # Get the node with the lowest f_score

            if current == goal:
                return self._reconstruct_path(came_from, current)

            for neighbor, weight in self.graph[current]:
                # Tentative g_score for the neighbor
                tentative_g_score = g_score[current] + weight
                if tentative_g_score < g_score[neighbor]:
                    # Update path and scores
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + self.heuristic[neighbor]
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))

        return None  # No path found

    def _reconstruct_path(self, came_from, current):
        """
        Reconstructs the path from start to goal.
        :param came_from: Dictionary of previous nodes.
        :param current: Current goal node.
        :return: List representing the path from start to goal.
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


# Fibonacci Search
def fibonacci_search(arr, target):
    """
    Performs Fibonacci Search on a sorted array.
    :param arr: List of sorted elements.
    :param target: Element to search for.
    :return: Index of the target element, or -1 if not found.
    """
    n = len(arr)
    fib2, fib1 = 0, 1  # Fibonacci numbers: fib2 = F(k-2), fib1 = F(k-1)
    fib = fib2 + fib1  # F(k)

    # Generate the smallest Fibonacci number greater than or equal to n
    while fib < n:
        fib2, fib1 = fib1, fib
        fib = fib2 + fib1

    offset = -1  # Marks the eliminated range

    while fib > 1:
        i = min(offset + fib2, n - 1)  # Index to be compared

        if arr[i] < target:
            # Move the range one Fibonacci step ahead
            fib, fib1, fib2 = fib1, fib2, fib - fib1
            offset = i
        elif arr[i] > target:
            # Move the range one Fibonacci step back
            fib, fib1, fib2 = fib2, fib - fib1, fib1 - fib2
        else:
            return i  # Target found

    # Check the last element
    if fib1 and offset + 1 < n and arr[offset + 1] == target:
        return offset + 1

    return -1  # Target not found


# Knuth-Morris-Pratt (KMP) Algorithm
def kmp_search(text, pattern):
    """
    Performs the KMP pattern searching algorithm.
    :param text: The main string where the pattern is to be searched.
    :param pattern: The pattern to be searched.
    :return: Starting index of the pattern in the text, or -1 if not found.
    """
    def compute_lps(pattern):
        """
        Computes the Longest Prefix Suffix (LPS) array.
        :param pattern: The pattern for which LPS is computed.
        :return: LPS array.
        """
        lps = [0] * len(pattern)
        length = 0  # Length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    i = j = 0  # Pointers for text and pattern

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):  # Full pattern matched
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # No match found


# Binary Search in 2D Matrix
def search_2d_matrix(matrix, target):
    """
    Searches for a target value in a 2D matrix sorted row-wise and column-wise.
    :param matrix: 2D matrix.
    :param target: Value to search for.
    :return: True if the target is found, False otherwise.
    """
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = matrix[mid // cols][mid % cols]  # Get the mid element

        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


# Test Cases
if __name__ == "__main__":
    # A* Search Test
    print("A* Search:")
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

    # Fibonacci Search Test
    print("\nFibonacci Search:")
    arr = [1, 3, 7, 15, 18, 22, 30]
    print("Index of 15:", fibonacci_search(arr, 15))  # Output: 3
    print("Index of 8:", fibonacci_search(arr, 8))  # Output: -1

    # KMP Search Test
    print("\nKMP Algorithm:")
    text = "ababcabcabababd"
    pattern = "ababd"
    print("Pattern found at index:", kmp_search(text, pattern))  # Output: 10

    # Binary Search in 2D Matrix Test
    print("\nBinary Search in 2D Matrix:")
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    print("Target 9 found:", search_2d_matrix(matrix, 9))  # Output: True
    print("Target 8 found:", search_2d_matrix(matrix, 8))  # Output: False
