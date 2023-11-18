"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=2&contestProbId=AV5PwGK6AcIDFAUq&categoryId=AV5PwGK6AcIDFAUq&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=2&pageSize=10&pageIndex=2

< 조교의 성적 매기기 >
"""
if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        scores = [list(map(int, input().split())) for _ in range(N)]
        results = []
        i = 1
        for score in scores:
            result = score[0] * 0.35 + score[1] * 0.45 + score[2] * 0.20
            results.append((i, result))
            i += 1
        results.sort(key=lambda x: -x[1])

        answer = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
        idx = 0
        answer_idx = 0
        for i, result in results:
            # print(i, result)
            if idx == N // 10:
                idx = 0
                answer_idx += 1
            if i == K:
                break
            idx += 1

        print("#{} {}".format(t + 1, answer[answer_idx]))
