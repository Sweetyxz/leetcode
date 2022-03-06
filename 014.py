strs = ['ab', 'ac', 'abcd']
'''
min_str = min(strs)
min_len = len(min_str)
flag = False
common_str = ''
for i in range(0, min_len):
    common_char = min_str[i]
    for m in strs:
        if m[i] == common_char:
            flag = True
        else:
            flag = False
            break
    if flag:
        common_str += common_char
    else:
        break
print(common_str)
'''
print(list(zip(*strs)))
