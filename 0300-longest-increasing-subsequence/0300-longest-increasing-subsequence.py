class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        sub_seq = [nums[0]]

        for i in range(1, n):
            num = nums[i]

            if num > sub_seq[-1]:
                sub_seq.append(num)
            else:
                j = 0
                while num > sub_seq[j]:
                    j += 1
                sub_seq[j] = num
        
        return len(sub_seq)
