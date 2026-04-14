class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n_count = {}
        for n in nums:
            if n not in n_count:
                n_count[n] = 1
            else:
                n_count[n] += 1
        heap = []
        for n in n_count.keys():
            heapq.heappush(heap, (n_count[n], n))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for x in range(k):
            res.append(heapq.heappop(heap)[1])
        return res