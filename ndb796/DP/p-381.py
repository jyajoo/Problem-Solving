"""
< 못생긴 수 >
"""

n = int(input())

dp = [0] * n  # 못생긴 수를 담는 테이블
dp[0] = 1

# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음에 곱셈값을 초기화
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp[i] = min(next2, next3, next5)

    if dp[i] == next2:
        i2 += 1
        next2 = dp[i2] * 2

    if dp[i] == next3:
        i3 += 1
        next3 = dp[i3] * 3

    if dp[i] == next5:
        i5 += 1
        next5 = dp[i5] * 5

print(dp[n - 1])

"""
"""
import sys

input = sys.stdin.readline

n = int(input())

num2, num3, num5 = 1, 1, 1
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    min_num = min(next2, next3, next5)

    if min_num == next2:
        num2 += 1
        next2 = 2 * num2

    if min_num == next3:
        num3 += 1
        next3 = 3 * num3

    if min_num == next5:
        num5 += 1
        next5 = 5 * num5

print(min_num)
