"""
백준 - https://www.acmicpc.net/problem/2470

< 두 용액 >
"""

from sys import stdin

input = stdin.readline

# 산성 용액은 양수, 알칼리성 용액은 음수
# 같은 양의 용액을 혼합하여 0에 가깝도록

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = []
start = 0
end = n - 1
diff = int(2e9)

while start < end:
    d = arr[end] + arr[start]

    if abs(d) < diff:
        diff = abs(d)
        result = [arr[start], arr[end]]

    if d < 0:
        start += 1
    elif d > 0:
        end -= 1
    else:
        break
result.sort()
print(*result)
