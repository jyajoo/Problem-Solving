"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/250136

< 석유 시추 >
"""

from collections import deque

land = []
visited = []


def bfs(i, j, num):
    global land, visited, n, m

    q = deque()
    q.append((i, j))
    count = 1
    visited[i][j] = num
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if land[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = num
                count += 1
                q.append((nx, ny))
    return count


def solution(l):
    global land, visited, n, m
    land = l
    result = 0
    n, m = len(l), len(l[0])
    visited = [[0] * m for _ in range(n)]
    size = [0]
    num = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                size.append(bfs(i, j, num))
                num += 1

    for j in range(m):
        count = 0
        nums = []
        for i in range(n):
            if land[i][j] == 1:
                num = visited[i][j]
                if num not in nums:
                    nums.append(num)
                    count += size[num]
        result = max(result, count)
    return result
'''
'''
from collections import deque
def solution(land):
    def bfs(i, j, room_number):
        nonlocal visited
        q = deque()
        q.append((i, j))
        visited[i][j] = True
        land[i][j] = room_number
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 1
        while q:
            x, y = q.popleft()
            
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                    continue
                if not visited[nx][ny] and land[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    count += 1
                    land[nx][ny] = room_number
        return count
                    
            
    answer = 0
    room_number = 1
    rooms = [0]
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    for i in range(len(land)):
        for j in range(len(land[0])):
            if not visited[i][j] and land[i][j]:
                count = bfs(i, j, room_number)
                rooms.append(count)
                room_number += 1
    for j in range(len(land[0])):
        room_numbers = set()
        for i in range(len(land)):
            if land[i][j] != 0:
                room_numbers.add(land[i][j])
        
        result = 0
        for i in room_numbers:
            result += rooms[i]
        answer = max(answer, result)
    
    
    return answer