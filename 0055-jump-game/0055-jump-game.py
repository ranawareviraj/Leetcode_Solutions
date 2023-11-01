class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True  # The last position is reachable.

        for position in range(n - 2, -1, -1):
            max_jump = min(n - 1, position + nums[position])
            for next_position in range(position + 1, max_jump + 1):
                if dp[next_position]:
                    dp[position] = True
                    break

        return dp[0]
