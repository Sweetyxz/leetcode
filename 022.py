n = 1
length = n * 2
tot_list = ["("]
i = 1
while i < length:
    left = tot_list.copy()
    right = tot_list.copy()
    for m in range(len(left)):
        left[m] = left[m] + "("
    for k in range(len(right)):
        right[k] = right[k] + ")"
    tot_list = left + right
    i = i + 1

final_list = tot_list.copy()
for i in final_list:
    if "()" in i:
        j = 0
        h = i
        while j < n:
            h = h.replace("()", '')
            j += 1
        if h != '':
            tot_list.remove(i)
    else:
        tot_list.remove(i)

print(tot_list)
