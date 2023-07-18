"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42891

< 무지의 먹방 라이브 >
"""
import heapq


def solution(food_times, k):
    if sum(food_times) <= k:  # 음식 먹는 데 걸리는 시간이 k보다 작거나 같다면 -1
        return -1

    q = []  # 우선순위 큐
    for i in range(len(food_times)):  # 우선순위 큐(최소 힙) 생성
        heapq.heappush(q, (food_times[i], i + 1))  # 음식 시간과 음식 번호를 넣어준다

    length = len(food_times)
    prev = 0

    while True:
        # q[0][0] : 힙의 가장 상단 부분으로 음식 시간이 제일 적은 것이 해당된다.
        if k > (q[0][0] - prev) * length:  # k보다 가장 적게 걸리는 음식 * 남은 음식 수가 작은 경우,
            k -= (q[0][0] - prev) * length  # 가장 적게 걸리는 음식을 다 먹을 때까지 소요된 시간을 빼준다.
            length -= 1
            prev, _ = heapq.heappop(q)
        else:
            i = k % length
            q.sort(key=lambda x: x[1])
            return q[i][1]


"""
"""


def solution2(food_times, k):
    if sum(food_times) <= k:
        return -1

    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    prev = 0
    length = len(food_times)

    while (q[0][0] - prev) * length < k:
        k -= (q[0][0] - prev) * length
        length -= 1
        prev, _ = heapq.heappop(q)

    result = sorted(q, key=lambda x: x[1])
    return result[k % length][1]


food_times = [8, 6, 4]
k = 15
print(solution2(food_times, k))
