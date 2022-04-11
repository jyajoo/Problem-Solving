'''
백준 - https://www.acmicpc.net/problem/3190

< 뱀 >

- 처음에는 오른쪽을 향한다.
- 바라보고 있는 방향에 따라 좌우에 맞춰 머리 이동
- 뱀의 머리가 먼저 이동, 사과가 있는지 확인
- 있다면 꼬리는 그대로, 없다면 기존에 이동해온 기록에 따라 꼬리 이동.
'''

from collections import deque

n = int(input())   # 보드의 크기
board = [[0] * n for _ in range(n)]
board[0][0] = 2   # 뱀의 몸통이 위치하는 곳은 2로

k = int(input())   # 사과의 개수 (1행 1열에는 사과가 없다.)
for _ in range(k):
    x, y = map(int, input().split())
    board[x - 1][y - 1] = 1

l = int(input())   # 뱀의 방향 변환 횟수
direct = []
for _ in range(l):
    direct.append((input().split()))

head= [0, 0]
tail = [0, 0]
time = 0
process = deque()

# 바라보는 방향(상하좌우)에 따른 이동
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 바라보는 방향 방향에 따른 좌우 이동(move의 인덱스); 상 - 좌우, 하 - 우좌, 좌 - 하상, 우 - 상하
ld = [(2, 3), (3, 2), (1, 0), (0, 1)]

idx = 3  # 처음 이동은 오른쪽
while True:

    head[0] += move[idx][0]
    head[1] += move[idx][1]
    time += 1
    x, y = head[0], head[1]
    process.append([x, y])     # 뱀의 이동 기록(꼬리 땡겨올 때 필요)

    # 맵을 벗어나거나 뱀의 몸(2)과 부딪힐 경우 break
    if head[0] == n or head[1] == n or head[0] < 0 or head[1] < 0 or board[head[0]][head[1]] == 2:
        print(time)
        break

    # 사과가 있는지 확인
    if board[head[0]][head[1]] != 1:
        board[tail[0]][tail[1]] = 0   # 없을 경우, 0으로 다시 바꿔주고, 꼬리를 한 칸 이동시켜준다.
        a = process.popleft()
        tail = a

    board[head[0]][head[1]] = 2       # 뱀 위치 표시

    # 바라보고 있는 방향에 따라 회전
    for i in direct:
        if int(i[0]) == time:
            if i[1] == 'L':
                idx = ld[idx][0]
            else:
                idx = ld[idx][1]

'''
책에서의 풀이

'''
