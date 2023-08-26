"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/60062

< 외벽 점검 >
"""
import sys
from itertools import permutations

input = sys.stdin.readline


def solution(n, weak, dist):
    answer = len(dist) + 1
    weak_new = weak + [i + n for i in weak]
    perm = list(permutations(dist, len(dist)))

    # 시작 지점
    for start in range(len(weak)):
        # 순열 차례대로 확인
        for friends in perm:
            count = 1  # 투입될 친구 수
            position = weak_new[start] + friends[count - 1]  # 점검할 수 있는 마지막 위치

            # 시작지점부터 n만큼 이동하며 확인
            for index in range(start, start + len(weak)):
                # 점검할 수 있는 범위를 벗어났다면
                if position < weak_new[index]:
                    count += 1  # 새로운 친구 투입
                    # 투입이 불가능하다면
                    if count > len(dist):
                        break
                    position = weak_new[index] + friends[count - 1]
            answer = min(answer, count)
    if answer > len(dist):
        return -1
    return answer

n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
