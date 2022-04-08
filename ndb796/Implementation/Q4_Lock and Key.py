'''
프로그래머스 - https://programmers.co.kr/learn/courses/30/lessons/60059

< 자물쇠와 열쇠 >

- 회전과 이동을 통해 열쇠 돌기 부분과 자물쇠의 홈 부분이 일치해야 한다.
- 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안된다.

- 3배 확장하여 그 중앙에 자물쇠를 배치한다.
- 완전 탐색으로 모두 1이 되는 점을 찾는다.
'''

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

# 열쇠 회전 - 1열을 역순으로 1행으로 만든다.
def rotation(key):
    key = []
    for i in range(len(key)):
        rotate = []
        for j in range(len(key) - 1, -1, -1):
            rotate.append(key[j][i])
        key.append(rotate)
    return key

def solution(key, lock):
    lenKey = len(key)
    lenLock = len(lock)
    expan = [[0] * lenLock * 3 for _ in range(lenLock * 3)]   # 3배 확장한 곳에 자물쇠를 배치한다.
    for i in range(lenLock):
        for j in range(lenLock):
            expan[i + lenLock][j + lenLock] = lock[i][j]

solution(key, lock)