nums = [-2,1]

result, count = (-1)*(10 ** 5), 0
dp = []
# for i in range(0, len(nums)):
#     count += nums[i]
#     if result < count:
#         result = count
#     if count < 0:
#         count = 0
#         continue

dp.append(nums[0])
for i in range(1, len(nums)):
    dp.append(max(dp[i - 1] + nums[i], nums[i]))
print(max(dp))
