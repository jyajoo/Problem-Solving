"""
백준 - https://www.acmicpc.net/problem/3273

< 두 수의 합 >
"""

from sys import stdin

input = stdin.readline

# n개의 서로 다른 양의 정수
n = int(input())
arr = list(map(int, input().split()))

# 각 값은 1보다 크거나 같고, 1,000,000보다 작거나 같은 자연수
# x가 주어졌을 때, a1 + a2 = x를 만족하는 (a1, a2)쌍의 수를 구하자
x = int(input())

# 정렬하기
arr.sort()
start = 0
end = -1

count = 0
while True:
    a, b = arr[start], arr[end]
    if a >= b:
        break

    if a + b == x:
        count += 1
        start += 1
        end -= 1
    elif a + b > x:
        end -= 1
    elif a + b < x:
        start += 1

print(count)
