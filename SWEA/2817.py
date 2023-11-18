"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV7IzvG6EksDFAXB&categoryId=AV7IzvG6EksDFAXB&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

< 부분 수열의 합 >
"""

def dfs(x, val):
    global answer

    if val > k:
        return

    if x == n:
        if val == k:
            answer += 1
        return
    dfs(x + 1, val + numbers[x])
    dfs(x + 1, val)


if __name__ == "__main__":
    T = int(input())

    for t in range(T):
        n, k = map(int, input().split())
        numbers = list(map(int, input().split()))
        answer = 0
        dfs(0, 0)

        print("#{} {}".format(t + 1, answer))
