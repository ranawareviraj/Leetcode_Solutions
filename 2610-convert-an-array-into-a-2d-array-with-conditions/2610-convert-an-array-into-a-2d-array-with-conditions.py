class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [0] * (n + 1)
        ans = []

        for num in nums:
            if freq[num] >= len(ans):
                ans.append([])

            # Store the integer in the list corresponding to its current frequency.
            ans[freq[num]].append(num)
            freq[num] += 1

        return ans
