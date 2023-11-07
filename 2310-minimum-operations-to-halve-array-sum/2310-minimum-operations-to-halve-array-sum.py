class Solution:
    def halveArray(self, nums: List[int]) -> int:
        total_sum = 0
        reduced_sum = 0
        max_heap = []

        for num in nums:
           max_heap.append(-num) 
           total_sum += num

        heapq.heapify(max_heap)
        halved_sum = total_sum / 2
        count = 0

        while reduced_sum < halved_sum:
            max_element = heapq.heappop(max_heap)
            remaining_number = max_element / 2

            reduced_sum += (-remaining_number)
            heapq.heappush(max_heap, remaining_number)
            count += 1
        
        return count


        