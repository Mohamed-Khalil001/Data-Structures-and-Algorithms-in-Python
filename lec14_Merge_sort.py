# Merge Sort Lecture Code
# Implements Merge Sort for sorting financial data (e.g., stock prices).
# Time Complexity: Analyzed per function.
# Example: Sorting large lists of stock prices or transaction amounts in ascending order.

# --------------------------------------------
# Concept: Merge Sort
# Definition: A sorting algorithm that uses Divide and Conquer: divides the list into halves, recursively sorts them, and merges the sorted halves.
# Properties:
# - Divide: Splits the list into two halves recursively until each sublist has one element.
# - Conquer: Recursively sorts each half.
# - Combine: Merges sorted halves into a single sorted list.
# - Time Complexity: O(n log n) worst/average/best.
# - Space Complexity: O(n) due to temporary arrays for merging.
# Use Case: Sorting large datasets in quantitative finance, like stock prices or transaction amounts, efficiently.
# --------------------------------------------

class FinancialMergeSort:
    def merge_sort(self, lst):
        """
        Merge Sort: Sorts a list in ascending order using Divide and Conquer.
        Time Complexity: O(n log n) worst/average/best.
        Space Complexity: O(n).
        """
        if len(lst) <= 1:  # Base case: list is sorted
            return lst
        mid = len(lst) // 2  # Divide into two halves
        left_half = self.merge_sort(lst[:mid])  # Recursive call on left
        right_half = self.merge_sort(lst[mid:])  # Recursive call on right
        return self.merge(left_half, right_half)  # Merge sorted halves

    def merge(self, left, right):
        """
        Merge: Combines two sorted lists into a single sorted list.
        """
        result = []  # Final sorted list
        i = j = 0  # Indices for left and right halves
        while i < len(left) and j < len(right):  # Compare elements
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])  # Add remaining left elements
        result.extend(right[j:])  # Add remaining right elements
        return result


# Testing
merge_sort = FinancialMergeSort()

# Example: Sorting stock prices
stock_prices = [100, 50, 75, 25, 200, 10]
# Output: [10, 25, 50, 75, 100, 200]
print("Merge Sort:", merge_sort.merge_sort(stock_prices.copy()))
# How it works: Divides list into halves, sorts recursively, and merges sorted halves
