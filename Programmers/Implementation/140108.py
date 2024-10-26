"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/140108

< 문자열 나누기 > 
"""


def solution(s):
    x = s[0]
    x_count = 1  # x의 개수
    not_x_count = 0  # x가 아닌 다른 글자의 개수
    answer = 0

    for i in range(1, len(s) - 1):
        if x != s[i]:
            not_x_count += 1
        else:
            x_count += 1

        if x_count == not_x_count:
            x = s[i + 1]
            x_count = 0
            not_x_count = 0
            answer += 1

    return answer + 1
