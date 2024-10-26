"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/131701

< 연속 부분 수열 합의 개수 >
"""


def solution(elements):
    length = len(elements)
    result = set()
    for i in range(1, length + 1):
        for start in range(length):
            end = start + i
            if end < length:
                n = sum(elements[start:end])
            else:
                n = sum(elements[start:] + elements[: end % length])
            result.add(n)
    return len(result)


"""
"""


def solution(elements):
    length = len(elements)
    elements = elements * 2
    answer = set()
    for i in range(1, length + 1):
        for start in range(length):
            answer.add(sum(elements[start : start + i]))

    return len(answer)
