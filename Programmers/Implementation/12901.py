"""
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/12901

< 2016년 >
"""


def solution(a, b):
    day = {0: "SUN", 1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT"}
    month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }

    d = 5
    for i in range(1, a):
        m_d = month.get(i)
        d = (d + (m_d % 7)) % 7
    d = (d + (b % 7 - 1)) % 7
    return day.get(d)
