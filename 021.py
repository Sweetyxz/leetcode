left = l1
right = l2

if left is None:
	print(l2)
if right is None:
	print(f"leftl1")

while left:
	if left.val > right.val:
		if right.next:
			if left.val < right.next.val
				temp = left
				right.next = temp
				temp.next = right.next
				right = right.next.
				left = left.next
			else:
				right = right.next
		else:
			node = left
			right.next = node
			left = left.next
			right = right.next
	elif left.val < right.val:
		temp = left
		temp.next = right
		left = left.next
	else:
		left = left.next

