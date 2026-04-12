class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = {}
        for n in nums:
            if n not in n_count:
                n_count[n] = 1
            else:
                n_count[n] += 1
        n_length = [[] for _ in range(len(nums)+1)]
        for n,f in n_count.items():
            n_length[f].append(n)
        
        target_list = []
        for x in reversed(n_length):
            for num in x:
                target_list.append(num)
                if len(target_list) == k:
                    return target_list
        return target_list