"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42860

< 조이스틱 >
"""


def solution(name):
    answer = 0

    move = len(name) - 1
    for i, n in enumerate(name):
        # 상하로 알파벳을 변동할 때의 최솟값
        answer += min(abs(ord(n) - ord("A")), abs(ord("Z") - ord(n)) + 1)

        # 좌우로 위치를 변동할 때의 최솟값
        idx = i + 1
        while idx < len(name) and name[idx] == "A":
            idx += 1

        move = min(move, i * 2 + (len(name) - idx), i + 2 * (len(name) - idx))

    return answer + move
