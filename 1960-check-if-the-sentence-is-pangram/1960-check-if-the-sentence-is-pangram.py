class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for ch in ascii_lowercase:
            if ch not in sentence:
                return False
        # If we reach here, then we have all alphabets in the sentence - Pangram
        return True
            