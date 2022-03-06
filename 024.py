class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = None
i = 4
num = 1
while i > 0:
    head = ListNode(i, head)
    i = i - 1
top = head

now = ListNode(-1, None)
dummy = ListNode(-1, now)

while True:
    if top:
        if top.next:
            now.next = ListNode(top.next.val, None)
            now = now.next
            now.next = ListNode(top.val, None)
            now = now.next
            top = top.next.next
        else:
            now.next = ListNode(top.val, None)
            top = top.next
    else:
        break
print(dummy.next.next.next.next.next.next)
