"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/81303#

< 표 편집 >
"""

from collections import defaultdict


def solution(n, k, cmd):
    dict = defaultdict(list)
    for i in range(n):
        dict[i] = [i - 1, i + 1]  # 이전 행, 다음 행 포인터 설정

    dict[0][0] = n - 1
    dict[n - 1][1] = 0

    z_list = []
    answer = ["O"] * n
    for c in cmd:
        # 현재 행 삭제, 바로 아래 행 선택.
        if c == "C":
            prev, next = dict[k]  # 현재 행의 이전 행과 다음 행
            # 현재 행을 삭제하므로 prev의 다음 행을 교체해주기 & next의 이전 행 교체해주기
            dict[prev][1] = next
            dict[next][0] = prev
            z_list.append((prev, k, next))  # 복구될 수 있으므로 기록
            del dict[k]
            answer[k] = "X"
            if next == 0:  # 마지막 행을 삭제한 경우
                k = prev  # k는 바로 윗 행을
            else:
                k = next  # k는 다음 행을 가리키도록

        # 최근 삭제한 행을 복구.
        elif c == "Z":
            prev, now, next = z_list.pop()
            # 복구되므로 prev의 다음 행을 교체해주기 & next의 이전 행 교체해주기
            dict[prev][1] = now
            dict[next][0] = now
            dict[now] = [prev, next]
            answer[now] = "O"

        else:
            a, b = c.split()
            # b칸 위에 있는 행을 선택
            if a == "U":
                for i in range(int(b)):
                    prev, _ = dict[k]
                    k = prev
            # b칸 아래에 있는 행 선택
            elif a == "D":
                for i in range(int(b)):
                    _, next = dict[k]
                    k = next
    return "".join(answer)
