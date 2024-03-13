"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42884#

< 단속카메라 >
"""


def solution(routes):
    routes.sort()
    answer = 0
    cameras = set()
    while True:
        lst = []
        for a, b in routes:
            for camera in cameras:
                if a <= camera <= b:
                    break
            else:
                lst.append((a, b))

        if len(lst) == 0:
            break

        lst.sort(key=lambda x: x[1])
        cameras.add(lst[0][1])

    return len(cameras)
