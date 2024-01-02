class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        freq = [0] * (n + 1)
        result = []

        for num in nums:
            if freq[num] >= len(result):
                result.append([])

            # Store the integer in the list corresponding to its current frequency.
            result[freq[num]].append(num)
            freq[num] += 1

        return result
