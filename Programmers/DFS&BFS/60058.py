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
'''
'''
from collections import deque
def solution(p):
    # 올바른 괄호 문자열인지 여부 파악
    def check(w):
        que = deque()
        for i in w:
            if i == '(':
                que.append('(')
            else:
                if que:
                    que.popleft()
                else:
                    return False
        if que:
            return False
        return True
        
    def func(w):
        if w == '':
            return ''
        
        u, v = '', ''
        for idx, i in enumerate(w):
            u += i
            if u.count('(') == u.count(')'): # 균형잡힌 문자열
                v = w[idx + 1:]
                break
        
        if check(u):
            u += func(v)
        else:
            u = u[1:-1] # 첫 번째, 마지막 문자 제거
            new_u = ''
            for i in u:
                if i == '(':
                    new_u += ')'
                else:
                    new_u += '('
            u = '(' + func(v) + ')' + new_u
        return u
    
    if check(p):
        return p
    x = func(p)
    return x
            