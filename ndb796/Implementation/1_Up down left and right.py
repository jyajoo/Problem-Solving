'''
< 상하좌우>

- 계획서에 따라 공간을 넘어가지 않도록 조건을 설정한 후, 이동시킨다.
'''
# N X N 정사각형 공간 만들기
# 계획서 입력 받기

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