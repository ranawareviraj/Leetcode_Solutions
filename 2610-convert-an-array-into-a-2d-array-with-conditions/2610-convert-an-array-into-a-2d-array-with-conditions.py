class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        print(counter)
        result = []
        while len(counter) > 0:
            row = []
            for key in list(counter.keys()):
                row.append(key)
                counter[key] -= 1
                if counter[key] == 0:
                    del counter[key]
            print(counter)
            result.append(row)
        
        return result
