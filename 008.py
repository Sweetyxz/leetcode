def myAtoi(self, s):
    """
    :type s: str
    :rtype: int
    """
    flag = 1
    res = 0
    s = s.lstrip()
    for l, i in enumerate(s):
        if l == 0 and i == '-':
            flag = -1
        elif l == 0 and i == '+':
            pass
        else:
            try:
                m = int(i)
            except ValueError:
                break
            else:
                res = res * 10 + m
    res = res * flag
    if -(2**31) < res and res < (2**31 - 1):
        return res
    elif res < 0:
        return -2147483648
    else:
        return 2147483647
