"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42885

< 구명보트 >
"""


def solution(people, limit):
    answer = 0
    people.sort()

    a, b = 0, len(people) - 1

    while a <= b:
        if people[a] + people[b] <= limit:
            answer += 1
            a += 1
            b -= 1
        else:
            answer += 1
            b -= 1

    return answer
