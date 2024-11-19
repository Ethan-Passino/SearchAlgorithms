import math


# Linear Search
def linear_search(arr, target):
    """
    Linear Search Algorithm
    -----------------------
    Time Complexity:
        Best Case: O(1) (target is at the beginning)
        Worst Case: O(n) (target is at the end or not found)
    Space Complexity: O(1)
    Use Case:
        - Works on unsorted data
        - Simple to implement but inefficient for large datasets
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search
def binary_search(arr, target):
    """
    Binary Search Algorithm
    -----------------------
    Time Complexity:
        Best Case: O(1) (target is at the middle)
        Worst Case: O(log n)
    Space Complexity:
        Iterative: O(1)
        Recursive: O(log n) (due to recursion stack)
    Use Case:
        - Requires the array to be sorted
        - Highly efficient for large datasets
    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Jump Search
def jump_search(arr, target):
    """
    Jump Search Algorithm
    ---------------------
    Time Complexity:
        Best Case: O(√n) (target found in the first block)
        Worst Case: O(√n)
    Space Complexity: O(1)
    Use Case:
        - Requires the array to be sorted
        - Efficient for large datasets where binary search isn't ideal
    """
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1


# Exponential Search
def exponential_search(arr, target):
    """
    Exponential Search Algorithm
    ----------------------------
    Time Complexity:
        Best Case: O(1) (target is at the first position)
        Worst Case: O(log n) (after the binary search step)
    Space Complexity:
        Iterative Binary Search: O(1)
        Recursive Binary Search: O(log n)
    Use Case:
        - Works well on sorted data
        - Suitable for unbounded or infinite arrays
    """
    if arr[0] == target:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= target:
        i *= 2
    # Binary search in the found range
    return binary_search(arr[:min(i, n)], target)


# Ternary Search
def ternary_search(arr, target, left, right):
    """
    Ternary Search Algorithm
    ------------------------
    Time Complexity:
        Best Case: O(1) (target is at a mid-point)
        Worst Case: O(log n) (similar to binary search but slower)
    Space Complexity:
        Iterative: O(1)
        Recursive: O(log n) (due to recursion stack)
    Use Case:
        - Requires the array to be sorted
        - Rarely used; may be applicable for unimodal arrays
    """
    if right >= left:
        mid1 = left + (right - left) // 3
        mid2 = right - (right - left) // 3

        if arr[mid1] == target:
            return mid1
        if arr[mid2] == target:
            return mid2

        if target < arr[mid1]:
            return ternary_search(arr, target, left, mid1 - 1)
        elif target > arr[mid2]:
            return ternary_search(arr, target, mid2 + 1, right)
        else:
            return ternary_search(arr, target, mid1 + 1, mid2 - 1)
    return -1


# Hash Table Implementation for Search
class HashTable:
    """
    Hash Table Search Algorithm
    ---------------------------
    Time Complexity:
        Average Case: O(1)
        Worst Case: O(n) (due to hash collisions)
    Space Complexity: O(n)
    Use Case:
        - Extremely fast lookups for key-value pairs
        - Commonly used in databases and dictionaries
    """
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def search(self, key):
        return self.table.get(key, -1)  # Return -1 if key not found


# Test the Search Algorithms
if __name__ == "__main__":
    # Test Data
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Linear Search:", linear_search(arr, 5))  # Output: 4
    print("Binary Search:", binary_search(arr, 5))  # Output: 4
    print("Jump Search:", jump_search(arr, 5))     # Output: 4
    print("Exponential Search:", exponential_search(arr, 5))  # Output: 4
    print("Ternary Search:", ternary_search(arr, 5, 0, len(arr) - 1))  # Output: 4

    # Hash Table Test
    hash_table = HashTable()
    hash_table.insert('apple', 1)
    hash_table.insert('banana', 2)
    print("Hash Table Search:", hash_table.search('apple'))  # Output: 1
    print("Hash Table Search (not found):", hash_table.search('grape'))  # Output: -1
