"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42627

< 디스크 컨트롤러 >
"""

import heapq


def solution(jobs):
    answer = 0
    heapq.heapify(jobs)
    possible = []
    total_time = 0
    l = len(jobs)
    cnt = l

    while cnt != 0:
        while jobs:
            start, time = heapq.heappop(jobs)
            if start <= total_time:
                heapq.heappush(possible, (time, start))
            else:
                heapq.heappush(jobs, [start, time])
                break
        if possible:
            time, start = heapq.heappop(possible)
            total_time += time
            answer += total_time - start
            cnt -= 1
        else:
            total_time += 1

    return answer // l
