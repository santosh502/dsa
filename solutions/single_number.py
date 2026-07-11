from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for each in nums:
            result = result^each
        return result
    

nums = [4, 1, 2, 1, 2]
sol = Solution()
print(sol.singleNumber(nums))