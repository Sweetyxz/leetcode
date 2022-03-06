class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0
        if x < 0:
            flag = 1
            x = abs(x)
        x_str = [i for i in str(x)]
        x_reverse = x_str[::-1]
        y = int("".join(x_reverse))
        if flag == 1:
            y = 0-y
        if -(2**31) < y and y < (2**31 - 1):
            return y
        else:
            return 0
