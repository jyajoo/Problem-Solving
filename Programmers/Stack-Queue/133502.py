"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/133502

< 햄버거 만들기 >
"""


def solution(ingredient):
    answer = 0

    stack = []
    for i in ingredient:
        stack.append(i)
        if len(stack) >= 4 and stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer
