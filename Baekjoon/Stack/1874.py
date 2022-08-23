'''
백준 - https://www.acmicpc.net/problem/1874

<스택 수열>

'''
n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num2 = sorted(num)

stack = []
top = 0

result = []
for i in num2:
    stack.append(i)
    result.append("+")
    while(True):
        if len(stack) == 0:
            break

        if num[top] == stack[len(stack) - 1]:
            top += 1
            stack.pop()
            result.append("-")
            if top == n:
                break
        else:
            break
if len(stack) == 0:
    for i in result:
        print(i)
else:
    print("NO")

#########################################################

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))

num2 = sorted(num)

stack = []
result = []

push = 0
pop = 0

while(True):
    while(True):
        if push == n:
            break
        if num2[push] > num[pop]:
            break
        else:
            stack.append(num2[push])
            result.append("+")
            push += 1

    if stack[-1] == num[pop]:
        stack.pop()
        result.append("-")
        pop += 1
        if pop == n:
            for i in result:
                print(i)
            break

    else:
        print("NO")
        break