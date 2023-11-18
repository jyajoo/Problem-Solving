"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV5LsaaqDzYDFAXc&categoryId=AV5LsaaqDzYDFAXc&categoryType=CODE&problemTitle=&orderBy=SUBMIT_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=1

< 진기의 최고급 붕어빵 >
"""
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, M, K = map(int, input().split())
        time = list(map(int, input().split()))
        time.sort()
        answer = "Possible"
        for x in range(N):
            if (time[x] // M) * K >= (x + 1):
                continue
            else:
                answer = "Impossible"
                break

        print("#{} {}".format(t + 1, answer))
