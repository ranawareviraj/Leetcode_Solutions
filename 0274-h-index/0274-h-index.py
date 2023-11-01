class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        print(citations)
        result = 0
        for num in citations:
            if num > result:
                result += 1
        
        return result
