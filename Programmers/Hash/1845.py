def solution(nums):
    num = []
    for i in nums:
        if i not in num:
            num.append(i)
    
    if len(num) > len(nums) // 2:
        return len(nums) // 2
    return len(num)