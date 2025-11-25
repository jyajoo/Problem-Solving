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

'''
A -> B로 찾아가는 방식은 두 갈래로 계속 갈라지는데, B -> A로 가는 방식은 어떨까?

1. 2로 나누어떨어진다면 2로 무조건 나눌 수 있다.
2. 일의 자리가 1이 라면 1을 무조건 뗄 수 있다
3. 둘다 불가능하다면 A를 만들 수 없다.

그리디 - 순간 가장 좋은 것을 선택하는 알고리즘

시간복잡도는 O(logB)
'''
a, b = map(int, input().split())
result = 0

while True:
    if b < a:
        result = -1
        break

    if b % 2 == 0:
        result += 1
        b //= 2
    elif str(b)[-1] == '1':
        result += 1
        b = int(str(b)[:-1])
    else:
        result = -1
        break

    if b == a:
        result += 1
        break
print(result)