# Fibonacci Series using Memoization

def fibonacci_memo(n, memo={}):
    if n <= 1:
        return n

    if n not in memo:
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]


# Fibonacci Series using Tabulation

def fibonacci_tab(n):
    if n == 0:
        return []

    dp = [0] * n

    dp[0] = 0
    if n > 1:
        dp[1] = 1

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp


# Input
n = int(input("Enter n: "))

# Memoization series
memo_series = []
for i in range(n):
    memo_series.append(fibonacci_memo(i))

# Tabulation series
tab_series = fibonacci_tab(n)

print("Fibonacci Series using Memoization:")
print(*memo_series)

print("Fibonacci Series using Tabulation:")
print(*tab_series)