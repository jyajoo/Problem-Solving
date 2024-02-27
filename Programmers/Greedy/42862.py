'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42862

< 체육복 >
'''

def solution(n, lost, reserve):
    answer = 0
    for i in range(1, n + 1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)
    
    for i in range(1, n + 1):
        if i in lost:
            if i - 1 in reserve:
                answer += 1
                reserve.remove(i - 1)
            elif i + 1 in reserve:
                answer += 1
                reserve.remove(i + 1)
        else:
            answer += 1
    return answer


'''
'''
def solution(n, lost, reserve):
    answer = n - len(lost)
    reserve.sort()
    lost.sort()
    for i, r in enumerate(reserve):
        for j, l in enumerate(lost):
            if r == l:
                reserve[i] = -1
                lost[j] = -1
                answer += 1
                break

    for i, r in enumerate(reserve):
        for j, l in enumerate(lost):
            if abs(r - l) == 1:
                reserve[i] = -1
                lost[j] = -1
                answer += 1
                break

    return answer
