class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            heaviest = heapq.heappop(max_heap)
            second_heaviest = heapq.heappop(max_heap)

            if heaviest != second_heaviest:
                heapq.heappush(max_heap, -abs(heaviest - second_heaviest))
        
        top = 0
        if max_heap:
            top = -max_heap[0]
        return top