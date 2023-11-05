class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_subset, current_index):
            
            subsets.append(current_subset[:]) 

            for i in range(current_index, n):
               current_subset.append(nums[i])
               backtrack(current_subset, i + 1)
               current_subset.pop()

        n = len(nums)
        subsets = []
        backtrack([], 0)
        return subsets