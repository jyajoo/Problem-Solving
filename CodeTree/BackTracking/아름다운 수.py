"""
코드 트리 - https://www.codetree.ai/missions/2/problems/beautiful-number?&utm_source=clipboard&utm_medium=text

< 아름다운 수 >
"""
def dfs(step):
    global answer
    if step == n:
        idx = 0
        while idx < n:
            x = num[idx]
            count = 0
            flag = False
            for i in range(idx, n):
                if num[i] == x:
                    count += 1
                else:
                    flag = True
                    break

            if count % x == 0:
                if flag:  # 계속해서 진행
                    idx = i
                else:
                    answer += 1
                    return
            else:
                return

    for i in range(1, 5):
        num.append(i)
        dfs(step + 1)
        num.pop()


n = int(input())


num = []
answer = 0
dfs(0)
print(answer)
'''
'''
def is_beautiful():
    idx = 0
    while idx < n:
        if idx + num[idx] - 1 >= n:
            return False

        for i in range(idx, idx + num[idx]):
            if num[i] != num[idx]:
                return False
        idx += num[idx]
    return True


def dfs(step):
    global answer
    if step == n:
        if is_beautiful():
            answer += 1
        return

    for i in range(1, 5):
        num.append(i)
        dfs(step + 1)
        num.pop()


n = int(input())

num = []
answer = 0
dfs(0)
print(answer)
