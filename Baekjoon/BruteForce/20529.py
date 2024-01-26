"""
백준 - https://www.acmicpc.net/problem/20529

< 가장 가까운 세 사람의 심리적 거리 >
"""
import sys

input = sys.stdin.readline
from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    students = []
    mbti_count = {}
    for mbti in input().split():
        if mbti in mbti_count:
            if mbti_count[mbti] < 3:
                mbti_count[mbti] += 1
                students.append(mbti)
        else:
            mbti_count[mbti] = 1
            students.append(mbti)

    answer = int(1e9)
    for a, b, c in list(combinations(students, 3)):
        result = 0
        for i in range(4):
            if a[i] != b[i]:
                result += 1

            if a[i] != c[i]:
                result += 1

            if b[i] != c[i]:
                result += 1

        answer = min(answer, result)

    print(answer)
"""
"""
import sys

input = sys.stdin.readline
from itertools import combinations

t = int(input())
for _ in range(t):
    n = int(input())
    students = list(input().split())

    # 32개 이상의 값이 입력된다면, 3개의 mbti가 존재한다는 것을 의미한다.
    if n > 32:
        answer = 0
    else:
        answer = int(1e9)
        for a, b, c in combinations(students, 3):
            result = 0
            for i in range(4):
                if a[i] != b[i]:
                    result += 1

                if a[i] != c[i]:
                    result += 1

                if b[i] != c[i]:
                    result += 1

            answer = min(answer, result)
            if answer == 2:
                break

    print(answer)
