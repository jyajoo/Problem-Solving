'''
프로그래머스 - https://school.programmers.co.kr/learn/courses/30/lessons/43165

< 타겟 넘버 >
'''
# 풀이 1
def solution(numbers, target):
    def dfs(numbers, target, current, idx):
        if idx == len(numbers) :   # 모든 정점의 끝인 경우, target과 동일한지 확인
            if current == target:
                return 1
            else:
                return 0
            
        # 다음 정점으로 이동하여 다시 DFS
        return dfs(numbers, target, current + numbers[idx], idx + 1) + dfs(numbers, target, current - numbers[idx], idx + 1)
    
    answer = dfs(numbers, target, 0, 0)
    return answer
        

# 풀이 2
cnt = 0

def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return

    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt