# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
head = None
i = 1
num = 1
while i > 0:
    head = ListNode(i, head)
    i = i - 1

top = head
for j in range(0, 31):
    if top.next:
        top = top.next
        num += 1
    else:
        break
print(num)
n = 1

top = head
if n == 1:
    head = head.next
else:
    left, right = head, ListNode()
    for i in range(2, n + 1):
        top = top.next
        if i == n - 1:
            left = top
            print(top.val)
        if i == n:
            right = top
            print(right.val)
    left.next = right.next

print('jieguo')
print(head.val)
print(head.next)
