'''
< 만들 수 없는 금액 >

- 동전 단위로 만들 수 있는 가장 큰 값까지 차례대로 만들 수 없는 양의 점수를 찾아나간다.
- 동전 단위가 큰 것부터 정수로부터 빼준다. (단, 동전의 단위가 정수보다 작아야 한다.)
- 뺄 수 있는 동전들을 모두 빼주었음에도 결과가 0이 되지 않는 경우를 출력
'''

n = int(input())
coins = list(map(int, input().split()))
answer = 0
coins.sort(reverse=True)

# for i in range(1, sum(coins) + 2)
# sum(coins)까지 모두 만들 수 있는 경우, sum(coins) + 1의 결과가 출력될 수 있도록 한다.
for i in range(1, sum(coins) + 1):   
    result = i
    for j in coins:
        if j <= result:
            result -= j
    if result != 0:
        answer = i
        break

if answer != 0:
    print(answer)
else:
    print(sum(coins) + 1)  # sum(coins)까지 만들 수 없는 금액이 없는 경우

'''
- 동전 단위를 오름차순으로 정렬한다.
- 동전 단위가 target보다 크지는 않는지 확인하여 target인 금액도 만들 수 있는지 확인
- target - 1까지 만들 수 있는 상태인지 확인
'''
n = int(input())
coins = list(map(int, input().split()))
answer = 0
coins.sort()
target = 1           

for i in coins:
    if target < i:
        break
    else:
        target += i  # target - 1까지 모든 금액을 만들 수 있다.
print(target)