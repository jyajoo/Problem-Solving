"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/258711

< 도넛과 막대 그래프 >
"""
from collections import defaultdict


def solution(edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)

    for s, e in edges:
        graph[s].append(e)
        out_degree[s] += 1
        in_degree[e] += 1

    # 임의로 생성된 노드는 진입 간선의 개수가 0개이고 진출 간선의 개수가 많음
    created_node = 0
    count = 0
    for v, e in out_degree.items():
        if in_degree[v] == 0 and count < e:
            count = e
            created_node = v

    def dfs(now):
        visited = set()
        stack = [now]
        v, e = 0, 0
        while stack:
            now = stack.pop()
            if now not in visited:
                visited.add(now)
                v += 1
                e += len(graph[now])
                stack.extend(graph[now])
        return v, e

    # 그래프 DFS 탐색하여 정점의 개수, 간선의 개수 구하기
    a, b, c = 0, 0, 0  # 도넛, 막대, 8자 그래프의 개수
    for now in graph[created_node]:
        v, e = dfs(now)

        if v == e:
            a += 1
        elif v == e + 1:
            b += 1
        else:
            c += 1
    return [created_node, a, b, c]

'''
'''
from collections import defaultdict
import sys

sys.setrecursionlimit(10**6)

def solution(edges):
    def dfs(now):
        nonlocal nc, ec
        visited.add(now) 
        nc += 1 
        ec += len(graph[now]) 
        
        for i in graph[now]:
            if i not in visited: 
                dfs(i)
    
    answer = [0, 0, 0, 0]
    
    graph = defaultdict(list)  
    in_degree = defaultdict(int)  # 해당 노드로 들어오는 간선 개수
    out_degree = defaultdict(int)  # 해당 노드에서 나가는 간선 개수
    
    for s, e in edges:
        in_degree[e] += 1
        out_degree[s] += 1
        graph[s].append(e)
        
    create_node = 0
    count = 0
    for v, e in out_degree.items():
        if in_degree[v] == 0 and count < e:
            count = e
            create_node = v
    
    answer[0] = create_node
    
    visited = set()
    for now in graph[create_node]:
        if now not in visited:  # 방문되지 않은 노드만 탐색
            nc, ec = 0, 0
            dfs(now)
            
            if nc == ec:  # 도넛 모양 그래프
                answer[1] += 1
            elif nc == ec + 1:  # 막대 모양 그래프
                answer[2] += 1
            else:  # 8자 모양 그래프
                answer[3] += 1
                
    return answer
