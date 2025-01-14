"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/133499

< 옹알이 (2) >
"""


def solution(babbling):
    answer = 0
    arr = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        word = i
        ex = ""
        while True:
            for x in arr:
                if x != ex and word.startswith(x):
                    word = word[len(x) :]
                    ex = x
                    break
            else:
                break
        if len(word) == 0:
            answer += 1
    return answer
