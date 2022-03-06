digits = ''

d_map = ['','','abc', 'def','ghi','jkl','mno','pqrs','tuv','wxyz']

if digits:
    i = 1
    x = d_map[int(digits[0])]
    if len(digits) == 1:
        x = [l for l in x]
    else:
        while i < len(digits):
            y = d_map[int(digits[i])]
            x = [m + n for m in x for n in y]
            i = i + 1
    print(x)
else:
    print([])
