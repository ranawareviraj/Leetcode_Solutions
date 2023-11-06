class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(current_combination, start):
            if len(current_combination) == k:
                combinations.append(current_combination[:])
                return
            
            need = k - len(current_combination)
            remaining = n + 1 - start
            available = remaining - need

            for num in range(start, start + available + 1):
                current_combination.append(num)
                backtrack(current_combination, num + 1)
                current_combination.pop()
        
        combinations = []
        backtrack([], 1)
        return combinations


