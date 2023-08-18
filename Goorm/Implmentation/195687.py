"""
구름톤 챌린지 - https://level.goorm.io/exam/195687/%EC%9D%B4%EC%A7%84%EC%88%98-%EC%A0%95%EB%A0%AC/quiz/1

< 이진수 정렬 >
"""
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

one = []

for i in arr:
    one.append((i, bin(i).count("1")))

one.sort(key=lambda x: (-x[1], -x[0]))

print(one[K - 1][0])
