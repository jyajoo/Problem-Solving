'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15008/lessons/121686

< 운영체제 >
'''

import heapq

def solution(programs):
    time = 0
    programs.sort(key = lambda x : (x[1], x[0]))
    idx = 0
    waiting = []
    answer = [0 for _ in range(10)]
    program = []    
    
    while idx < len(programs) or len(waiting) != 0:    
        for i in range(idx, len(programs)):
            if programs[idx][1] <= time:
                heapq.heappush(waiting, programs[idx])
                idx += 1
            else:
                break
        if len(waiting) != 0:
            program = heapq.heappop(waiting)
            answer[program[0] - 1] += time - program[1]
            time += program[2]
        else:
            time += 1
            
    return [time] + answer
    
'''
'''
import heapq

def solution(programs):
    time = 0
    programs.sort(key = lambda x : (x[1], x[0]))
    idx = 0
    waiting = []
    answer = [0 for _ in range(10)]
    program = []    
    
    while idx < len(programs):    
        for i in range(idx, len(programs)):
            if programs[idx][1] <= time:
                heapq.heappush(waiting, programs[idx])
                idx += 1
            else:
                break
        if len(waiting) != 0:
            program = heapq.heappop(waiting)
            answer[program[0] - 1] += time - program[1]
            time += program[2]
        else:
            time += 1
    
    while len(waiting) > 0:
        program = heapq.heappop(waiting)
        answer[program[0] - 1] += 0 if time - program[1] < 0 else time - program[1]
        time += program[2]

    return [time] + answer
    