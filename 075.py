nums = [2,0,2,1,1,0]
# red = 0
# white = 0
# blue = 0

# for i in nums:
#     if i == 0:
#         red += 1
#     elif i == 1:
#         white += 1
#     elif i == 2:
#         blue += 1

# for i in range(0, len(nums)):
#     if i < red:
#         nums[i] = 0
#     elif i >= red and i < red + white:
#         nums[i] = 1
#     else:
#         nums[i] = 2

left = 0
right = len(nums) - 1
i = 0
while i <= right:
    if nums[i] == 0:
        temp = nums[left]
        nums[left] = nums[i]
        nums[i] = temp
        left += 1
        i += 1
    elif nums[i] == 2:
        temp = nums[right]
        nums[right] = nums[i]
        nums[i] = temp
        right -= 1
    else:
        i += 1
print(nums)
