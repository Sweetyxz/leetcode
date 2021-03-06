grid = [[1,3,1],[1,5,1],[4,2,1]]
m = len(grid)
n = len(grid[0])
dp = [[0] * n for _ in range(m)]

for i in range(0, m):
    for j in range(0, n):
        if i == 0 and j == 0:
            dp[i][j] = grid[i][j]
        elif i == 0:
            dp[i][j] = dp[i][j-1] + grid[i][j]
        elif j == 0:
            dp[i][j] = dp[i-1][j] + grid[i][j]
        else:
            dp[i][j] = min(dp[i][j-1] + grid[i][j], dp[i-1][j] + grid[i][j])
print(dp)
print(dp[m-1][n-1])
