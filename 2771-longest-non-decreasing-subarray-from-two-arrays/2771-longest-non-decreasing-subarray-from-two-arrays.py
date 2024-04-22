class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = dp1 = dp2 = 1
        for i in range(1, len(nums1)):
            t11 = dp1 + 1 if nums1[i - 1] <= nums1[i] else 1
            t12 = dp1 + 1 if nums1[i - 1] <= nums2[i] else 1
            t21 = dp2 + 1 if nums2[i - 1] <= nums1[i] else 1
            t22 = dp2 + 1 if nums2[i - 1] <= nums2[i] else 1
            dp1 = max(t11, t21)
            dp2 = max(t12, t22)
            res = max(res, dp1, dp2)
        return res