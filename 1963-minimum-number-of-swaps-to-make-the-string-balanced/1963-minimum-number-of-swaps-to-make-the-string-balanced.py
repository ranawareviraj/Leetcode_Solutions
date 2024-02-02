class Solution:
    def minSwaps(self, s: str) -> int:
        # stack = []
        count = 0
        res = 0
        matches = 0
        for i in s:
            if i == '[':
                count += 1
                matches += 1
            else:
                matches -= 1
                if count>0:
                    count -= 1
                    continue
                else:
                    res += 1
        return -1 if matches != 0 else ceil(res/2)