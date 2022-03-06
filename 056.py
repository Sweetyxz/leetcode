intervals = [[1,4],[4,5]]

inter = sorted(intervals)
result = []
left, right = inter[0][0], inter[0][1]
i = 1
while i < len(inter):
    if inter[i][0] <= right and inter[i][1] >= right:
        right = inter[i][1]
        print(left, right)
    elif inter[i][0] > right:
        result.append([left, right])
        left = inter[i][0]
        right = inter[i][1]
        print(left, right)
    i += 1
result.append([left, right])
print(result)
