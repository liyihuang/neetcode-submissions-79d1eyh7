class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = set(nums)
        for i,v in enumerate(nums):
            p = target-v
            if p in nums_set:
                j = nums.index(p)
                if i != j:
                    return sorted([i, j])