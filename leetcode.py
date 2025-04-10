# grid = [[1, 1], [2, 2], [3, 3]]
# n = len(grid)
# g = 0
#
# for i in range(n - 1):
#     for j in range(len(grid[i]) - 1):
#         if abs(grid[i][j] + grid[i][j]) == abs(grid[i][j] - grid[i][j+1]):
#             g += 1
#
# print(g)

ball = [[8,7],[9,9],[7,4],[9,7]]
s = []
c = []
for i in range(len(ball)):
    a = ball[i][0]
    s.append(a)
s.sort()
for i in range(len(s)-1):
    x = s[i+1] - s[i]
    c.append(x)
print(c)
