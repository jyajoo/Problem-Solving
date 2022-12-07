'''
백준 - https://www.acmicpc.net/problem/11051

< 이항 계수 2 >
'''

# 메모리 초과
from itertools import combinations

n, k = map(int, input().split())
num = [0] * n
comb = list(combinations(num, k))
print(len(comb) % 10007)


'''
- 팩토리얼 사용으로 해결
'''
from math import factorial

n, k = map(int, input().split())

result = factorial(n) // (factorial(k) * factorial(n-k))
print(result % 10007)

