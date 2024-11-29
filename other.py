from collections import deque, defaultdict
import heapq

# Bidirectional Search
class BidirectionalSearch:
    def __init__(self, graph):
        self.graph = graph

    def search(self, start, goal):
        """
        Performs Bidirectional Search.
        :param start: Start node.
        :param goal: Goal node.
        :return: List of nodes representing the path, or None if no path exists.
        """
        if start == goal:
            return [start]

        # Frontiers for BFS from start and goal
        frontier_start = {start}
        frontier_goal = {goal}

        # Visited sets and parent dictionaries
        visited_start = {start: None}
        visited_goal = {goal: None}

        while frontier_start and frontier_goal:
            # Expand from start
            path = self._expand_frontier(frontier_start, visited_start, visited_goal)
            if path:
                return path

            # Expand from goal
            path = self._expand_frontier(frontier_goal, visited_goal, visited_start)
            if path:
                return path

        return None  # No path found

    def _expand_frontier(self, frontier, visited, other_visited):
        next_frontier = set()
        for node in frontier:
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited[neighbor] = node
                    next_frontier.add(neighbor)
                if neighbor in other_visited:
                    return self._reconstruct_path(visited, other_visited, neighbor)
        frontier.clear()
        frontier.update(next_frontier)
        return None

    def _reconstruct_path(self, visited_start, visited_goal, meeting_node):
        path = []
        # From start to meeting node
        current = meeting_node
        while current:
            path.append(current)
            current = visited_start[current]
        path.reverse()

        # From meeting node to goal
        current = visited_goal[meeting_node]
        while current:
            path.append(current)
            current = visited_goal[current]

        return path


# Iterative Deepening Search (IDS)
def iterative_deepening_search(graph, start, goal):
    """
    Performs Iterative Deepening Search.
    :param graph: Adjacency list of the graph.
    :param start: Start node.
    :param goal: Goal node.
    :return: List of nodes representing the path, or None if no path exists.
    """
    def dls(node, depth, visited):
        if depth == 0:
            return [node] if node == goal else None
        if depth > 0:
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    path = dls(neighbor, depth - 1, visited)
                    if path:
                        return [node] + path
            visited.remove(node)
        return None

    depth = 0
    while True:
        visited = set()
        path = dls(start, depth, visited)
        if path:
            return path
        depth += 1


# Dijkstra's Algorithm
def dijkstra(graph, start):
    """
    Finds the shortest paths from a starting node using Dijkstra's algorithm.
    :param graph: Weighted adjacency list of the graph.
    :param start: Start node.
    :return: Dictionary of shortest distances to all nodes from the start.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]  # Priority queue as (distance, node)

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Bellman-Ford Algorithm
def bellman_ford(graph, start):
    """
    Solves the single-source shortest path problem using the Bellman-Ford algorithm.
    :param graph: Weighted adjacency list of the graph.
    :param start: Start node.
    :return: Dictionary of shortest distances to all nodes from the start, or None if a negative cycle is detected.
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # Relax edges up to |V| - 1 times
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph[node]:
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    # Check for negative weight cycles
    for node in graph:
        for neighbor, weight in graph[node]:
            if distances[node] + weight < distances[neighbor]:
                return None  # Negative weight cycle detected

    return distances


# Test Cases
if __name__ == "__main__":
    print("Bidirectional Search:")
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

    print("\nIterative Deepening Search:")
    print("Path from A to F:", iterative_deepening_search(graph, 'A', 'F'))  # Output: ['A', 'C', 'F']

    print("\nDijkstra's Algorithm:")
    weighted_graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 6)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 6), ('C', 3)]
    }
    print("Shortest paths from A:", dijkstra(weighted_graph, 'A'))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 6}

    print("\nBellman-Ford Algorithm:")
    weighted_graph_negative = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', -3)],
        'C': [('D', 2)],
        'D': []
    }
    print("Shortest paths from A:", bellman_ford(weighted_graph_negative, 'A'))  # Output: {'A': 0, 'B': 1, 'C': -2, 'D': 0}
