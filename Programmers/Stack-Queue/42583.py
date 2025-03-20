'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42583

< 다리를 지나는 트럭 >
'''
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    truck_weights = deque(truck_weights)    
    bridge = deque([0] * bridge_length)
    currentWeight = 0
    # 트럭이 모두 다리를 건널 때까지
    while len(truck_weights) != 0:
        b = bridge.popleft()
        currentWeight -= b
        
        if (currentWeight + truck_weights[0] <= weight):
            tw = truck_weights.popleft()
            bridge.append(tw)
            currentWeight += tw
        else:
            bridge.append(0)
        time += 1
    time += bridge_length    
    return time

'''
'''
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    sum_weight = 0
    truck_weights = deque(truck_weights)
    
    while truck_weights:
        answer += 1
        w = bridge.popleft()
        sum_weight -= w
        tw = truck_weights[0]
        if (tw + sum_weight) <= weight:
            tw = truck_weights.popleft()
            bridge.append(tw)
            sum_weight += tw
        else:
            bridge.append(0)
    
    for idx, x in enumerate(list(bridge)[::-1]):
        if x != 0:
            answer += bridge_length - idx
            break
    
    return answer