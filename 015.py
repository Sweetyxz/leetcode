nums = []
zheng, fu = [], []
res = []
sort_nums = sorted(nums)

for i in nums:
    if i < 0:
        fu.append(i)
    else:
        zheng.append(i)

print(fu, zheng)
left, right = 0, len(fu) - 1
if fu:
    while True:
        if left == len(fu) - 1:
            break
        if abs(fu[left] + fu[right]) in zheng:
            res.append([fu[left], fu[right], abs(fu[left] + fu[right])])
            right -= 1
        else:
            right -= 1
        if right == left:
            left += 1
            right = len(fu) - 1

left, right = 0, len(zheng) - 1

if zheng:
    while True:
        if left == len(zheng) - 1:
            break
        if 0 - (zheng[left] + zheng[right]) in fu:
            res.append([zheng[left], zheng[right], abs(zheng[left] + zheng[right])])
            right -= 1
        else:
            right -= 1
        if right == left:
            left += 1
            right = len(zheng) - 1
print(res)
