"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/181188

< 요격 시스템 >
"""


def solution(targets):
    answer = 1
    targets.sort(key=lambda x: x[1])

    now_e = targets[0][1] - 0.5
    for s, e in targets:
        if now_e < s or now_e > e:
            now_e = e - 0.5
            answer += 1

    return answer


"""
"""


def solution(targets):
    targets.sort(key=lambda x: (x[1]))
    answer = [0]
    for s, e in targets:
        if answer[-1] > s and answer[-1] < e:
            continue
        answer.append(e - 0.5)

    return len(answer) - 1
'''
'''
def solution(targets):
    targets.sort(key = lambda x : (x[1]))
    answer = 1
    prev = targets[0][1] - 1
    for idx, (x, y) in enumerate(targets[1:]):
        if x > prev or prev > y:
            answer += 1
            prev = y - 1
    
    return answer