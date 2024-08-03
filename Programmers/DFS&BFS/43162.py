"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/43162

< 네트워크 >
"""


def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x == y:
        return False
    else:
        parent[x] += parent[y]
        parent[y] = x
        return True


def find_parent(x):
    global parent
    if parent[x] < 0:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


parent = []


def solution(n, computers):
    global parent
    answer = 0
    parent = [-i for i in range(n + 1)]

    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(i + 1, j + 1)

    for i in parent:
        if i < 0:
            answer += 1

    return answer


"""
"""


def dfs(i):
    global visited
    stack = [i]
    visited[i] = True
    while stack:
        x = stack.pop()
        for idx, i in enumerate(computers[x]):
            if i and not visited[idx]:
                visited[idx] = True
                stack.append(idx)


visited = []
computers = []
length = 0


def solution(n, computer):
    global visited, computers, length
    length = n
    computers = computer
    answer = 0

    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1

    return answer
