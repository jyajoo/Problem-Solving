"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/84512

< 모음사전 >
"""

from itertools import product


def solution(word):
    lst = ["A", "E", "I", "O", "U"]

    word_lst = []
    for i in range(1, 6):
        for p in product(lst, repeat=i):
            word_lst.append("".join(p))

    word_lst.sort()

    return word_lst.index(word) + 1
