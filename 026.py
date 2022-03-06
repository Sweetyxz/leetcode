nums = [0,0,1,1,1,2,2,3,3,4]

left = 0
right = 1

while right < len(nums):
	if nums[left] == nums[right]:
		nums.remove(nums[right])
		print(len(nums))
	else:
		left += 1
		right += 1
print(len(nums))