"""
백준 - https://www.acmicpc.net/problem/31092

< 스티커 재배치 >
"""
import sys

input = sys.stdin.readline
import copy


def calc(start, end):
    global answer
    cost = 0
    storage = []
    k_board = board[start:end]
    now_board = copy.deepcopy(board)
    # 떼서 보관하기
    for i in range(k):
        alpha, d, _ = k_board[i]
        s_alpha = s[i]
        if alpha != s_alpha:
            storage.append((alpha))
            cost += d

    for i in range(k):
        alpha, d, a = k_board[i]
        s_alpha = s[i]
        if alpha != s_alpha:
            # 보관함에 스티커가 있는지 확인
            for storage_alpha in storage:
                if storage_alpha == s_alpha:
                    storage.remove(storage_alpha)
                    break
            else:
                # 스티커를 구매하는 경우
                s_a = int(1e9)
                for j in range(m):
                    _, sticker, _, sticker_a = stickers[j]
                    if sticker == s_alpha:
                        s_a = sticker_a
                        break

                # k 구역 외의 다른 곳에서 떼는 비용이 가장 적은 스티커를 떼온다
                min_d = int(1e9)
                idx = 0
                for i in range(n):
                    if i < start or i >= end:
                        board_alpha, board_d, _ = now_board[i]
                        if board_alpha == s_alpha:
                            if min_d > board_d:
                                min_d = board_d
                                idx = i

                if s_a < min_d:
                    cost += s_a
                else:
                    now_board[idx] = ('0', 0, 0)
                    cost += min_d
    answer = min(answer, cost)


# 보드판의 칸 개수, 스티커 종류, 문자열 길이
n, m, k = map(int, input().split())

stickers = []
for i in range(m):
    # 알파벳 소문자, 떼는 비용, 구매 비용
    s, d, a = input().split()
    stickers.append((i, s, int(d), int(a)))

stickers.sort(key=lambda x: x[3])
# 각 칸에 부여된 스티커 번호
board_numbers = list(map(int, input().split()))
# 문자열
s = input().strip()

board = []
for i in board_numbers:
    for j in range(m):
        num, alpha, d, a = stickers[j]
        if num == i - 1:
            board.append((alpha, d, a))

answer = int(1e9)
for i in s:
    flag = False
    for j in range(m):
        _, alpha, _, _ = stickers[j]
        if alpha == i:
            flag = True
            break
    if not flag:
        answer = -1
        break
else:
    for i in range(n):
        if i + k <= n:
            calc(i, i + k)
print(answer)
