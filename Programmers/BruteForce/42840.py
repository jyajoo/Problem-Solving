"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42840#

< 모의고사 >
"""
def solution(answers):
    answer = []
    scores = [0] * 3

    num = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for idx, j in enumerate(answers):
        if j == num[idx % 5]:
            scores[0] += 1
        if j == num2[idx % 8]:
            scores[1] += 1
        if j == num3[idx % 10]:
            scores[2] += 1

    val = max(scores)
    for i, s in enumerate(scores):
        if val == s:
            answer.append(i + 1)

    return answer
