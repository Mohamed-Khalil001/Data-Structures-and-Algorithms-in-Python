# Linear Search and Binary Search Lecture Code
# Implements searching algorithms for financial data.
# Time Complexity: Analyzed per function.
# Example: Searching stock prices in quantitative analysis.

# --------------------------------------------
# Concept: Searching Algorithms
# Definition: Methods to find an element in a collection of data (e.g., a list).
# Algorithms Covered:
# - Linear Search: Iterates through each element until the target is found or the list ends.
# - Binary Search: Divides a sorted list in half each time to find the target.
# Properties:
# - Linear Search:
#   - Works on any list (sorted or unsorted).
#   - Returns True/False or index if target is found.
#   - Time Complexity: O(n), where n is list size.
# - Binary Search:
#   - Requires a sorted list.
#   - Returns True/False or index if target is found.
#   - Time Complexity: O(log n), much faster for large lists.
# Use Case: Finding specific stock prices or transactions in financial datasets.
# --------------------------------------------

class FinancialSearch:
    def linear_search(self, prices, target):
        """
        Performs linear search to find target in prices.
        Time Complexity: O(n)
        """
        for i in range(len(prices)):  # Loop through each index
            if prices[i] == target:  # Check if current price is target
                return True  # Found target, return True
        return False  # Target not found, return False

    def linear_search_index(self, prices, target):
        """
        Performs linear search and returns index of target.
        Time Complexity: O(n)
        """
        for i in range(len(prices)):  # Loop through each index
            if prices[i] == target:  # Check if current price is target
                return i  # Return index of target
        return -1  # Target not found, return -1

    def binary_search(self, prices, target):
        """
        Performs binary search on sorted prices to find target.
        Time Complexity: O(log n)
        """
        first = 0  # Start of search range
        last = len(prices) - 1  # End of search range
        while first <= last:  # Continue while range is valid
            middle = (first + last) // 2  # Calculate middle index
            if prices[middle] == target:  # If middle element is target
                return True  # Found target, return True
            elif prices[middle] > target:  # If target is smaller
                last = middle - 1  # Search left half
            else:  # If target is larger
                first = middle + 1  # Search right half
        return False  # Target not found, return False

    def binary_search_index(self, prices, target):
        """
        Performs binary search and returns index of target.
        Time Complexity: O(log n)
        """
        first = 0  # Start of search range
        last = len(prices) - 1  # End of search range
        while first <= last:  # Continue while range is valid
            middle = (first + last) // 2  # Calculate middle index
            if prices[middle] == target:  # If middle element is target
                return middle  # Return index of target
            elif prices[middle] > target:  # If target is smaller
                last = middle - 1  # Search left half
            else:  # If target is larger
                first = middle + 1  # Search right half
        return -1  # Target not found, return -1

# Testing
search = FinancialSearch()

# Linear Search
prices_unsorted = [300.75, 100.00, 200.50]
print("Linear Search (200.50):", search.linear_search(prices_unsorted, 200.50))  # Output: True
# How it works: Checks 300.75, 100.00, then finds 200.50
print("Linear Search Index (200.50):", search.linear_search_index(prices_unsorted, 200.50))  # Output: 2
# How it works: Returns index 2 where 200.50 is found

# Binary Search
prices_sorted = [100.00, 200.50, 300.75, 400.00, 500.25]
print("Binary Search (300.75):", search.binary_search(prices_sorted, 300.75))  # Output: True
# How it works: Checks middle (300.75), finds target
print("Binary Search Index (300.75):", search.binary_search_index(prices_sorted, 300.75))  # Output: 2
# How it works: Returns index 2 where 300.75 is found



