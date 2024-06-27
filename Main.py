# The greedy_change_making function takes a list of coin denominations and a target amount
# It returns the minimum number of coins needed to make the target amount using a greedy algorithm
def greedy_change_making(coins, target):
    # Sort the coins in descending order
    coins.sort(reverse=True)
    # Initialize the result list
    result = []
    # Iterate over each coin
    for coin in coins:
        # While the target is greater than or equal to the coin value
        while target >= coin:
            # Subtract the coin value from the target
            target -= coin
            # Add the coin to the result list
            result.append(coin)
    # Return the number of coins and the list of coins if the target is 0, else return "No solution"
    return len(result), result if target == 0 else "No solution"


# Test the greedy_change_making function with different sets of coins and targets

# Test function 1
coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = 163
print("Greedy Change Making")
print("Test 1: ")
print(greedy_change_making(coins, target))

# Test function 2
coins = [10, 7, 1]
target = 15
print("Test 2: ")
print(greedy_change_making(coins, target))

# Test function 3
coins = [3, 2]
target = 4
print("Test 3: ")
print(greedy_change_making(coins, target))



# The dp_change_making function takes a list of coin denominations and a target amount
# It returns the minimum number of coins needed to make the target amount using dynamic programming
def dp_change_making(coins, target):
    # Initialize the dp list with infinity for all values except for the 0th index
    dp = [float('inf')] * (target + 1)
    dp[0] = 0
    # Iterate over each coin
    for coin in coins:
        # For each value from the coin value to the target
        for i in range(coin, target + 1):
            # Update the dp value for the index with the minimum of the current dp value and the dp value of the
            # index minus the coin value plus 1
            dp[i] = min(dp[i], dp[i - coin] + 1)
            # If the dp value for the target is not infinity
    if dp[target] != float('inf'):
        # Initialize the result list
        result = []
        # While the target is not 0
        while target:
            # Iterate over each coin
            for coin in coins:
                # If the target is greater than or equal to the coin value and the dp value for the target is equal
                # to the dp value for the target minus the coin value plus 1
                if target >= coin and dp[target] == dp[target - coin] + 1:
                    # Add the coin to the result list
                    result.append(coin)
                    # Subtract the coin value from the target
                    target -= coin
                    break
        # Return the number of coins and the list of coins
        return len(result), result
    else:
        # If the dp value for the target is infinity, return "No solution"
        return "No solution"


# Test the dp_change_making function with different sets of coins and targets
print("")
print("")
print("Dynamic Change Making")
# Test function 1
coins = [200, 100, 50, 20, 10, 5, 2, 1]
target = 163
print("Test 1: ")
print(dp_change_making(coins, target))
# Test function 2
coins = [10, 7, 1]
target = 15
print("Test 2: ")
print(dp_change_making(coins, target))
# Test function 3
coins = [3, 2]
target = 4
print("Test 3: ")
print(dp_change_making(coins, target))
