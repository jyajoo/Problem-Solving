"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/67258?language=python3

< 보석 쇼핑 >
"""


def solution(gems):
    answer = []
    total_type = len(set(gems))
    start = 0
    types = dict()
    length = int(1e9)
    for idx, gem in enumerate(gems):
        if gem not in types:
            types[gem] = 1
        else:
            types[gem] += 1

        if len(types) == total_type:
            for i in range(start, idx + 1):
                if types[gems[i]] >= 2:
                    types[gems[i]] -= 1
                else:
                    break
            start = i
            if (idx - start + 1) < length:
                length = idx - start + 1
                answer = [start + 1, idx + 1]

    return answer


"""
"""
from collections import defaultdict


def solution(gems):
    answer = []
    total_type = len(set(gems))
    start = 0
    types = defaultdict(int)
    length = int(1e9)
    for end, gem in enumerate(gems):
        types[gem] += 1

        while len(types) == total_type:
            if (end - start + 1) < length:
                length = end - start + 1
                answer = [start + 1, end + 1]
            types[gems[start]] -= 1
            if types[gems[start]] == 0:
                del types[gems[start]]
            start += 1
    return answer
