"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/340212

< 퍼즐 게임 챌린지 >
"""


def solution(diffs, times, limit):
    answer = int(1e9)
    start = min(diffs)
    end = max(diffs)

    while start <= end:
        middle = (start + end) // 2
        total_time = 0
        for i in range(len(diffs)):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = 0
            if i != 0:
                time_prev = times[i - 1]

            if diff <= middle:
                total_time += time_cur
            else:
                total_time += (diff - middle) * (time_cur + time_prev) + time_cur
        if total_time <= limit:
            answer = min(answer, middle)
            end = middle - 1
        else:
            start = middle + 1

    return answer


"""
"""


def solution(diffs, times, limit):
    start, end = min(diffs), max(diffs)
    answer = int(1e9)
    while start <= end:
        middle = (start + end) // 2
        total_time = 0
        for idx in range(len(diffs)):
            diff = diffs[idx]
            time = times[idx]
            if middle >= diff:
                total_time += time
            else:
                total_time += (diff - middle) * (time + times[idx - 1]) + time
        if total_time <= limit:
            answer = min(answer, middle)
            end = middle - 1
        else:
            start = middle + 1
    return answer
'''
'''
def solution(diffs, times, limit):
    answer = int(1e9)
    answer_time = int(1e9)
    start = 1
    end = max(diffs)
    
    while start <= end:
        level = (start + end) // 2
        result = 0
        time_prev = 0
        for diff, time_cur in zip(diffs, times):
            if diff <= level:
                result += time_cur
            else:
                result += (diff - level) * (time_cur + time_prev) + time_cur
            time_prev = time_cur
        if result <= limit:
            if answer > level:
                answer_time = result
                answer = level
            end = level - 1
        else:
            start = level + 1
            
    return answer