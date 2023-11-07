class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        
        # While there are at least 2 stones in the heap
        # Pop heaviest two stones
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)
            
            # If weight of stones is not same
            if stone1 != stone2:
                # Put negative diff, indtead of s1-s2, put s2-s1 (Max heap)
                heapq.heappush(heap, -(stone1 - stone2))
        
  		# If no stones left, return 0. Else return weight of stone remaining
        last_remaining_stone = 0
        if len(heap) != 0:
            last_remaining_stone = -heapq.heappop(heap)
						
        return last_remaining_stone