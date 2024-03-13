"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42861

< 섬 연결하기 >
"""


def find_parent(x):
    global parent
    if parent[x] < 0:
        return x
    else:
        parent[x] = find_parent(parent[x])
        return parent[x]


def union(x, y):
    global parent
    a = find_parent(x)
    b = find_parent(y)

    if a == b:
        return False
    else:
        parent[a] += parent[b]
        parent[b] = a
        return True


def solution(n, costs):
    answer = 0

    global parent
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = -i

    costs.sort(key=lambda x: x[2])

    for a, b, cost in costs:
        if find_parent(a + 1) != find_parent(b + 1):
            union(a + 1, b + 1)
            answer += cost

    return answer
