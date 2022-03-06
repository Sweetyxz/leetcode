board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
m = len(board)
n = len(board[0])
mark = [[0] * n for _ in range(m)]

print(mark)
# direct = [(0, -1), (0, 1), (-1, 0), (1, 0)]

# def backtrack(i, j, mark, nextindex):
# 	if nextindex == len(word):
# 		return True
# 	for m in direct:
# 		cur_i = i + m[0]
# 		cur_j = j + m[1]
		
# 		if cur_i >= 0 and cur_i <= m and cur_j >= 0 and cur_j <= n and board[cur_i][cur_j] == word[nextindex]:
# 			if mark[cur_i][cur_j] == 1:
# 				continue
# 			mark[cur_i][cur_j] = 1
# 			nextindex += 1
# 			if backtrack(cur_i, cur_j, mark, nextindex) == True:
# 				return True
# 		else:
# 			mark[i][j] = 0
# 			nextindex -= 1
# 	return False


# for i in range(m):
# 	for j in range(n):
# 		if board[i][j] == word[0]:
# 			mark[i][j] = 1
# 			if backtrack(i, j, mark, 1) == True:
# 				return True
# 			else:
# 				mark[i][j] = 0
# return False
