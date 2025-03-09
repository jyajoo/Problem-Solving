"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12951

< JadenCase 문자열 만들기 >
"""


def solution(s):
    answer = ""

    flag = True
    for i in s:
        if i == " ":
            flag = True
            answer += i
        elif flag:
            flag = False
            if i.isalpha():
                answer += i.upper()
            else:
                answer += i
        else:
            answer += i.lower()

    return answer
