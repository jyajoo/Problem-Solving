'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42576

< 완주하지 못한 선수 >
'''

# solution_1
from collections import Counter

def solution(participant, completion):
    participantCnt = Counter(participant)
    completionCnt = Counter(completion)

    for i in participant:
        if participantCnt[i] != completionCnt[i]:
            return i


# solution_2
def solution(participant, completion):
    data = dict()
    for i in participant:
        if data.get(i, 0) == 0:
            data[i] = 1
        else:
            data[i] += 1
    
    for i in completion:
        if data.get(i, 0) == 0:
            return i
        else:
            data[i] -= 1
            if data[i] == 0:
                data.pop(i)
    return list(data.keys())[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

print(solution(participant, completion))

'''
< 시간 초과 >


def solution(participant, completion):
    for i in participant:
        if i not in completion:
            return i
        
        else:
            completion.pop(completion.index(i))

def solution(participant, completion):
    for i in participant:
        if participant.count(i) != completion.count(i):
            return i
'''
