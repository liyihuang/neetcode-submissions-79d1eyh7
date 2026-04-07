class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i,v in enumerate(nums):
            p = target-v
            if p in nums_map:
                return [nums_map[p],i]
            nums_map[v]=i