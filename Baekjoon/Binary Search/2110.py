"""
백준 - https://www.acmicpc.net/problem/2110

< 공유기 설치 >
"""
import sys
input = sys.stdin.readline

# 집 개수, 공유기 개수
n, c = map(int, input().split())
homes = [int(input()) for _ in range(n)]
homes.sort(key = lambda x : x)

start = 1
end = homes[-1] - homes[0]
result = 0
while start <= end:
    # 가장 인접한 두 공유기 사이의 거리
    middle = (start + end) // 2

    # 첫번째 집에 공유기 설치
    val = homes[0]
    count = 1
    
    # 이전에 공유기가 설치된 집과 middle 이상만큼 떨어져있다면,
    # 공유기 설치가 가능하다.
    for i in range(1, n):
       if homes[i] >= val + middle:
            count += 1
            val = homes[i]

    # 설치한 공유기가 c보다 많다면, start를 늘려서 거리를 증가한다.
    if count >= c:
        start = middle + 1
        result = middle
    # 설치한 공유기가 c보다 적다면, end를 줄여서 거리를 줄인다.
    else:
        end = middle - 1

print(result)