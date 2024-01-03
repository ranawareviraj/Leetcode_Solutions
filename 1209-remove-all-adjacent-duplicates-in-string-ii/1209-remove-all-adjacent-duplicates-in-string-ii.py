class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append((ch, 1))
            else:
                ch, freq = stack.pop()
                if freq < k - 1:
                    stack.append((ch, freq + 1))

        result = []
        for ch, n in stack:
            result.extend([ch] * n)
        
        return "".join(result)