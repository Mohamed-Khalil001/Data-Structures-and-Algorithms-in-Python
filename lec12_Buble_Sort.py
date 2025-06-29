# Bubble Sort Lecture Code
# Implements Bubble Sort (basic and optimized) for sorting financial data (e.g., stock prices).
# Time Complexity: Analyzed per function.
# Example: Sorting stock prices or transaction amounts in ascending order.

# --------------------------------------------
# Concept: Bubble Sort
# Definition: A sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order, "bubbling" larger elements to the end.
# Properties:
# - Basic Version:
#   - Compares and swaps adjacent elements in nested loops.
#   - Time Complexity: O(n²) for worst/average case, Ω(n²) for best case.
# - Optimized Version:
#   - Uses a flag to detect if the list is sorted, stopping early if no swaps are needed.
#   - Time Complexity: O(n²) for worst/average case, Ω(n) for best case (sorted list).
# Use Case: Sorting small or nearly sorted lists of stock prices or transaction amounts in quantitative finance.
# --------------------------------------------

class FinancialBubbleSort:
    def bubble_sort(self, lst):
        """
        Basic Bubble Sort: Sorts a list in ascending order.
        Time Complexity: O(n²) worst/average, Ω(n²) best.
        """
        n = len(lst)  # Length of the list
        for i in range(n):  # Iterate n times
            for j in range(n - i - 1):  # Skip sorted elements at the end
                if lst[j] > lst[j + 1]:  # If first element is larger
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
        return lst  # Return sorted list

    def bubble_sort_optimized(self, lst):
        """
        Optimized Bubble Sort: Stops early if no swaps are needed.
        Time Complexity: O(n²) worst/average, Ω(n) best (sorted list).
        """
        n = len(lst)  # Length of the list
        while True:  # Keep iterating until sorted
            is_sorted = True  # Assume list is sorted
            for j in range(n - 1):  # Compare adjacent elements
                if lst[j] > lst[j + 1]:  # If first element is larger
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]  # Swap
                    is_sorted = False  # List is not sorted yet
                    print(lst, j, n)
            if is_sorted:  # If no swaps, list is sorted
                break
            n -= 1  # Skip sorted elements at the end
        return lst  # Return sorted list


# Testing
bubble_sort = FinancialBubbleSort()

# Example: Sorting stock prices
stock_prices = [100, 50, 75, 25]
print("Basic Bubble Sort:", bubble_sort.bubble_sort(
    stock_prices.copy()))  # Output: [25, 50, 75, 100]
# How it works: Compares and swaps adjacent elements, bubbling largest to the end each iteration

# Example: Sorting nearly sorted stock prices
nearly_sorted = [5, 4, 3, 1, 2]
print("Optimized Bubble Sort:", bubble_sort.bubble_sort_optimized(
    nearly_sorted.copy()))  # Output: [25, 50, 75, 80, 100]
# How it works: Stops early if no swaps are needed, efficient for nearly sorted lists
