nums = [8, 8, 8, 8, 8]
target = 8

start, end = -1, -1


def find_binary(nums, target, boo):  # 循环判断左右边界的方法
    left, right = 0, len(nums) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            ans = mid
            if boo:
                right = mid - 1
            else:
                left = mid + 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return ans


start = find_binary(nums, target, True)
end = find_binary(nums, target, False)

'''
left, right = start - 1, end + 1

while start != -1 and left > 0:
    if nums[left] == target:
        start = left
        left -= 1
    else:
        break

while end != -1 and right < len(nums):
    if nums[right] == target:
        end = right
        right += 1
    else:
        break
'''
print(start, end)
