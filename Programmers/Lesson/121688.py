'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/15009/lessons/121688

< 신입사원 교육 >
'''
import heapq

def solution(ability, number):
    answer = sum(ability)
    heapq.heapify(ability) 
    for i in range(number):
        num1 = heapq.heappop(ability)
        num2 = heapq.heappop(ability)
        num = num1 + num2
        heapq.heappush(ability, num)
        heapq.heappush(ability, num)
        answer += num
    return answer