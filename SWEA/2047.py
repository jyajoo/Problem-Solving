"""
swea - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=1&contestProbId=AV5QKsLaAy0DFAUq&categoryId=AV5QKsLaAy0DFAUq&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=1&pageSize=10&pageIndex=1

< 신문 헤드라인 >
"""

arr = list(input().split("_"))
for i in range(len(arr)):
    arr[i] = str.upper(arr[i])

print('_'.join(arr))