"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/43163

< 단어 변환 >
"""


def dfs(word, count):
    global visited, answer

    if word == target:
        answer = min(answer, count)
        return
    for idx, next_word in enumerate(words):
        cnt = 0
        for i in range(length):
            if word[i] != next_word[i]:
                cnt += 1
        if cnt == 1 and not visited[idx]:
            visited[idx] = True
            dfs(next_word, count + 1)
            visited[idx] = False


target = ""
length = 0
visited = []
words = []
answer = 0


def solution(begin, t, w):
    global target, length, visited, words, answer
    words = w
    length = len(begin)
    visited = [False] * len(words)
    target = t
    answer = int(1e9)

    dfs(begin, 0)
    if answer == int(1e9):
        answer = 0
    return answer


"""
"""
from collections import deque


def diff_count(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    return False


def solution(begin, target, words):
    if target not in words:
        return 0

    q = deque()
    q.append((begin, 0))
    visited = [False] * len(words)

    while True:
        now, cnt = q.popleft()

        if now == target:
            return cnt

        for i, word in enumerate(words):
            if not visited[i] and diff_count(now, word):
                visited[i] = True
                q.append((word, cnt + 1))

    return 0
