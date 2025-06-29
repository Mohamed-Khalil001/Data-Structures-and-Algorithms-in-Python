# Selection Sort and Insertion Sort Lecture Code
# Implements Selection Sort and Insertion Sort for sorting financial data (e.g., stock prices).
# Time Complexity: Analyzed per function.
# Example: Sorting stock prices or transaction amounts in ascending order.

# --------------------------------------------
# Concept: Selection Sort
# Definition: A sorting algorithm that selects the smallest element from the unsorted portion and swaps it with the first unsorted element.
# Properties:
# - Iterates through the list, finding the minimum element in each pass.
# - Swaps the minimum with the first unsorted element.
# - Time Complexity: O(n²) worst/average/best.
# Use Case: Sorting small lists of stock prices or transaction amounts in quantitative finance.

# Concept: Insertion Sort
# Definition: A sorting algorithm that builds the sorted list one element at a time by inserting each element into its correct position.
# Properties:
# - Efficient for small or nearly sorted lists.
# - Shifts larger elements to make space for the current element.
# - Time Complexity: O(n²) worst/average, Ω(n) best (sorted list).
# Use Case: Sorting nearly sorted financial data (e.g., daily stock prices with small changes).
# --------------------------------------------

class FinancialSort:
    def selection_sort(self, lst):
        """
        Selection Sort: Sorts a list in ascending order by selecting the minimum element.
        Time Complexity: O(n²) worst/average/best.
        """
        n = len(lst)  # Length of the list
        for i in range(n - 1):  # Iterate until n-1
            min_idx = i  # Assume first unsorted is minimum
            for j in range(i + 1, n):  # Check rest of the list
                if lst[j] < lst[min_idx]:  # If smaller value found
                    min_idx = j  # Update minimum index
            lst[i], lst[min_idx] = lst[min_idx], lst[i]  # Swap
        return lst  # Return sorted list

    def insertion_sort(self, lst):
        """
        Insertion Sort: Sorts a list in ascending order by inserting each element into its correct position.
        Time Complexity: O(n²) worst/average, Ω(n) best (sorted list).
        """
        n = len(lst)  # Length of the list
        for i in range(1, n):  # Start from second element
            number_to_order = lst[i]  # Element to insert
            j = i - 1  # Index of last sorted element
            while j >= 0 and number_to_order < lst[j]:  # Shift larger elements
                lst[j + 1] = lst[j]
                j -= 1
            lst[j + 1] = number_to_order  # Insert in correct position
        return lst  # Return sorted list


# Testing
sorter = FinancialSort()

# Example: Sorting stock prices
stock_prices = [100, 50, 75, 25]
print("Selection Sort:", sorter.selection_sort(
    stock_prices.copy()))  # Output: [25, 50, 75, 100]
# How it works: Selects the smallest element and swaps it with the first unsorted element each iteration

# Example: Sorting nearly sorted stock prices
nearly_sorted = [25, 50, 75, 100, 80]
print("Insertion Sort:", sorter.insertion_sort(
    nearly_sorted.copy()))  # Output: [25, 50, 75, 80, 100]
# How it works: Inserts each element into its correct position, efficient for nearly sorted lists
