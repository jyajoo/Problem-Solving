"""
백준 - https://www.acmicpc.net/problem/2961

< 도영이가 만든 맛있는 음식 >
"""

import sys
from itertools import combinations

input = sys.stdin.readline

# 신맛 : 재료의 곱
# 쓴맛 : 재료의 합
# 둘의 차이가 최소가 되도록

n = int(input())
answer = int(1e9)
arr = []
for _ in range(n):
    s, b = map(int, input().split())
    arr.append((s, b))

for i in range(1, n + 1):
    for comb in combinations(arr, i):
        total_s, total_b = 1, 0
        for s, b in comb:
            total_s *= s
            total_b += b
        answer = min(answer, abs(total_s - total_b))

print(answer)
"""
비트마스킹

& : AND
| : OR
^ : XOR
~ : NOT
<< : 왼쪽 시프트
>> : 오른쪽 시프트

원소 추가 : A |= (1 << k)
원소 삭제 : A &= ~(1 << k)
원소 토글 : A ^= (1 << K)
포함 여부 확인 : A & (1 << k)

해당 재료를 쓸지 말지 0과 1로 표현
"""
import sys

input = sys.stdin.readline

n = int(input())
answer = int(1e9)
arr = []
for _ in range(n):
    s, b = map(int, input().split())
    arr.append((s, b))

"""
예를 들어 1 << 4의 경우는 0001(1) -> 10000(16)이 된다.
0000 ~ 1111까지만 포함되도록 for문 설정
"""
for i in range(1, 1 << n):
    s, b = 1, 0
    for j in range(n):
        if i & (1 << j):  # j번째 비트가 1이면 포함되어있음을 의미함
            s *= arr[j][0]
            b += arr[j][1]
    answer = min(answer, abs(s - b))

print(answer)
