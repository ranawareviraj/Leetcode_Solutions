class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)

        h_index = 0
        for num in citations:
            if num > h_index:
                h_index += 1
            else:
                break
                
        return h_index
