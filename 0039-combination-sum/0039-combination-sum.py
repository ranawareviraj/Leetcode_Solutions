class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(current_combination, current_sum):
            if current_sum == target:
                val = [str(x) for x in sorted(current_combination)]
                val = "".join(val)

                if val not in combinations_set:
                    combinations_set.add(val)
                    combinations.append(current_combination[:])
                return
            
            if current_sum > target:
                return
            
            for candidate in candidates:
                current_combination.append(candidate)

                backtrack(current_combination, current_sum + candidate) 
                
                current_combination.pop()

        combinations = []
        combinations_set = set()
        backtrack([], 0)
        return combinations