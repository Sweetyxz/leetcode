nums = [1, 2, 3]
result = [[]]
path = []
start_index = 0


# def find_path(nums, path, start_index):
#     for j in range(start_index, len(nums)):
#         path.append(nums[j])
#         result.append(path.copy())
#         find_path(nums, path, j + 1)
#         path.pop()


# find_path(nums, path, start_index)

for i in nums:
    add = []
    for n in result:
        x = n[:]
        x.append(i)
        add.append(x)
    result.extend(add)
print(result)
