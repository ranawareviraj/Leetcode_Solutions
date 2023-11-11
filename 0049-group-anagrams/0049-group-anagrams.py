class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for word in strs:
            key = [0] * 26
            for ch in word:
                key[ord(ch) - ord('a')] += 1
            key = "-".join([str(num) for num in key])
            map[key].append(word)
        
        return map.values()
