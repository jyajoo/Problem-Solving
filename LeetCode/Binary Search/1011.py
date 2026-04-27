'''
LeetCode - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

< Capacity To Ship Packages Within D Days >
'''
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        
        answer = int(1e9)
        while start <= end:
            middle = (start + end) // 2

            w = 0
            count = 0
            for i in weights:
                if w + i <= middle:
                    w += i
                else:
                    w = i
                    count += 1
            count += 1

            if count > days:
                start = middle + 1
            else:
                end = middle - 1
                answer = min(answer, middle)

        return answer
