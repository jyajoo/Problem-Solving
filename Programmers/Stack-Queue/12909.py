'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12909

< 올바른 괄호 >

'''

# solution_1
# def solution(s):
#     stack = []
#     for i in s:
#         if i == "(":
#             stack.append("(")
#         else:
#             if len(stack) != 0:
#                 stack.pop()
#             else:
#                 return False
    
#     if len(stack) != 0:
#         return False
#     else:
#         return True

# solution_2

from collections import deque

def solution(s):
    queue = deque()
    for i in s:
        if i == "(":
            queue.append("(")
        else:
            if len(queue) != 0:
                queue.pop()
            else:
                return False
    if len(queue) != 0:
        return False
    else:
        return True

s = "(()("

print(solution(s))