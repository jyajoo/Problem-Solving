"""
구름톤 챌린지 - https://level.goorm.io/exam/195699/%EA%B7%B8%EB%9E%98%ED%94%84%EC%9D%98-%EB%B0%80%EC%A7%91%EB%8F%84/quiz/1

< 통신망 분석 >
"""
import sys
from collections import defaultdict

input = sys.stdin.readline


def find_parent(a):
    if parent[a] != a:
        return find_parent(parent[a])
    else:
        return a


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[a] = b
    else:
        parent[b] = a


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parent = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    union(a, b)

union = defaultdict(list)
for i in range(1, n + 1):
    p = find_parent(i)
    union[p] += [i]

result = []
for values in union.values():
    count = 0
    for j in values:
        count += len(graph[j])
    result.append((count / len(values), len(values), min(values), values))

result.sort(key=lambda x: (-x[0], x[1], x[2]))

for i in result[0][3]:
    print(i, end=" ")
"""
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start):
    queue = deque([start])
    component = set()
    while queue:
        q = queue.popleft()
        visited[q] = True
        component.add(q)
        for i in graph[q]:
            if not visited[i]:
                queue.append(i)
    
    edge = 0

    for i in component:
        for j in graph[i]:
            if i in graph[j]:
                edge += 1
    
    return sorted(list(component)), edge / len(component)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []
max_density = 0

for i in range(1, n + 1):
    if not visited[i]:
        component, density = bfs(i)
        '''
        실수값끼리 ==을 이용하여 비교하는 것보다 아래처럼 사용하여 비교하는 것이 안전하다.
        두 실수값의 차이가 1e-8보다 작다면, 같은 값이라고 생각한다.
        '''
        if abs(density - max_density) < 1e-8:
            if len(result) > len(component):
                result = component
                max_density = density
            elif len(result) == len(component):
                if result[0] > component[0]:
                    result = component
                    max_density = density
        
        elif density > max_density:
            result = component
            max_density = density

print(*result)