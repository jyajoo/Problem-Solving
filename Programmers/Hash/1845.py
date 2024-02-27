"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/1845

< 폰켓몬 >
"""


def solution(nums):
    num = []
    for i in nums:
        if i not in num:
            num.append(i)

    if len(num) > len(nums) // 2:
        return len(nums) // 2
    return len(num)


"""
"""


def solution(nums):
    answer = 0
    l = len(nums)
    nums = set(nums)
    if l // 2 > len(nums):
        answer = len(nums)
    else:
        answer = l // 2
    return answer
