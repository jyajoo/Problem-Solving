"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/150369

< 택배 배달과 수거하기 >
"""


def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = [(i + 1, deliveries[i]) for i in range(n) if deliveries[i] > 0]
    pickups = [(i + 1, pickups[i]) for i in range(n) if pickups[i] > 0]

    # 전부 배달 & 수거될 때까지
    while deliveries or pickups:
        delivery_box = 0
        pickup_box = 0
        dist = 0

        # 배달
        while deliveries and delivery_box < cap:
            d, delivery = deliveries.pop()
            # 전부 배달 가능한 경우
            if delivery_box + delivery <= cap:
                delivery_box += delivery
                dist = max(dist, d)
            # 일부만 배달 가능한 경우
            else:
                deliveries.append((d, delivery - (cap - delivery_box)))  # 다시 담아주기
                delivery_box = cap
                dist = max(dist, d)
                break

        # 수거
        while pickups and pickup_box < cap:
            d, pickup = pickups.pop()
            # 전부 수거 가능한 경우
            if pickup_box + pickup <= cap:
                pickup_box += pickup
                dist = max(dist, d)
            # 일부만 수거 가능한 경우
            else:
                pickups.append((d, pickup - (cap - pickup_box)))  # 다시 담아주기
                pickup_box = cap
                dist = max(dist, d)
                break

        answer += dist * 2
    return answer

'''
'''
import heapq

def solution(cap, n, deliveries, pickups):
    answer = 0
    delivery_heapq = []    
    for i, d in enumerate(deliveries):
        if d > 0:
            heapq.heappush(delivery_heapq, (-(i + 1), d))
    pickup_heapq = []    
    for i, p in enumerate(pickups):
        if p > 0:
            heapq.heappush(pickup_heapq, (-(i + 1), p))
    
    while delivery_heapq or pickup_heapq:
        cap_d = cap
        cap_p = cap
        max_dist = 0
        while delivery_heapq and cap_d > 0:
            dist, delivery = heapq.heappop(delivery_heapq)
            max_dist = max(max_dist, -dist)
            
            if cap_d >= delivery:
                cap_d -= delivery
            else:
                delivery -= cap_d
                cap_d = 0
                heapq.heappush(delivery_heapq, (dist, delivery))
            
        while pickup_heapq and cap_p > 0:
            dist, pickup = heapq.heappop(pickup_heapq)
            max_dist = max(max_dist, -dist)
        
            if cap_p >= pickup:
                cap_p -= pickup
            else:
                pickup -= cap_p
                cap_p = 0
                heapq.heappush(pickup_heapq, (dist, pickup))
        answer += max_dist * 2
    return answer