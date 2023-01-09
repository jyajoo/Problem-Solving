'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15008/lessons/121685

< 유전 법칙 >
'''

def bean(generation, order):
    if generation == 1: return "Rr"

    parent = bean(generation - 1, (order - 1) // 4 + 1)
    if parent == "RR" or parent == "rr": return parent

    if order % 4 == 0:
        return "rr"
    elif order % 4 == 1:
        return "RR"
    else:
        return "Rr"
    

def solution(queries):
    answer = []
    for query in queries:
        answer.append(bean(query[0], query[1]))
    return answer