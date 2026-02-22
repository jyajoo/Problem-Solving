'''
백준 - https://www.acmicpc.net/problem/13305

< 주유소 >
'''
'''
2 <= n <= 100,000
1 <= 거리 <= 1,000,000,000
1 <= 가격 <= 1,000,000,000

for문으로 현 가격보다 작은 주유소 탐색
'''
import sys

input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
cities = list(map(int, input().split()))

answer = 0
now = cities[0]

for i in range(1, n):
    if now >= cities[i]:
        answer += distance[i - 1] * now
        now = cities[i]
    else:
        answer += distance[i - 1] * now

print(answer)