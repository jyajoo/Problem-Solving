"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/77484

< 로또의 최고 순위와 최저 순위 >
"""


def solution(lottos, win_nums):
    def get_rank(n):
        rank = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
        return rank[n]

    count = 0
    score = 0
    for i in lottos:
        if i in win_nums:
            score += 1
        elif i == 0:
            count += 1

    return [get_rank(score + count), get_rank(score)]
