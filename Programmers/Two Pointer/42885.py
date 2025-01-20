"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42885#

< 구명보트 >
"""


def solution(people, limit):
    answer = 0
    # 몸무게 내림차순 정렬
    people.sort(reverse=True)
    start = 0
    end = len(people) - 1

    while start <= end:
        x = people[start]
        y = people[end]
        if x + y <= limit:
            start += 1
            end -= 1
        else:
            start += 1
        answer += 1

    return answer
