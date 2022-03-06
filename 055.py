nums = [3,2,1,0,4]

max_cover = 0
i = 0

if len(nums) == 1:
    return True

while i <= max_cover:
    max_cover = max(max_cover, i + nums[i])
    if max_cover >= len(nums) - 1:
        return True
    i += 1
return False
