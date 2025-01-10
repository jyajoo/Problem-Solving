"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/72410

< 신규 아이디 추천 >
"""


def solution(new_id):
    new_id = new_id.lower()
    x = ""
    for i in new_id:
        if i.islower() or i.isdigit() or i == "_" or i == "." or i == "-":
            x += i
    while ".." in x:
        x = x.replace("..", ".")

    if x.startswith("."):
        x = x[1:]
    if x.endswith("."):
        x = x[:-1]
    if len(x) == 0:
        x += "a"
    if len(x) >= 16:
        x = x[:15]
    if x.endswith("."):
        x = x[:-1]
    if len(x) <= 2:
        x += x[-1] * (3 - len(x))
    print(x)
    return x
