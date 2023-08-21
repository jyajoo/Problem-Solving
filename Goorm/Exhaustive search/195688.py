"""
구름톤 챌린지 - https://level.goorm.io/exam/195688/%EB%AC%B8%EC%9E%90%EC%97%B4-%EB%82%98%EB%88%84%EA%B8%B0/quiz/1

< 문자열 나누기 >
"""
import sys
from itertools import product

input = sys.stdin.readline

n = int(input())  # 문자열 길이
arr = input()  # 문자열 S

# (1, 1, n - 2)로 가장 큰 수는 n - 2이므로 1부터 n - 1까지로 설정
num = [i for i in range(1, n - 1)]

# 중복 순열
prod = list(product(num, repeat=3))

# 중복 순열 중 합이 n인 것만 추출
str_list = []
for x in prod:
    if sum(x) == n:
        i, j, k = x[0], x[1], x[2]
        a = arr[:i]
        b = arr[i : i + j]
        c = arr[i + j :].strip()
        str_list.append((a, b, c))

# p에 중복 제거하고 담기
p = set()
for a, b, c in str_list:
    p.add(a)
    p.add(b)
    p.add(c)
p = list(p)
p.sort()

# p에서 인덱스 + 1 값으로 result 구하기
result = 0
for a, b, c in str_list:
    a = p.index(a)
    b = p.index(b)
    c = p.index(c)
    result = max(result, a + b + c + 3)

print(result)
