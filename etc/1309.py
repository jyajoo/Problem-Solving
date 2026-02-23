'''
백준 - https://www.acmicpc.net/problem/1309

< 동물원 >
'''
import sys

input = sys.stdin.readline

n = int(input())

if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    a = 3
    b = 2
    for i in range(3, n + 1):
        c = a + b * 2
        b = a + b
        a = c
    
    print((a + b * 2) % 9901)

'''
'''
import sys

input = sys.stdin.readline
n = int(input())
dp = [1, 1]
for i in range(2, n + 1):
    a = dp[0] + dp[1] * 2
    b = dp[0] + dp[1]
    dp = [a, b]

print((dp[0] + dp[1] * 2) % 9901)
