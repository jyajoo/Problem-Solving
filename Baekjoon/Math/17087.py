'''
백준 - https://www.acmicpc.net/problem/17087

< 숨바꼭질 6 >
'''
import sys

input = sys.stdin.readline

n, s = map(int, input().split())
positions = list(map(int, input().split()))

arr = []
for p in positions:
    d = abs(p - s)
    arr.append(d)
arr.sort(reverse=True)

gcd = arr[0]
for i in range(1, n):
    a, b = gcd, arr[i]
    while b != 0:
        n = a % b
        a = b
        b = n
    gcd = a
print(gcd)