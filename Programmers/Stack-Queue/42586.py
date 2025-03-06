"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42586

< 기능 개발 >
"""


def solution(progresses, speeds):
    answer = []

    prev = -1
    for i, p in enumerate(progresses):
        day = (100 - p) / speeds[i]

        if day > (100 - p) // speeds[i]:
            day = (100 - p) // speeds[i] + 1

        if prev >= day:
            answer[-1] += 1
        else:
            answer.append(1)
            prev = day

    return answer

'''
'''
def solution(progresses, speeds):
    answer = []
    ex_time = -1
    count = 0
    for idx, progress in enumerate(progresses):
        time = (100 - progress) // speeds[idx]
        if (100 - progress) % speeds[idx] != 0:
            time += 1
        
        if ex_time < time:
            ex_time = time
            if idx != 0:
                answer.append(count)
            count = 1
            
        elif time <= ex_time:
            count += 1
            
    answer.append(count)
    
    return answer
