class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        for ch in s:
            if stack:
                if stack[-1][0] == ch:
                    ch, freq = stack.pop()
                    if freq < k - 1:
                        stack.append((ch, freq + 1))
                else:
                    stack.append((ch, 1))
            else:
                stack.append((ch, 1))

        result = []
        for ch, n in stack:
            result.extend([ch] * n)
        
        return "".join(result)