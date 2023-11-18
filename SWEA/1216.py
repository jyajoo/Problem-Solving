"""
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV14Rq5aABUCFAYi&categoryId=AV14Rq5aABUCFAYi&categoryType=CODE&problemTitle=&orderBy=RECOMMEND_COUNT&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=2

< [S/W 문제해결 기본] 3일차 - 회문2 >
"""


def is_pal(arr, leng):
    for lst in arr:
        for i in range(100 - leng + 1):
            # if lst[i:i + leng] == lst[i:i + leng][::-1]:
            #     return True

            for j in range(leng // 2):
                if lst[i + j] != lst[i + leng - 1 - j]:
                    break
            else:  # break 안한 경우 else 실행
                return True
    return False


if __name__ == "__main__":
    for t in range(10):
        n = int(input())
        arr1 = [input() for _ in range(100)]
        arr2 = ["".join(x) for x in zip(*arr1)]

        for leng in range(100, 1, -1):
            if is_pal(arr1, leng) or is_pal(arr2, leng):
                break

        print("#{} {}".format(t + 1, leng))
