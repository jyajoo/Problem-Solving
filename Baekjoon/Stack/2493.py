"""
백준 - https://www.acmicpc.net/problem/2493

< 탑 > 
"""

from sys import stdin

input = stdin.readline

n = int(input())
t = list(map(int, input().split()))

result = [0]
for i in range(1, n):
    if t[i] < t[i - 1]:
        result.append(i)

    else:
        ex = i - 1
        while ex >= 0:
            idx = result[ex] - 1
            l = t[idx]
            if t[i] < l:
                result.append(result[ex])
                break
            ex -= 1
        else:
            result.append(0)

print(*result)
