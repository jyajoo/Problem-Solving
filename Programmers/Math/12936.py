'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12936

< 줄 서는 방법 >
'''
def factorial(n):
    result = 1
    x = n
    for i in range(n, 0, -1):
        result *= x
        x -= 1
    return result

def solution(n, k):
    answer = []
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            f = factorial(n - i)
            if j not in answer:
                if k - f > 0:
                    k -= f
                else:
                    answer.append(j)
                    break
    return answer