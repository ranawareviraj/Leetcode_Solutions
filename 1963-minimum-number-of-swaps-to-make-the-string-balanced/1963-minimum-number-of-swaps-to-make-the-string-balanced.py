class Solution:
    def minSwaps(self, s: str) -> int:


        # stack = []
        count = 0
        res = 0
        for i in s:
            if i == '[':
                count += 1
            else:
                if count>0:
                    count -= 1
                    continue
                else:
                    res += 1
        return ceil(res/2)