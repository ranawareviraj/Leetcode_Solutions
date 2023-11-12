class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        min_heap = [asteroid for asteroid in asteroids]
        heapq.heapify(min_heap)
        curr_mass = mass

        while min_heap and min_heap[0] <= curr_mass:
            curr_mass += heapq.heappop(min_heap)
        
        return len(min_heap) == 0
        