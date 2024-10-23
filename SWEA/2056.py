"""
swea = https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QLkdKAz4DFAUq&categoryId=AV5QLkdKAz4DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

< 연월일 달력 >
"""

T = int(input())

for t in range(T):
    date = input().strip()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    answer = ""

    if int(month) in [1, 3, 5, 7, 8, 10, 12]:
        if int(day) < 1 or int(day) > 31:
            answer = "-1"
        else:
            answer = year + "/" + month + "/" + day
    elif int(month) in [4, 6, 9, 11]:
        if int(day) < 1 or int(day) > 30:
            answer = "-1"
        else:
            answer = year + "/" + month + "/" + day
    elif int(month) == 2:
        if int(day) < 1 or int(day) > 28:
            answer = "-1"
        else:
            answer = year + "/" + month + "/" + day
    else:
        answer = "-1"

    print("#%d " % (t + 1) + answer)
"""
"""
T = int(input())

for t in range(T):
    date = input().strip()
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    answer = ""
    month_day = {
        1: 31,
        2: 28,
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

    if (
        month_day.get(int(month))
        and int(day) >= 1
        and int(day) <= month_day.get(int(month))
    ):
        answer = year + "/" + month + "/" + day
    else:
        answer = "-1"

    print("#%d " % (t + 1) + answer)
