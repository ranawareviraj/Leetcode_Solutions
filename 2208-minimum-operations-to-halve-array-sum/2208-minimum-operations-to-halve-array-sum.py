class Solution:
    def halveArray(self, nums: List[int]) -> int:
        curr_sum = sum(nums) / 2
        count = 0
        heap = [ -x for x in nums]
        heapify(heap)
        
        while curr_sum > 0:
            top = -heappop(heap)
            half = top / 2
            curr_sum -= half
            heappush(heap, -half)
            count += 1
        
        return count
