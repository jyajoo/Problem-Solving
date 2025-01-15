"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12926

< 시저 암호 >
"""


def solution(s, n):
    answer = ""

    for i in s:
        if i.isalpha():
            x = ord(i) + n
            if x > ord("z") and i.islower():
                x = x - ord("z") + ord("a") - 1
            elif x > ord("Z") and i.isupper():
                x = x - ord("Z") + ord("A") - 1
            answer += chr(x)
        else:
            answer += i

    return answer


"""
"""


def solution(s, n):
    answer = ""

    for i in s:
        if i.islower():
            x = (ord(i) + n - ord("a")) % 26 + ord("a")
        elif i.isupper():
            x = (ord(i) + n - ord("A")) % 26 + ord("A")
        else:
            answer += i
            continue
        answer += chr(x)
    return answer
