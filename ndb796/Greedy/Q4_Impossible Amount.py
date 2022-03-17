'''
< 만들 수 없는 금액 >

- 동전 단위로 만들 수 있는 가장 큰 값까지 차례대로 만들 수 없는 양의 점수를 찾아나간다.
- 동전 단위가 큰 것부터 정수로부터 빼준다. (단, 동전의 단위가 정수보다 작아야 한다.)
- 뺄 수 있는 동전들을 모두 빼주었음에도 결과가 0이 되지 않는 경우를 출력
'''

n = int(input())
coins = list(map(int, input().split()))

coins.sort(reverse=True)

for i in range(1, sum(coins) + 2):
    result = i
    for j in coins:
        if j <= result:
            result -= j
    if result != 0:
        print(i)
        break
