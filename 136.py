s = "applepenapple"
wordDict = ["apple", "pen"]
left = 0
right = 1
def backtrack(left, right):
    while True:
        if right == len(s) + 1:
                return False
        print(s[left:right])
        if s[left:right] in wordDict:
            leng = right - left
            left = right
            right += 1
            if left == len(s):
                return True
            if backtrack(left, right):
                return True
            else:
                right = left + 1
                left -= leng
        else:
            right += 1

if backtrack(left, right):
    print("yese")
else:
    print("no")
