"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV15Khn6AN0CFAYD&categoryId=AV15Khn6AN0CFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1#

< [S/W 문제해결 응용] 2일차 - 최대 상금 >
"""
def dfs(n):
    global answer
    if n == int(change):
        answer = max(answer, int("".join(map(str, lst))))
        return

    # 두 개의 원소를 뽑기 (조합)
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            # 이미 체크한 경우가 아닌 경우에만 dfs 실행 (중복 방지)
            num = int("".join(map(str, lst)))
            if (n, num) not in visited:
                dfs(n + 1)  
                visited.append((n, num))

            # 반드시 원상 복구 해주기
            lst[i], lst[j] = lst[j], lst[i]


T = int(input())
for x in range(T):
    number, change = input().split()

    lst = []
    for ch in number:
        lst.append(int(ch))

    L = len(lst)
    answer = 0
    visited = []
    dfs(0)

    print("#{} {}".format(x + 1, answer))
