"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/87946

< 피로도 >
"""

from itertools import permutations


def solution(k, dungeons):
    answer = -1
    for arr in permutations(dungeons, len(dungeons)):
        count = 0
        tired = k
        for a, b in arr:  # 최소 필요 피로도, 소모 피로도
            if tired >= a:
                count += 1
                tired -= b
            else:
                break
        answer = max(answer, count)

    return answer
