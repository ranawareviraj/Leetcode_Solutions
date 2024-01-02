class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        counter = Counter(arr)
        seen = set()
        count = 0
        for word in arr:
            if word not in seen and counter[word] == 1:
                count += 1
                if count == k:
                    return word
            seen.add(word)
        
        return ""