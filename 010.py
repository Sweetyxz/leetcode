s = 'aa'
p = '.'

up = len(s) - 1
down  = len(p) = 1
flag = False

if p == "" and s == "":
	flag == True
if p == "" and s != "":
	flag == False
if s == "" and p != "":
	pass

while True:
	if p[down] == s[up] or p[down] == '.':
		flag = True
		up -= 1
		down -= 1
	elif p[down] == '*':
		if p[left] == p[down - 1]:
			left -= 1
			flag = True
		else:
			down -= 2
