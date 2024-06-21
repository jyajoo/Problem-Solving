"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/176963

< 추억 점수 >
"""

from collections import defaultdict


def solution(name, yearning, photo_list):
    answer = []
    point = defaultdict(int)
    for i in range(len(name)):
        point[name[i]] = yearning[i]

    for photo in photo_list:
        score = 0
        for p in photo:
            score += point[p]
        answer.append(score)
    return answer
