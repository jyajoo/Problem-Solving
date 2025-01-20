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


"""
"""


def solution(brown, yellow):
    """
    yellow + brown = 총 격자의 개수
    가로 세로를 곱하여 총 격자의 개수와 동일해야 한다.
    가로 >= 세로이자, 가로 - 세로의 격차가 가장 작은 경우
    노란색 개수 확인
    """

    total_count = brown + yellow

    gap = int(1e9)
    answer = []
    for i in range(1, int(total_count ** (1 / 2)) + 1):
        if total_count % i == 0:
            x, y = total_count // i, i
            if yellow == (x - 2) * (y - 2) and gap >= x - y:
                gap = x - y
                answer = [x, y]
    return answer
