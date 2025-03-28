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
'''
25.03.28
'''
def solution(number, k):
    number = list(map(int, number))
    num_list = []
    cnt = 0
    for n in number:
        if num_list:
            for _ in range(len(num_list)):
                x = num_list[-1]
                if x < n and cnt < k: # 새로운 수가 더 클 때, 기존에 더 작았던 수를 제외시킨다.
                    num_list.pop()
                    cnt += 1
                else:
                    break
            num_list.append(n)
        else:
            num_list.append(n)
    
    if cnt != k:
        num_list = num_list[:-(k - cnt)]
    return ''.join(map(str, num_list))
'''
'''
def solution(number, k):
    num_list = [number[0]]
    for n in number[1:]:
        while num_list and num_list[-1] < n and k > 0:
            num_list.pop()
            k -= 1
        num_list.append(n)
    
    if k > 0:
        num_list = num_list[:-k]
    return ''.join(num_list)