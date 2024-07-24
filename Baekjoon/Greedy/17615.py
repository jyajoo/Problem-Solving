"""
백준 - https://www.acmicpc.net/problem/17615

< 볼 모으기 >
"""

import sys

input = sys.stdin.readline

# 입력 처리
n = int(input().strip())
arr = list(input().strip())

r_count = arr.count("R")
b_count = arr.count("B")

balls_r = []
balls_b = []
cnt = 1
for i in range(1, n):
    if arr[i] != arr[i - 1]:
        if arr[i - 1] == "R":
            balls_r.append(cnt)
        else:
            balls_b.append(cnt)
        cnt = 1
    else:
        cnt += 1

if arr[-1] == "R":
    balls_r.append(cnt)
else:
    balls_b.append(cnt)


# 왼쪽으로 몰기
if arr[0] == "R":
    left_red = r_count - balls_r[0]
    left_blue = b_count
else:
    left_red = r_count
    left_blue = b_count - balls_b[0]

# 오른쪽으로 몰기
if arr[-1] == "R":
    right_red = r_count - balls_r[-1]
    right_blue = b_count

else:
    right_red = r_count
    right_blue = b_count - balls_b[-1]

if r_count == 0 or b_count == 0:
    print(0)
else:
    result = min(left_red, left_blue, right_red, right_blue)
    print(result)

"""
"""
import sys

input = sys.stdin.readline

n = int(input())
arr = list(input().strip())
r_balls = []
b_balls = []

ex_ball = arr[0]
cnt = 1
for i in range(1, n):
    if ex_ball == arr[i]:
        cnt += 1
    else:
        if arr[i] == "B":
            r_balls.append(cnt)
        else:
            b_balls.append(cnt)
        ex_ball = arr[i]
        cnt = 1

if arr[-1] == "B":
    b_balls.append(cnt)
else:
    r_balls.append(cnt)

result = int(1e9)
if len(r_balls) == 0 or len(b_balls) == 0:
    result = 0
else:
    # 오른쪽 끝 R
    if arr[-1] == "R":
        cnt_r = sum(r_balls[: len(r_balls) - 1])
        cnt_b = sum(b_balls)
        result = min(result, cnt_r, cnt_b)

    # 오른쪽 끝 B
    else:
        cnt_r = sum(r_balls)
        cnt_b = sum(b_balls[: len(b_balls) - 1])
        result = min(result, cnt_r, cnt_b)

    # 왼쪽 끝 R
    if arr[0] == "R":
        cnt_r = sum(r_balls[1:])
        cnt_b = sum(b_balls)
        result = min(result, cnt_r, cnt_b)
    else:
        cnt_r = sum(r_balls)
        cnt_b = sum(b_balls[1:])
        result = min(result, cnt_r, cnt_b)

print(result)
