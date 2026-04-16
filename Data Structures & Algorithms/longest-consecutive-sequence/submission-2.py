class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_streak = 0
        
        for n in nums:
            if n - 1 not in set_nums:
                current_n = n
                count = 1
                while current_n + 1 in set_nums:
                    current_n += 1
                    count += 1
                longest_streak = max(longest_streak, count)
        
        return longest_streak

        