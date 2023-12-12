class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current_permutation, seen):
            if len(current_permutation) == len(nums):
                permutations.append(current_permutation[:])
                # return
            
            for num in nums:
                if num not in seen:
                    # Take element to the current combination
                    current_permutation.append(num)
                    seen.add(num)

                    # Call backtrack recursively to build the combination
                    backtrack(current_permutation, seen)
                    
                    # Remove the last added element from the current combination
                    current_permutation.pop()
                    seen.remove(num)
            
        permutations = []
        backtrack([], set())
        return permutations