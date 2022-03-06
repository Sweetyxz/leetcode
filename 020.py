s = '(){}]'
dic = {
    "(": ")",
    "[": "]",
    "{": "}"
}
stri = ''
flag = True
for i in s:
    if i in dic.keys():
        stri += i
    else:
        if stri != "" and i == dic[stri[-1]]:
            stri = stri.replace(stri[-1], '')
        else:
            flag = False
            break
if stri == '' and flag:
    print('yes')
else:
    print('no')