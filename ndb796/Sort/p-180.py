'''
< 성적이 낮은 순서로 학생 출력하기 >
'''
n = int(input())
arr = []
for _ in range(n):
    name, score = input().split()
    arr.append((name, int(score)))

arr.sort(key = lambda student : student[1])
for student in arr:
    print(student[0], end = " ")