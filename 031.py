nums = [1, 2]

nums_len = len(nums)
if nums_len == 1:
    print(nums)
dummy = -1
left, right = nums_len - 2, nums_len - 1
while left >= 0:
    if nums[right] < nums[left]:
        left -= 1
    else:
        dummy = left
        temp = nums[right]
        nums[right] = nums[left]
        nums[left] = temp
        break
nums[dummy + 1:] = sorted(nums[dummy + 1:])
print(nums)
