class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n_dict = {}
        res = set()
        for i,v in enumerate(nums):
            n_dict[v] = i

        for i in range(len(nums) - 1):
            for j in range(i+1,len(nums)):
                three = -(nums[i]+ nums[j])
                if three in n_dict and i != n_dict[three] and j != n_dict[three]:
                    triplet = tuple(sorted([nums[i], nums[j], three]))
                    res.add(triplet) 
        return [list(t) for t in res]