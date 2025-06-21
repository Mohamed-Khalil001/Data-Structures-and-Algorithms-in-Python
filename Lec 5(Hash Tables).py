# Hash Tables Lecture 5
# This code demonstrates Python dictionaries as hash tables for managing stock data.
# Time complexity is analyzed using Big O Notation.
# The example is tailored for quantitative analysis (e.g., stock price lookups and analysis).

# Hash Tables are a data structure that stores data in a key-value format, meaning each key points to a specific value.
# Think of it like a dictionary: every word (key) has a definition (value).
# What makes Hash Tables special is their speed in searching and inserting data.
# This efficiency comes from the hash function, which converts a key into a specific location (index) in the table.
# instead of searching through all the data, the hash function tells you exactly where to look —
# making operations like lookups, inserts, and deletions extremely fast (often in constant time, O(1)).


class StockHashTable:
    def __init__(self):
        """
        Initializes an empty dictionary to store stock data.
        Time Complexity: O(1)
        """
        self.stocks = {}

    def insert(self, ticker, data):
        """
        Inserts a stock's data (e.g., price, sector) using ticker as key.
        Time Complexity: O(1) average
        """
        self.stocks[ticker] = data

    def lookup(self, ticker):
        """
        Looks up a stock's data by ticker.
        Time Complexity: O(1) average
        """
        return self.stocks.get(ticker)

    def modify(self, ticker, data):
        """
        Modifies a stock's data.
        Time Complexity: O(1) average
        """
        if ticker in self.stocks:
            self.stocks[ticker] = data

    def remove(self, ticker):
        """
        Removes a stock by ticker.
        Time Complexity: O(1) average
        """
        if ticker in self.stocks:
            del self.stocks[ticker]

    def get_all_tickers(self):
        """
        Returns all stock tickers.
        Time Complexity: O(1)
        """
        return list(self.stocks.keys())

    def get_all_data(self):
        """
        Returns all stock data.
        Time Complexity: O(1)
        """
        return list(self.stocks.items())

    def calculate_average_price(self):
        """
        Calculates the average price of all stocks.
        Time Complexity: O(n)
        """
        if not self.stocks:
            return 0
        total = sum(stock["price"] for stock in self.stocks.values())
        return total / len(self.stocks)


# Testing the Hash Table
stock_table = StockHashTable()

# Inserting stock data (O(1) each)
stock_table.insert("TSLA", {"price": 300.00, "sector": "Technology"})
stock_table.insert("AAPL", {"price": 150.00, "sector": "Technology"})
stock_table.insert("GOOG", {"price": 2800.00, "sector": "Technology"})

# Lookup stock data (O(1))
# Output: {'price': 300.00, 'sector': 'Technology'}
print("TSLA Data:", stock_table.lookup("TSLA"))
print("NVDA Data:", stock_table.lookup("NVDA"))  # Output: None

# Modify stock data (O(1))
stock_table.modify("TSLA", {"price": 305.50, "sector": "Technology"})
# Output: {'price': 305.50, 'sector': 'Technology'}
print("Modified TSLA Data:", stock_table.lookup("TSLA"))

# Remove stock (O(1))
stock_table.remove("AAPL")
# Output: ['TSLA', 'GOOG']
print("All Tickers:", stock_table.get_all_tickers())

# Get all data (O(1))
# Output: [('TSLA', {...}), ('GOOG', {...})]
print("All Data:", stock_table.get_all_data())

# Calculate average price (O(n))
# Output: Average of TSLA and GOOG prices
print(f"Average Price: ${stock_table.calculate_average_price():.2f}")
