'''
백준 - https://www.acmicpc.net/problem/1713

< 후보 추천하기 >
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
count = int(input())
arr = list(map(int, input().split()))
students = defaultdict(int)

for i in arr:
    if len(students) < n:
        students[i] += 1
    else:
        if i in students.keys():
            students[i] += 1
        else:
            min_stu = 0
            min_count = int(1e9)
            for (k, v) in students.items():
                if min_count > v:
                    min_count = v
                    min_stu = k
            
            del students[min_stu]
            students[i] += 1

print(*sorted(list(students.keys())))

'''
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
count = int(input())
arr = list(map(int, input().split()))
pictures = []
cnt = []

for i in arr:
    if i in pictures:
        cnt[pictures.index(i)] += 1
    
    else:
        if len(pictures) == n:
            idx = cnt.index(min(cnt))
            del cnt[idx]
            del pictures[idx]
        pictures.append(i)
        cnt.append(1)

print(*sorted(pictures))