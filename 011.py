'''
height = []
x_y = [(i, l) for l, i in enumerate(height)]
print(x_y)
h = sorted(x_y)
max_s = 0
print(h)
for m, n in h[:-1]:
    loc = h.index((m, n))
    max_len = 0
    for x, y in h[loc + 1:]:
        max_len = abs(y - n) if abs(y - n) > max_len else max_len
    s = m * max_len
    print(m, max_len, s)
    max_s = s if s > max_s else max_s
print(max_s)
'''
height = [4, 3, 2, 1, 4]
i, n = 0, len(height) - 1
max_area = 0
while i < n:
    if height[i] < height[n]:
        s = height[i] * (n - i)
        i = i + 1
    else:
        s = height[n] * (n - i)
        n = n - 1
    max_area = s if s > max_area else max_area
print(max_area)
