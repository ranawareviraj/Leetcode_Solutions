class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        #1) Replace the punctuations with spaces,
        #   and put all letters in lower case
        paragraph = "".join([ c.lower() if c.isalnum() else " " for c in paragraph ])
        
        #2) Split the string into words
        words = paragraph.split()
        
        words_counter = defaultdict(int)
        banned_words = set(banned)
        
        #3) Count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                words_counter[word] += 1
        
        #4) Return the word with the highest frequency
        most_common_word = ""
        max_freq = 0
        for word, freq in words_counter.items():
            if freq > max_freq:
                max_freq = freq
                most_common_word = word
                
        return most_common_word
        
        