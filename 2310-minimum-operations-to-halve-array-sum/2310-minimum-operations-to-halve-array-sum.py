class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = 0
        current_sum = 0
        max_heap = []

        for num in nums:
           max_heap.append(-num) 
           total_sum += num

        heapq.heapify(max_heap)
        total_sum = total_sum / 2
        count = 0

        while current_sum < total_sum:
            max_element = heapq.heappop(max_heap)
            remaining_number = max_element / 2

            current_sum += (-remaining_number)
            heapq.heappush(max_heap, remaining_number)
            count += 1
        
        return count


        