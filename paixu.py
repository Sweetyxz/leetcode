nums = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]


# 选择排序
# for i in range(len(nums)):
#     index = i
#     for j in range(i+1, len(nums)):
#         if nums[j] < nums[index]:
#             index = j
#     temp = nums[i]
#     nums[i] = nums[index]
#     nums[index] = temp
# print(nums)

# 插入排序

# for i in range(1, len(nums)):
#     x = nums[i]
#     index = i
#     while index > 0 and nums[index-1] > x:
#         index -= 1
#     j = i
#     for m in range(j, index, -1):
#         temp = nums[m - 1]
#         nums[m - 1] = nums[m]
#         nums[m] = temp
# print(nums)

# 冒泡排序
# j = len(nums)
# while j > 0:
#     for i in range(j - 1):
#         if nums[i] > nums[i + 1]:
#             temp = nums[i + 1]
#             nums[i + 1] = nums[i]
#             nums[i] = temp
#     j -= 1
# print(nums)

# 冒泡排序优化
# j = len(nums)
# while j > 0:
#     flag = True  # 未发生交换 说明有序 可以直接退出
#     for i in range(j - 1):
#         if nums[i] > nums[i + 1]:
#             flag = False
#             temp = nums[i + 1]
#             nums[i + 1] = nums[i]
#             nums[i] = temp
#     if flag:
#         break
#     j -= 1
# print(nums)

# 希尔排序

size = len(nums)
gap = size//2

