'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/118667

< 두 큐 합 같게 만들기 >
'''
from collections import deque
def solution(queue1, queue2):
    answer = 0
    dq1 = deque(queue1)
    dq2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    for _ in range(4 * len(dq1)):
        if sum1 < sum2:
            now = dq2.popleft()
            dq1.append(now)
            sum2 -= now
            sum1 += now
        elif sum1 > sum2:
            now = dq1.popleft()
            dq2.append(now)
            sum1 -= now
            sum2 += now
        else:
            return answer
        answer += 1
    answer = -1
    return answer