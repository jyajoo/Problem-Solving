"""
백준 - https://www.acmicpc.net/problem/2138

< 전구와 스위치 >
"""
import sys

input = sys.stdin.readline

n = int(input())

start = list(map(int, input().strip()))
end = list(map(int, input().strip()))

answer = int(1e9)
light = start[:]
# 0번 전구를 누르고 시작
for i in [0, 1]:
    if light[i] == 0:
        light[i] = 1
    else:
        light[i] = 0

switch = 1
count = 1
while True:
    if switch == n:
        if light == end:
            answer = min(answer, count)
        break
    if light[switch - 1] == end[switch - 1]:
        switch += 1
    else:
        # 이전 스위치가 같지 않다면, 현재 스위치를 누르기
        for i in [-1, 0, 1]:
            if 0 <= switch + i < n:
                if light[switch + i] == 0:
                    light[switch + i] = 1
                else:
                    light[switch + i] = 0
        count += 1
        switch += 1


# 0번 전구를 누르지 않고 시작
light = start
switch = 1
count = 0
while True:
    if switch == n:
        if light == end:
            answer = min(answer, count)
        break
    if light[switch - 1] == end[switch - 1]:
        switch += 1
    else:
        # 이전 스위치가 같지 않다면, 현재 스위치를 누르기
        for i in [-1, 0, 1]:
            if 0 <= switch + i < n:
                if light[switch + i] == 0:
                    light[switch + i] = 1
                else:
                    light[switch + i] = 0
        count += 1
        switch += 1

if answer == int(1e9):
    answer = -1

print(answer)
