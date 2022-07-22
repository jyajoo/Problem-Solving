'''
백준 - https://www.acmicpc.net/problem/16652

<Email Desturcton>
- 첫 번째 이메일 : 소문자로 이루어진 제목
- 그 후 이메일 : Re: + 제목

- 공격 당한 후 남은 메일 수를 보고, 이전 메일 수를 계산한다.
- 예측했던 이전 메일 수보다 많게 나오면, 추청 불가능.
'''

# n : 이전 메일 수, k : 공격당한 후 남은 메일 수
n, k = map(int, input().split())
subject = []
cnt = []
for _ in range(k):
    email = input().split("Re: ")
    if email[len(email) - 1] not in subject:
        subject.append(email[len(email) - 1])
        cnt.append(len(email))
    else:
        idx = subject.index(email[len(email) - 1])
        if cnt[idx] < len(email):
            cnt[idx] += len(email) - cnt[idx]

result = 0
for i in cnt:
    result += i
if result <= n:
    print("YES")
else:
    print("NO")
