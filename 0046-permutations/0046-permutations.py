class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, curr, ans):
            if len(curr) == len(nums):
                ans.append(curr[:])
                return
            
            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(nums, curr, ans)
                    curr.pop()
            
        ans = []
        backtrack(nums, [], ans)
        return ans