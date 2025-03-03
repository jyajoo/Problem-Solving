"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/64065

< 튜플 >
"""


def solution(s):
    s = s.replace("{", "")
    s = s.replace(",", " ")
    s = s.split("}")
    numbers = []
    for i in s:
        if len(i):
            a = set(map(int, i.strip().split()))
            numbers.append(a)
    numbers.sort(key=lambda x: len(x))

    answer = []
    ex = set()
    for i in numbers:
        new = i - ex
        ex = ex | new
        answer.append(new.pop())
    return answer


"""
"""


def solution(s):
    s = s.lstrip("{").rstrip("}").split("},{")

    numbers = []
    for i in s:
        numbers.append(list(map(int, i.split(","))))

    numbers.sort(key=len)
    answer = []
    for i in numbers:
        for j in range(len(i)):
            if i[j] not in answer:
                answer.append(i[j])

    return answer

'''
'''
def solution(s):
    s = s[1:-1]
    s = s.replace('}', '')
    s = s.replace(',', ' ')
    s = s.split('{')
    arr = []
    for i in s:
        if len(i) != 0:
            arr.append(list(map(int, i.strip().split(' '))))
    arr.sort(key = lambda x : len(x))
    answer = []
    for i in arr:
        sa = set(answer)
        si = set(i)
        ss = list(si - sa)
        answer.append(ss[0])
    return answer
