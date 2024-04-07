class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_ship_with_capacity(capacity):
            curr_weight = 0
            days_needed = 1

            for weight in weights:
                curr_weight += weight
                if curr_weight > capacity:
                    days_needed += 1
                    curr_weight = weight
                    
            return days_needed <= days 


        left = max(weights) # min_capacity
        right = sum(weights) # max_capacity

        while left < right:
            mid = (left + right) // 2

            if(can_ship_with_capacity(mid)):
                right = mid
            else:
                left = mid + 1

        return right

