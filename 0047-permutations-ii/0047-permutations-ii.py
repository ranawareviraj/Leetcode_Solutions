class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(current_permutation, seen):
            if len(current_permutation) == len(nums):
                val = [str(x) for x in current_permutation]
                val = "".join(val)

                if val not in permutations_set:
                    permutations.append(current_permutation[:])
                    permutations_set.add(val)
                return

            for (index, num) in enumerate(nums):
                if (index, num) not in seen:
                    current_permutation.append(num)
                    seen.add((index, num))

                    backtrack(current_permutation, seen)

                    current_permutation.pop()
                    seen.remove((index, num))
            
        permutations = []
        permutations_set = set()
        backtrack([], set())
        return permutations