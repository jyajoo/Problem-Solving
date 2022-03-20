'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/42891?language=python3

< 무지의 먹방 라이브 > - refine

- 우선순위 큐를 이용하여, (음식의 양, 음식 번호) 삽입
- 최소 힙으로 구성되어 있으므로, pop으로 가장 음식의 양이 적다는 것을 이용
- 남은 시간과 음식의 총 개수를 이용하여 최종적으로 먹어야 하는 음식의 번호를 출력한다.
'''

import heapq  # 우선순위 큐


def solution(food_times, k):
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))   # 우선순위 큐 삽입

    if k >= sum(food_times):      # 모든 음식을 다 먹을 시간보다 k가 큰 경우, -1 출력
        return -1

    length = len(food_times)      # 음식의 개수
    prev = 0                      # 이전에 음식을 먹는 동안 걸린 시간

    while True:
        # (양이 가장 적은 음식을 먹는 데에 걸리는 시간 - 이전에 음식을 먹는 동안 걸린 시간)  * 총 음식의 종류 가 k보다 클 경우
        if k > (q[0][0] - prev) * length:          
            k -= (q[0][0] - prev) * length         
            prev = q[0][0]                         # 이전 음식 시간 재설정
            heapq.heappop(q)                       # 가장 양이 적은 음식을 다 먹어치움
            length -= 1
        else:
            i = k % length
            q.sort(key=lambda x: x[1])             # 음식 번호순대로 오름차순 정렬
            return q[i][1]

''' pop과 append를 반복하는 방법으로, 시간 초과 발생..'''
# from collections import deque
# def solution(food_times, k):

#     times = deque()
#     for i in range(len(food_times)):
#         times.append([food_times[i], i + 1])  # 덱에 음식의 양, 음식 번호를 담는다.
#     for i in range(k + 1):
#         if  len(times) != 0:                  # 덱에 음식이 남아있는 경우
#             food = times.popleft()
#         else:
#             return -1

#         if food[0] > 0:                       # 음식의 양이 0보다 크면, 1씩 줄여나가며, 다시 덱에 삽입
#             food[0] -= 1 
#             if food[0] > 0:
#                 times.append(food)
#     return food[1]                            # k초가 되고 난 후, 먹어야 하는 음식 출력

food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times, k))
