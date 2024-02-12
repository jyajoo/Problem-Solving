"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42889

< 실패율 >
"""


def solution(N, stages):
    lst = []
    answer = []
    stages.sort()
    for i in range(N):
        count = 0
        count2 = 0
        total = 0
        for j in range(len(stages)):
            if stages[j] > i + 1:
                break
            if stages[j] == i + 1:
                count += 1
            else:
                count2 += 1
        if j != 0:
            total = len(stages) - count2
        if count != 0 and total != 0:
            p = count / total
        else:
            p = 0
        lst.append((i + 1, p))
    lst.sort(key=lambda x: -x[1])
    for i, _ in lst:
        answer.append(i)
    return answer


N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
'''
'''
def solution(N, stages):
    result = {}
    length = len(stages)
    for stage in range(1, N + 1):
        if length != 0:
            count = stages.count(stage)
            result[stage] = count / length
            length -= count
        else:
            result[stage] = 0
    
    return sorted(result, key = lambda x : result[x], reverse=True)