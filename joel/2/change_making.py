def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    coin_count = [0] * (amount + 1)
    coin_used = [0] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x] > dp[x - coin] + 1:
                dp[x] = dp[x - coin] + 1
                coin_count[x] = coin_count[x - coin] + 1
                coin_used[x] = coin

    if dp[amount] == float('inf'):
        return -1

    res = []
    i = amount
    while i > 0:
        res.append(coin_used[i])
        i -= coin_used[i]

    for coin in coins:
        print(f"Coin {coin}: {res.count(coin)}")

    return dp[amount]


# example usage:
coins = [1, 5, 10, 25]
amount = int(input("Enter amount: "))
print(min_coins(coins, amount))
