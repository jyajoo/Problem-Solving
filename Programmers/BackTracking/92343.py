"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/92343

< 양과 늑대 >
"""

answer = 0
graph = []


def find_sheep(visited, info, sheep, wolf, now, arr):
    global answer
    answer = max(answer, sheep)

    for i in graph[now]:
        arr.append(i)

    for i in arr:
        if info[i] == 0 and not visited[i]:
            visited[i] = True
            new_arr = arr[:]
            new_arr.remove(i)
            find_sheep(visited, info, sheep + 1, wolf, i, new_arr)
            visited[i] = False
        elif info[i] == 1 and not visited[i]:
            if sheep > wolf + 1:
                visited[i] = True
                new_arr = arr[:]
                new_arr.remove(i)
                find_sheep(visited, info, sheep, wolf + 1, i, new_arr)
                visited[i] = False


def solution(info, edges):
    global graph
    graph = [[] for _ in range(len(info))]
    visited = [False] * len(info)
    for a, b in edges:
        graph[a].append(b)

    visited[0] = True
    sheep, wolf = 1, 0
    find_sheep(visited, info, sheep, wolf, 0, [])
    return answer
