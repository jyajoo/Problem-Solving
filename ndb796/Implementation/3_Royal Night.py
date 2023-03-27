'''
< 왕실의 나이트 >

- 상하좌우 2칸 이동 (상하-좌우 1칸 이동, 좌우-상하 1칸 이동)
'''

n = input()
y = ord(n[0]) - 96   # int(ord(n[0])) - int(ord('a')) + 1
x = int(n[1])
chess = []

# 이동할 수 있는 8가지 방향
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, 2), (1, 2), (-1, -2), (1, -2)]
result = 0
for step in steps:
    nx = x + step[0]
    ny = y + step[1]
    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue
    result += 1
print(result)

'''
'''

chess = []
n = input()
y = ord(n[0]) - 96
x = int(n[1])

# 상하좌우
dx = [-2, +2, 0, 0]
dy = [0, 0, -2, +2]

dx_2 = [-1, +1, 0, 0]
dy_2 = [0, 0, -1, +1]

cnt = 0
for i in range(2):       # 상하 2칸 이동
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue
    x, y = nx, ny
    for j in range(2,4):  # 좌우 1칸
        nx = x + dx_2[j]
        ny = y + dy_2[j]
        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        cnt += 1

nx, ny = 0, 0
y = ord(n[0]) - 96
x = int(n[1])
for i in range(2,4):    # 좌우 2칸 이동
    nx = x + dx[i]
    ny = y + dy[i]
    if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
        continue
    x, y = nx, ny
    for j in range(2):  # 상하 1칸
        nx = x + dx_2[j]
        ny = y + dy_2[j]
        if nx <= 0 or nx > 8 or ny <= 0 or ny > 8:
            continue
        cnt += 1

print(cnt)

'''
2023.03.27
'''
n = input()
move = [(-1, -2), (1, -2), (-1, 2), (1, 2), (-2, -1), (2, -1), (-2, 1), (2, 1)]

x = int(n[1])
y = ord(n[0]) - 96
result = 0
for a,  b in move:
    if a + x < 1 or a + x > 8 or b + y < 1 or b + y > 8:
        continue
    result += 1
print(result)