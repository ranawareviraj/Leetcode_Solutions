class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heap = [ x for x in sticks]
        heapify(heap)
        cost = 0
        
        while len(heap) >= 2:
            s1 = heappop(heap)
            s2 = heappop(heap)
            
            combined_stick = s1 + s2
            cost += combined_stick
            heappush(heap, combined_stick)
            
        return cost