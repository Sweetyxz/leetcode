s = 'MCMXCIV'
dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}
res = 0
x = 0
while x < len(s):
    m = s[x: x+2]
    if m in dic:
        print(m)
        res += dic.get(m)
        x = x + 2
    else:
        res += dic.get(s[x])
        x = x + 1
print(res)
