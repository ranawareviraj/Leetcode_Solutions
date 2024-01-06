class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapify(heap)

        while len(heap) >= 2:
            stone1 = heappop(heap)
            stone2 = heappop(heap)

            if stone1 != stone2:
                heappush(heap, -abs(stone1 - stone2))
        
        return 0 if not heap else -heap[0]