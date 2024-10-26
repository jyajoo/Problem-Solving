"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/150369

< 택배 배달과 수거하기 >
"""

# cap : 최대 상자 수
# n : 집의 총 수
# deliveries : 각 집에 배달할 상자 수
# pickups : 각 집에서 수거할 상자 수


def solution(cap, n, deliveries, pickups):
    answer = 0
    deliver = pickup = 0  # 현재 배달 및 수거해야 하는 상자 수

    # 가장 먼 집부터 탐색
    for i in range(n - 1, -1, -1):
        # 현재 집의 배달, 수거 상자 수 누적하기
        deliver += deliveries[i]
        pickup += pickups[i]

        # 배달 및 수거해야 할 상자가 있는 경우
        while deliver > 0 or pickup > 0:
            # cap 용량만틈 상자를 처리한다.
            # 음수가 되어도 상관이 없는 이유는 다음 집을 이어서 처리할 수 있기 때문
            deliver -= cap
            pickup -= cap
            answer += (i + 1) * 2

    return answer
