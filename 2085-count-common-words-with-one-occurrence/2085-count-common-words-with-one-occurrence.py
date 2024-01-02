class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter1 = Counter(words1)
        counter2 = Counter(words2)

        count = 0
        for word, freq in counter1.items():
            if word in counter2 and  freq == counter2[word] == 1:
                count += 1
            
        return count