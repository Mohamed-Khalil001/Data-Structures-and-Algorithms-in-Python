# big notation lecture code
# this code demonstrate different time complexities (e.g o(1) , o(n) , o(n^2) , 0(n^3))
# and how to calculate and simplify big o for algorithms
# examples are inspired quantiative analysis (e.g stock price analysis)

# o(1) - constant time
# accessing a specific stock price at a given index
# performs one operation regardless of input size
def gt_third_price(prices):
    return prices[2]  # o(1)

# o(n) - linear time
# printing all stock prices
# time (operations) Directly proportional with data


def print_all_prices(prices):
    for price in prices:  # o(n)
        print(price)


# o(n^2) - Quadratic time
# compare every stock price with every other price
# time (operations) Directly proportional quadratic  with data
def compare_all_prices(prices):
    for i in range(len(prices)):  # o(n)
        for j in range(len(prices)):  # o(n)
            print(f"compare {prices[i]} with {prices[j]}")  # o(n*n) = o(n^2)


# o(n^3) - cubic time
# analyzing more three parameter as prices , volumes , and time
# time(operations) Directly proportional cubic with data
def analyze_price_volume_time(prices, volumes, times):
    for price in prices:  # o(n)
        for volume in volumes:  # o(n)
            for time in times:  # o(n)
                # o(n*n*n) = o(n^3)
                print(f"price: {price} , volume {volume} , time {time}")


# calculating big o for a mixed algrithm
# analyze two  seperated lists price (tesla and apple )
# time complexity form : o(n+m) - Linear time for two separate loops over n and m items.
def analyze_two_lists(prices, other_prices):

    count = 0  # o(1) # one operation
    print("start alnalysis")  # o(1) # one operation
    for price in prices:  # o(n) - n perations
        count += 1
    for other_price in other_prices:  # o(m) - m operations
        count += 1
    return count  # o(1) - one operation

    # total : o(1+1+n+m+1) = o(5+n+m) ≈ o(n+m)
    # Simplifying Big O
    # Example: O(5 + n + n^2) simplifies to O(n^2) by removing constants and smaller terms(very small).


# Testing the functions
prices = [300.00, 305.50, 307.75, 310.00]
volumes = [1000, 1500, 1200]
times = ["08:00", "09:00", "10:00"]

print("O(1) Example:")
print(gt_third_price(prices))  # Output: 307.75
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")
print("\nO(n) Example:")
print_all_prices(prices)  # Output: 300.00, 305.50, 307.75, 310.00
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")

print("\nO(n^2) Example:")
compare_all_prices(prices)  # Output: Differences for all pairs
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")

print("\nO(n^3) Example:")
analyze_price_volume_time(prices, volumes, times)
print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n")

print("\nO(n + m) Example:")
other_prices = [200.00, 205.00]
# Output: 6 (4 from prices + 2 from other_prices)
print(analyze_two_lists(prices, other_prices))
