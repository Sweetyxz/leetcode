nums = [-2, 3, -2]
max_result = nums[0]
imax = nums[0]
imin = nums[0]

for i in range(1, len(nums)):
    if nums[i] < 0:
    	temp = imax
    	imax = imin
    	imin = temp
    imax = max(nums[i] * imax, imax)
    imin = min(nums[i] * imin, imin)
    max_result = max(imax, max_result)
print(max_result)
# 错的