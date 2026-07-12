from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seem = set()
        for each in nums:
            if each in seem:
                return True
            else:
                seem.add(each)
        return False


nums = [1, 2, 3, 1]
sol = Solution()
print(sol.containsDuplicate(nums))  # Output: True  

nums = [1, 2, 3, 4]
sol = Solution()
print(sol.containsDuplicate(nums))  # Output: False