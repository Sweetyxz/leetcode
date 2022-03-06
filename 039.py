candidates = [2, 3, 6, 7]
target = 7
nums_sum = 0
path = []
result = []
startindex = 0


def check_sum(candidates, target, result, path, nums_sum, startindex):
    if nums_sum == target:
        result.append(path.copy()) # 传入副本
        print("res", result)
        return
    elif nums_sum > target:
        return
    else:
        for i in range(startindex, len(candidates)):
            path.append(candidates[i])
            print(result)
            nums_sum += candidates[i]
            check_sum(candidates, target, result, path, nums_sum, i)
            path.pop()
            nums_sum -= candidates[i]


candidates = sorted(candidates)
check_sum(candidates, target, result, path, nums_sum, startindex)
print(result)
