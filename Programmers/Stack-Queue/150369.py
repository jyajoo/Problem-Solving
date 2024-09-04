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
