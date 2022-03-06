prices = [7,1,5,3,6,4]
dp = [[0-prices[0], 0] for _ in range(len(prices))]

for i in range(1, len(prices)):
	old_have = dp[i-1][0]
	new_have = 0 - prices[i]
	dp[i][0] = max(old_have, new_have)

	old_no = dp[i-1][1]
	new_no = dp[i-1][0] + prices[i]
	dp[i][1] = max(old_no, new_no)

print(dp[len(prices)-1][1])
