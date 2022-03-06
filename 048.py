matrix = [[1,2,3],[4,5,6],[7,8,9]]

n = len(matrix)

# for row in range(0, n//2):
#     for col in range(0, (n + 1)// 2):
#         temp = matrix[row][col]
#         matrix[row][col] = matrix[n - col - 1][row]
#         print(matrix[row][col])
#         matrix[n - col - 1][row] = matrix[n - row - 1][n - col - 1]
#         matrix[n - row - 1][n - col - 1] = matrix[col][n - row - 1]
#         matrix[col][n - row - 1] = temp

for i in range(0, n // 2):  # 翻转矩阵
    temp = matrix[i]
    matrix[i] = matrix[n - i - 1]
    matrix[n - i - 1] = temp

for i in range(1, n):  # 沿着对角线反转
    for j in range(0, i):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

print(matrix)
