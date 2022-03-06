strs = ["cab","tin","pew","duh","may","ill","buy","bar","max","doc"]
res_dic = {}
res = []
for i in strs:
    x_sorted = sorted(i)
    x_sorted = "".join(x_sorted)
    if x_sorted in res_dic.keys():
        res_dic[x_sorted].append(i)
    else:
        res_dic[x_sorted] = [i]

print(list(res_dic.values()))