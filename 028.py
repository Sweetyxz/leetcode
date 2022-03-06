needle = 'aaa'
haystack = ''

if not needle:
    print(0)

needle_len = len(needle)
haystack_len = len(haystack)

if haystack_len < needle_len:
    print(-1)
i = 0
while i + needle_len < haystack_len:
    if haystack[i: i + needle_len] == needle:
        print(i)
        break
    else:
        i += 1
print(-1)
