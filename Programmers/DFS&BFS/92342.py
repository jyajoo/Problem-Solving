"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/92342

< 양궁 대회 >
"""

import copy

score_diff = 0
answer_list = []


def dfs(lion_info, n, step, info):
    global score_diff, answer_list

    if n < 0:
        return
    if step == 11:
        if n != 0:
            lion_info[-1] = n
        lion_score = apeach_score = 0
        for i in range(11):
            if info[i] == lion_info[i] == 0:
                continue
            elif info[i] < lion_info[i]:
                lion_score += 10 - i
            else:
                apeach_score += 10 - i

        if apeach_score < lion_score:
            if score_diff < lion_score - apeach_score:
                score_diff = lion_score - apeach_score
                answer_list = []
                answer_list.append(copy.deepcopy(lion_info[:]))
            elif score_diff == lion_score - apeach_score:
                answer_list.append(copy.deepcopy(lion_info[:]))
        return

    apeach_n = info[step]

    # 해당 점수판(step)을 포기한다.
    lion_info[step] = 0
    dfs(lion_info, n, step + 1, info)

    # 해당 점수판을 뺏는다.
    lion_info[step] = apeach_n + 1
    n -= apeach_n + 1
    dfs(lion_info, n, step + 1, info)


def solution(n, info):
    lion_info = [0] * 11
    dfs(lion_info, n, 0, info)
    answer_list.sort(reverse=True, key=lambda x: (x[10::-1]))
    if len(answer_list) == 0:
        return [-1]
    return answer_list[0]


# n = 5
# info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
# n = 1
# info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# n = 9
# info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
n = 10
info = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]


print(solution(n, info))


"""
"""


def calculate_diff(apeach, lion):
    apeach_sc = lion_sc = 0
    lion += [0] * (11 - len(lion))
    for i in range(11):
        if apeach[i] == 0 and lion[i] == 0:
            continue
        if apeach[i] < lion[i]:
            lion_sc += 10 - i
        elif apeach[i] == lion[i]:
            apeach_sc += 10 - i
        else:
            apeach_sc += 10 - i
    return lion_sc - apeach_sc


def backtracking(step, n, apeach, lion):
    global diff, answer
    if step >= 11 or n == 0:
        d = calculate_diff(apeach, lion)
        if d > diff:
            diff = d
            answer = []
            answer.append(lion)
        elif d == diff:
            answer.append(lion)
        return

    # 이길 경우
    if apeach[step] < n:
        backtracking(
            step + 1, n - (apeach[step] + 1), apeach, lion + [apeach[step] + 1]
        )

    # 비길 경우
    elif apeach[step] <= n:
        backtracking(step + 1, n - apeach[step], apeach, lion + [apeach[step]])

    # 질 경우
    if step == 10:
        backtracking(step + 1, 0, apeach, lion + [n])
    else:
        backtracking(step + 1, n, apeach, lion + [0])


diff = 0
answer = []


def solution(n, info):
    backtracking(0, n, info, [])

    if len(answer) == 0 or diff == 0:
        return [-1]
    else:
        answer.sort(reverse=True, key=lambda x: (x[10::-1]))
        return answer[0]
