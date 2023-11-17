'''
SWEA - https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

< 홀수만 더하기 >
'''
T = int(input())
for i in range(T):
    numbers = list(map(int, input().split()))
    answer = 0
    for n in numbers:
        if n % 2 != 0:
            answer += n
    
    print("#%d" % (i + 1), end = " ")
    print(answer)