class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        conflict = set()
        for x in nums:
            if x in conflict:
                return True
            else:
                conflict.add(x)
        return False
                