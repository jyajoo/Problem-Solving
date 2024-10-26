"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/258709

< 주사위 고르기 >
"""

from itertools import combinations
from bisect import bisect_left


def solution(dice):

    def get_scores(dices):
        def dfs(step, score):
            if step == len(dices):
                results.append(score)
                return

            for i in dices[step]:
                dfs(step + 1, score + i)

        results = []
        dfs(0, 0)
        return results

    n = len(dice)
    half = n // 2

    max_rate = 0
    best_combination = []

    for comb in combinations(range(n), half):
        a_dices = [dice[i] for i in comb]
        b_dices = [dice[i] for i in set(range(n)) - set(comb)]
        a_scores = get_scores(a_dices)
        b_scores = get_scores(b_dices)
        b_scores.sort()
        total = len(a_scores) * len(b_scores)

        win = 0
        for a in a_scores:
            # b_scores에서 a가 삽입될 수 있는 가장 왼쪽 인덱스 찾기
            idx = bisect_left(b_scores, a)
            win += idx

        rate = win / total

        if rate > max_rate:
            max_rate = rate
            best_combination = comb
    return [i + 1 for i in sorted(best_combination)]


"""
과거 코드..
"""
from itertools import combinations
from collections import defaultdict


def solution(dice):
    def dfs(step, score, type):
        if type == 0 and step == len(a_dices):
            a_scores[score] += 1
            return
        elif type == 1 and step == len(b_dices):
            b_scores[score] += 1
            return

        if type == 0:
            dices = a_dices[step]
        else:
            dices = b_dices[step]
        for i in dices:
            dfs(step + 1, score + i, type)

    numbers = [i for i in range(len(dice))]

    max_val = 0.0
    result = []
    for a_idx in combinations(numbers, len(dice) // 2):
        a_dices = [dice[i] for i in a_idx]
        b_idx = set(numbers) - set(a_idx)
        b_dices = [dice[i] for i in b_idx]

        a_scores = defaultdict(int)
        b_scores = defaultdict(int)
        dfs(0, 0, 0)
        dfs(0, 0, 1)

        total = 0
        win = 0
        for a_score, a_count in a_scores.items():
            for b_score, b_count in b_scores.items():
                total += a_count * b_count
                if a_score > b_score:
                    win += a_count * b_count

        if max_val < (win / total):
            max_val = win / total
            result = list(a_idx)

    arr = [i + 1 for i in result]
    arr.sort()
    return arr
