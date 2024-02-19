"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/60060

< 가사 검색 >
"""

from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_idx = bisect_right(a, right_value)
    left_idx = bisect_left(a, left_value)

    return right_idx - left_idx


# 모든 단어를 길이마다 나누어서 저장하는 리스트
array = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하는 리스트
array2 = [[] for _ in range(10001)]


def solution(words, queries):
    answer = []

    for word in words:
        # 단어 길이에 해당하는 리스트에 삽입
        array[len(word)].append(word)
        array2[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        array2[i].sort()

    for q in queries:
        if q[0] != "?":
            res = count_by_range(
                array[len(q)], q.replace("?", "a"), q.replace("?", "z")
            )
        else:
            res = count_by_range(
                array2[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z")
            )

        answer.append(res)

    return answer
