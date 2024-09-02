"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/178871

< 달리기 경주 >
"""

from collections import defaultdict


def solution(players, callings):
    rank = defaultdict(int)
    rank_2 = defaultdict(str)
    for i in range(len(players)):
        rank[players[i]] = i
        rank_2[i] = players[i]

    for i in callings:
        r = rank[i]  # 현재 선수의 순위
        x = rank_2[r - 1]  # 현재 선수보다 앞선 선수의 이름
        rank[x] = r
        rank[i] = r - 1
        rank_2[r] = x
        rank_2[r - 1] = i

    arr = list(rank.items())
    arr.sort(key=lambda x: x[1])
    return [i[0] for i in arr]


"""
"""


def solution(players, callings):
    rank = dict()
    rank_2 = dict()
    for i, player in enumerate(players):
        rank[player] = i
        rank_2[i] = player

    for i in callings:
        r = rank[i]  # 현재 선수의 순위
        x = rank_2[r - 1]  # 현재 선수보다 앞선 선수의 이름
        rank[x] = r
        rank[i] = r - 1
        rank_2[r] = x
        rank_2[r - 1] = i

    return [rank_2[i] for i in range(len(players))]
