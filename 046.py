nums = [1]

res, path = [], []
nums_copy = nums.copy()
def do(res, path, nums_copy):
    if nums_copy == []:
        res.append(path.copy())
        return
    for i in range(0, len(nums_copy)):
        path.append(nums_copy[i])
        nums_last = nums_copy[:]
        nums_copy = nums_copy[0:i] + nums_copy[i+1:len(nums_copy)]
        do(res, path, nums_copy)
        path.pop()
        nums_copy = nums_last[:]

do(res, path, nums_copy)
print(res)
