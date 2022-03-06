# left = 0
# while left < len(nums):
#   if nums[left] == val:
#       nums.remove(nums[left])
#   else:
#       left += 1
# return len(nums)

nums = []
val = 2
left, right = 0, len(nums)
while left < right:
    if nums[left] == val:
        nums[left] = nums[right]
        right -= 1
    else:
        left += 1
print(left)
