"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/42883#

< 큰 수 만들기 >
"""


def solution(number, k):
    answer = ""
    answer += number[0]
    cnt = k
    for i in range(1, len(number)):
        while len(answer) > 0:
            if int(answer[-1]) < int(number[i]) and cnt > 0:
                cnt -= 1
                answer = answer[:-1]
            else:
                break
        answer += number[i]
    return answer[: len(number) - k]


"""
"""


def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]

    return "".join(stack)
