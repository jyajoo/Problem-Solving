"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42842

< 카펫 >
"""


def solution(brown, yellow):
    answer = []

    y_w, y_h = 0, 0

    if yellow == 1:
        y_w, y_h = 1, 1

    for h in range(1, yellow // 2 + 1):
        y_w, y_h = yellow // h, h

        if y_w < y_h:
            break

        if yellow % y_h == 0 and brown == (y_w + 2) * 2 + y_h * 2:
            break

    answer = [y_w + 2, y_h + 2]
    return answer
