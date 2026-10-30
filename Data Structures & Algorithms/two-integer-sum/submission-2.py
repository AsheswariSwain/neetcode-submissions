class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums and nums.index(diff) != i:
                if nums.index(diff) < i:
                    return [nums.index(diff), i]
                else:
                    return [i, nums.index(diff)]