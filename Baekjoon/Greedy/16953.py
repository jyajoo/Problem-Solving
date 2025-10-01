'''
백준 - https://www.acmicpc.net/problem/16953

< A -> B >
'''
import sys

input = sys.stdin.readline

'''
정수 a를 b로 바꾸기

1. 2를 곱한다
2. 1을 수의 가장 오른쪽에 추가한다
a를 b로 바꾸는데 필요한 연산의 최솟값에 1을 더하여 출력
만들 수 없는 경우 -1 출력
'''

'''
a < b <= 10^9
시간 복잡도가 O(N)보다 작아야 한다. (O(N) > O(1), O(logN))

순차적으로 1번 연산과 2번 연산 중 b에 도달하면 바로 출력
전부 b보다 커지게 된다면 -1
-> 이진 트리의 형태로 매 단계마다 2개씩 불어나는 구조
-> 트리의 깊이가 깊어질 수록 시간 복잡도가 커짐
-> 'if i < b' 조건으로 가지치기를 해서 시간 복잡도 내에 풀이 성공

BFS(너비우선탐색) - 해당 깊이에 있는 노드들을 모두 방문한다.
시간 복잡도가 O(logB)
'''

a, b = map(int, input().split())
result = 0
num = [a]

while True:
    new_num = []
    flag = False
    for i in num:
        if i < b:
            x, y = i * 2, int(str(i) + '1')
            new_num.append(x)
            new_num.append(y)
            if x == b or y == b:
                flag = True
                break
    if flag:
        result += 1 + 1
        break
    
    if len(new_num) == 0:
        result = -1
        break
    num = new_num
    result += 1

print(result)