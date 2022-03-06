nums = [0,3,7,2,5,8,4,6,0,1]

if nums:
    nums = sorted(nums)
    dp = [0 for _ in range(len(nums))]
    dp[0] = 1
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1] + 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
    print(dp)
    print(max(dp))
else:
    print(0)
