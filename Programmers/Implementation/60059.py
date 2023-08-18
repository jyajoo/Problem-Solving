'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/60059

<자물쇠와 열쇠>
'''
def rotate(a):
    n = len(a)      # 행의 길이
    m = len(a[0])   # 열의 길이
    result = [[0] * n for _ in range(m)] # 새로운 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j] # 우측으로 90도 회전된 위치로 리스트 생성
    return result

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock): 
    n = len(lock)  # 자물쇠의 길이
    m = len(key)   # 열쇠의 길이

    # 자물쇠의 3배로 새로운 자물쇠 생성
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 3배 늘어난 자물쇠 가운데에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[n + i][n + j] = lock[i][j]

    for rotation in range(4):
        key = rotate(key) # 열쇠 회전
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                if check(new_lock):
                    return True

                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
    return False