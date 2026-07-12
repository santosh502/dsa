class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n%2
            n=n//2
        return res
    
    def hammingWeightBitManipulation(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res
        

n = 11
sol = Solution()
print(sol.hammingWeight(n))  # Output: 3
print(sol.hammingWeightBitManipulation(n))  # Output: 3