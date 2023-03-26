'''
< 상하좌우 > - refine

- 계획서에 따라 공간을 넘어가지 않도록 조건을 설정한 후, 이동시킨다.
'''

n = int(input())
plan = list(input().split())

x = y = 1
for i in plan:
    if i == "R":
        if y < n:
            y += 1
    elif i == "U":
        if x > 1:
            x -= 1
    elif i == "D":
        if x < n:
            x += 1
    elif i == "L":
        if y < 1:
            y -= 1
print(x, y)

'''
'''
n = int(input())
x = y = 1
plans = list(input().split())

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

type = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(4):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or nx > n or ny < 1 or ny > n:
        continue
    x, y = nx, ny
print(x, y)

'''
2023.03.26
'''
n = int(input())
arr = list(input().split())
x_arr = [0, 0, -1, 1]
y_arr = [-1, 1, 0, 0]
X = 1
Y = 1
for i in arr:
    if i == 'L':
        x = x_arr[0]
        y = y_arr[0]
    elif i == 'R':
        x = x_arr[1]
        y = y_arr[1]
    elif i == 'U':
        x = x_arr[2]
        y = y_arr[2]
    else:
        x = x_arr[3]
        y = y_arr[3]
    
    if X + x < 1 or X + x > n or Y + y < 1 or Y + y > n:
        continue
    else:
        X += x
        Y += y

print(X, Y) 

'''
'''
n = int(input())
arr = list(input().split())

X, Y = 1, 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
types = ['L', 'R', 'U', 'D']

for i in arr:
    for t in range(len(types)):
        if types[t] == i:
            if X + dx[t] < 1 or X + dx[t] > n or Y + dy[t] < 1 or Y + dy[t] > n:
                break
            X += dx[t]
            Y += dy[t]
print(X, Y)