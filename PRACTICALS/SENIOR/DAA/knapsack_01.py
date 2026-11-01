def knapsack_01(weights, values, capacity):
    n = len(values)

    # DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill DP
    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]

        for w in range(1, capacity + 1):
            if wt <= w:
                take = val + dp[i - 1][w - wt]
                skip = dp[i - 1][w]
                dp[i][w] = max(take, skip)
            else:
                dp[i][w] = dp[i - 1][w]

    # Find picked items
    w = capacity
    items_taken = []

    for i in range(n, 0, -1):
        # if value came from taking item
        if dp[i][w] != dp[i - 1][w]:
            items_taken.append((weights[i - 1], values[i - 1]))
            w -= weights[i - 1]

    items_taken.reverse()
    return dp[n][capacity], items_taken


# Example
values  = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value, items = knapsack_01(weights, values, capacity)

print("Max Value:", max_value)
print("Items picked:")
for item in items:
    print(item)

