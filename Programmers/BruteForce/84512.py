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


"""
"""
from itertools import product


def dfs(w, word):
    global answer
    global cnt
    cnt += 1

    if w == word:
        answer = cnt
        return

    if len(w) >= 5:
        return

    for i in ["A", "E", "I", "O", "U"]:
        dfs(w + i, word)


answer = 0
cnt = -1


def solution(word):
    global answer
    dfs("", word)
    return answer

'''
'''
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = 0
    step = 4
    while word:
        count = 0
        for i in range(step, -1, -1):
            count += 5 ** i
        
        for i in alpha:
            if word.startswith(i):
                word = word[1:]
                step -= 1
                answer += 1
                break
            answer += count
    return answer
        