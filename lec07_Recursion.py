# Understanding Recursion Lecture Code
# Implements recursive functions for financial calculations.
# Time Complexity: Analyzed per function.
# Example: Portfolio and transaction analysis in quantitative finance.

# --------------------------------------------
# Concept: Recursion
# Definition: A function calls itself to solve a smaller instance of a problem until reaching a base case.
# Properties:
# - Base Case: Condition that stops recursion (e.g., n = 1 in factorial).
# - Recursive Case: Function calls itself with reduced input (e.g., factorial(n-1)).
# - Call Stack: Stores each function call until completion, using more memory.
# - Use Case: Simplifies complex problems like factorial, compound interest, or financial calculations.
# Time Complexity:
# - Linear recursion (e.g., factorial): O(n)
# - Exponential recursion (e.g., naive Fibonacci): O(2^n)
# Optimization: Dynamic Programming with memoization reduces complexity by caching results.
# --------------------------------------------
class RecursiveFinancialCalculator:
    def factorial(self, n):
        """
        Calculates factorial recursively (e.g., for combinatorial financial models).
        Time Complexity: O(n)
        """
        if n <= 1:  # Base Case: Stop if n is 1 or less
            return 1  # Return 1 because 1! = 1 and 0! = 1
        return n * self.factorial(n - 1)  # Recursive Case: n * factorial(n-1)

    def sum_transactions(self, transactions, index):
        """
        Sums transaction amounts recursively (e.g., for portfolio analysis).
        Time Complexity: O(n)
        """
        if index < 0:  # Base Case: Stop if index is negative
            return 0  # Return 0 to not affect sum
        # Recursive Case: Add current and rest
        return transactions[index] + self.sum_transactions(transactions, index - 1)

    def compound_interest(self, principal, rate, years):
        """
        Calculates compound interest recursively.
        Time Complexity: O(n)
        """
        if years == 0:  # Base Case: Stop if no years left
            return principal  # Return principal as is
        # Recursive Case: Apply interest
        return self.compound_interest(principal, rate, years - 1) * (1 + rate)

    def fibonacci_memoized(self, n, memo=None):
        """
        Calculates nth Fibonacci number with memoization (e.g., for growth modeling).
        Time Complexity: O(n) with memoization
        """
        if memo is None:  # Initialize memo dictionary if None
            memo = {}
        if n <= 1:  # Base Case: Return n for 0 or 1
            return n
        if n not in memo:  # Check if n is not in memo
            memo[n] = self.fibonacci_memoized(
                # Calculate and store
                n - 1, memo) + self.fibonacci_memoized(n - 2, memo)
        return memo[n]  # Return result from memo or calculation


# Testing
calculator = RecursiveFinancialCalculator()

# Factorial
print("Factorial(5):", calculator.factorial(5))  # Output: 120
# How it works: 5 * (4 * (3 * (2 * (1)))) = 120

# Sum Transactions
transactions = [100.00, 200.50, 300.75]
print("Total Transactions:", calculator.sum_transactions(
    transactions, len(transactions) - 1))  # Output: 601.25
# How it works: 300.75 + (200.50 + (100.00 + 0)) = 601.25

# Compound Interest
print("Compound Interest (1000, 5%, 3 years):",
      calculator.compound_interest(1000, 0.05, 3))  # Output: 1157.625
# How it works: 1000 * 1.05 * 1.05 * 1.05 = 1157.625

# Fibonacci with Memoization
print("Fibonacci(5):", calculator.fibonacci_memoized(5))  # Output: 5
# How it works: fib(5) = fib(4) + fib(3), memo saves results
