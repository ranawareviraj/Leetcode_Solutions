class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = sorted(zip(capital, profits))
        print(projects)
        heap = []
        i = 0
        
        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(heap, -projects[i][1])
                i += 1
            
            if len(heap) == 0:
                # not enough money to do any more projects
                return w
            
            # minus because we stored negative numbers on the heap
            w -= heapq.heappop(heap)
        
        return w    