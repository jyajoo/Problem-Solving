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
    rotate = []
    for i in range(len(key)):
        row = []
        for j in range(len(key) - 1, -1, -1):
            row.append(key[j][i])
        rotate.append(row)
    return rotate

def allOne(expan):
    lenEx = len(expan) // 3
    for i in range(lenEx, lenEx * 2):
        for j in range(lenEx, lenEx * 2):
            if expan[i][j] != 1:
                return False
    return True

def solution(key, lock):
    lenKey = len(key)
    lenLock = len(lock)

    # 3배 확장한 곳에 자물쇠를 배치한다.
    expan = [[0] * lenLock * 3 for _ in range(lenLock * 3)]   
    for i in range(lenLock):
        for j in range(lenLock):
            expan[i + lenLock][j + lenLock] = lock[i][j]

    for _ in range(4):
        
        key = rotation(key)

        for x in range(1, lenLock * 2):
            for y in range(1, lenLock * 2):

                # 열쇠 넣기
                for i in range(lenKey):
                    for j in range(lenKey):
                        expan[x + i][y + j] += key[i][j]

                # 모두 1일 되는지 확인
                if allOne(expan):
                    return True

                # 열쇠 빼기
                for i in range(lenKey):
                    for j in range(lenKey):
                        expan[x + i][y + j] -= key[i][j]
    return False
    
solution(key, lock)
