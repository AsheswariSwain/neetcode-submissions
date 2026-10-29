class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        maxc = 0
        for i in nums:
            if i ==1:
                current += 1
                maxc = max(maxc, current)
            else:
                current = 0
        return maxc


        
 