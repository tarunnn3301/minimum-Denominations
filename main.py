def minimumDenominations(amount):
    # List of available denominations
    denominations = [1, 5, 10, 20, 25, 50]
    
    # Dynamic programming array to store the minimum number of denominations
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # 2D matrix to store the number of coins for each denomination
    coins = [[0] * len(denominations) for _ in range(amount + 1)]

    # Dynamic programming loop
    for i in range(1, amount + 1):
        for j in range(len(denominations)):
            if denominations[j] <= i:
                if 1 + dp[i - denominations[j]] < dp[i]:
                    # Update the minimum number of denominations
                    dp[i] = 1 + dp[i - denominations[j]]
                    # Update the number of coins for each denomination
                    coins[i] = coins[i - denominations[j]][:]
                    coins[i][j] += 1

    return dp[amount], coins[amount]

# Test the function
amount = int(input("Enter the amount: "))
min_denominations, coin_count = minimumDenominations(amount)
print("Minimum number of denominations:", min_denominations)
print("Number of coins for each denomination:")
denominations = [1, 5, 10, 20, 25, 50]
for i in range(len(denominations)):
    print(f"{denominations[i]}: {coin_count[i]}")
