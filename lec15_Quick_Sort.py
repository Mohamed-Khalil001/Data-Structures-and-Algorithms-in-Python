# Quicksort Lecture Code (Improved to Avoid RecursionError)
# Implements Quicksort with Lomuto's partition and random pivot for sorting financial data (e.g., stock prices).
# Time Complexity: Analyzed per function.
# Example: Sorting large lists of stock prices or transaction amounts in ascending order.

# --------------------------------------------
# Concept: Quicksort
# Definition: A sorting algorithm that uses Divide and Conquer: selects a pivot, partitions the list around it, and recursively sorts the sublists.
# Properties:
# - Pivot: Randomly chosen to avoid worst-case scenarios (e.g., sorted lists).
# - Partition: Places smaller elements to the left of the pivot and larger to the right (Lomuto's scheme).
# - Recursive: Applies Quicksort to left and right sublists.
# - Time Complexity: O(n²) worst, Θ(n log n) average/best.
# - Space Complexity: O(log n) average for recursion stack, O(n) worst.
# Use Case: Sorting large datasets in quantitative finance, like stock prices or transaction amounts, efficiently (in-place sorting).
# --------------------------------------------

import random


class FinancialQuicksort:
    def quicksort(self, lst, first_index, last_index):
        """
        Quicksort: Sorts a list in ascending order using Divide and Conquer.
        Time Complexity: O(n²) worst, Θ(n log n) average/best.
        Space Complexity: O(log n) average, O(n) worst.
        """
        if first_index < last_index:
            # Choose random pivot to avoid worst-case scenarios
            pivot_index = random.randint(first_index, last_index)
            lst[first_index], lst[pivot_index] = lst[pivot_index], lst[first_index]

            partition_index = self.partition(lst, first_index, last_index)
            self.quicksort(lst, first_index, partition_index - 1)  # Sort left
            self.quicksort(lst, partition_index + 1, last_index)  # Sort right
        return lst

    def partition(self, lst, first_index, last_index):
        """
        Partition: Places pivot in its correct position using Lomuto's scheme.
        Smaller elements to the left, larger to the right.
        """
        pivot = lst[last_index]  # Choose last element as pivot (Lomuto's scheme)
        i = first_index - 1  # Index of smaller element
        for j in range(first_index, last_index):
            if lst[j] <= pivot:  # If current element is smaller than or equal to pivot
                i += 1  # Increment index of smaller element
                lst[i], lst[j] = lst[j], lst[i]  # Swap
        lst[i + 1], lst[last_index] = lst[last_index], lst[i + 1]  # Place pivot
        return i + 1  # Return pivot's index


# Testing
quicksort = FinancialQuicksort()

# Example: Sorting stock prices
stock_prices = [100, 50, 75, 25, 200, 10]
print("Quicksort:", quicksort.quicksort(
    stock_prices.copy(), 0, len(stock_prices) - 1))
# Output: [10, 25, 50, 75, 100, 200]

# Test with sorted list (previously causing RecursionError)
sorted_prices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Quicksort (sorted list):", quicksort.quicksort(
    sorted_prices.copy(), 0, len(sorted_prices) - 1))
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
