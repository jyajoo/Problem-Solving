'''
< 순차 탐색 > 
'''

def sequential_search(n, target, arr):
    for i in range(n):
        if arr[i] == target:
            return i + 1
        
print("생성할 원소 개수 입력 후 문자열 입력")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수만큼 문자열 입력")
arr = input().split()

print(sequential_search(n, target, arr))