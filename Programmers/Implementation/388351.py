'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/388351

< 유연근무제 >
'''

def solution(schedules, timelogs, startday):
    answer = 0
    
    for idx, schedule in enumerate(schedules):
        start = startday
        h = schedule // 100
        m = (schedule % 100) + 10
        if m >= 60:
            h += 1
            m %= 60
        limit = h * 100 + m
        
        for time in timelogs[idx]:
            if time > limit:
                if start != 6 and start != 7:
                    break
            start += 1
            if start == 8:
                start = 1
        else:
            answer += 1    
    
    return answer