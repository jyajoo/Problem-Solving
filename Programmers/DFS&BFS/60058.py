"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/60058?language=python3

< 괄호 변환 >
"""


def balance(p):
    return p.count("(") == p.count(")")


def correct(p):
    cnt = 0
    for i in p:
        if i == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    return True


def solution(p):
    answer = ""
    if p == "":
        return answer

    u, v = p, ""
    for i in range(1, len(p) + 1):
        if balance(p[:i]):
            u = p[:i]
            v = p[i:]
            break

    if correct(u):
        answer = u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)

    return answer
