class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_count = curr_count = 0
        prev_number = -math.inf

        for x in nums:
            if x > prev_number:
                curr_count += 1
                max_count = max(max_count, curr_count)
            else:
                curr_count = 1
            
            prev_number = x
        
        return max_count