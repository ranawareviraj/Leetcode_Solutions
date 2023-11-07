class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        heap = []

        for num in freq_map:
            heapq.heappush(heap, (freq_map[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [val[1] for val in heap]



        